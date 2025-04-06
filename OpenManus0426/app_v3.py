# app.py
from flask import Flask, render_template, request, jsonify,send_from_directory,Response
import mimetypes
import os
import time
from pathlib import Path
import asyncio
import queue
from app.agent.manus import Manus
from app.logger import logger,log_queue
import threading

app = Flask(__name__)
app.config['WORKSPACE'] = 'workspace'

# 初始化工作目录
os.makedirs(app.config['WORKSPACE'], exist_ok=True)
LOG_FILE = 'logs/root_stream.log'
FILE_CHECK_INTERVAL = 2  # 文件检查间隔（秒）
PROCESS_TIMEOUT = 600      # 最长处理时间（秒）

def get_files_pathlib(root_dir):
    """使用pathlib递归获取文件路径"""
    root = Path(root_dir)
    return [str(path) for path in root.glob('**/*') if path.is_file()]

@app.route('/')
def index():
    files = os.listdir(app.config['WORKSPACE'])
    return render_template('index.html', files=files)


@app.route('/file/<filename>')
def file(filename):
    file_path = os.path.join(app.config['WORKSPACE'], filename)
    if os.path.isfile(file_path):
        mime_type, _ = mimetypes.guess_type(filename)
        if mime_type and mime_type.startswith('text/'):
            if mime_type == 'text/html':
                return send_from_directory(app.config['WORKSPACE'], filename)
            else:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                return render_template('code.html', filename=filename, content=content)
        elif mime_type == 'application/pdf':
            return send_from_directory(app.config['WORKSPACE'], filename)
        # elif mime_type in ['application/vnd.ms-powerpoint',
        #                    'application/vnd.openxmlformats-officedocument.presentationml.presentation']:
        #     return render_template('google_viewer.html', filename=filename, viewer_type='ppt')
        # elif mime_type in ['application/msword',
        #                    'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        #     return render_template('google_viewer.html', filename=filename, viewer_type='word')
        # elif mime_type in ['application/vnd.ms-excel',
        #                    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
        #     return render_template('google_viewer.html', filename=filename, viewer_type='excel')
        # elif mime_type in ['application/vnd.ms-powerpoint',
        #                    'application/vnd.openxmlformats-officedocument.presentationml.presentation']:
        #     return render_template('google_viewer.html', filename=filename, viewer_type='ppt')
        # elif mime_type in ['application/msword',
        #                    'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        #     return render_template('google_viewer.html', filename=filename, viewer_type='word')
        # elif mime_type in ['application/vnd.ms-excel',
        #                    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
        #     return render_template('google_viewer.html', filename=filename, viewer_type='excel')

        else:
            return send_from_directory(app.config['WORKSPACE'], filename)
    else:
        return "File not found", 404


async def main(prompt):
    agent = Manus()
    await agent.run(prompt)


# 线程包装器
def run_async_task(message):
    """在新线程中运行异步任务"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(message))
    loop.close()


@app.route('/api/chat-stream', methods=['POST'])
def chat_stream():
    """流式日志接口"""
    # 清空日志文件
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    # 获取请求数据
    prompt = request.get_json()
    print("收到请求:", prompt)

    # 启动异步任务线程
    task_thread = threading.Thread(
        target=run_async_task,
        args=(prompt["message"],)
    )
    task_thread.start()

    # 流式生成器
    def generate():
        start_time = time.time()

        while task_thread.is_alive() or not log_queue.empty():
            # 超时检查
            if time.time() - start_time > PROCESS_TIMEOUT:
                yield "\n[错误] 处理超时\n"
                break
            new_content = ""
            try:
                new_content = log_queue.get(timeout=0.1)
            except queue.Empty:
                pass

            if new_content:
                yield new_content

            # 无新内容时暂停
            if not new_content:
                time.sleep(FILE_CHECK_INTERVAL)

        # 最终确认
        yield "\n[完成] 处理结束\n"

    return Response(generate(), mimetype="text/plain")



if __name__ == '__main__':
    app.run(debug=True)
    # 帮我用html语言生成贪吃蛇游戏
    # 搜索 Manus Agent 的信息和报道，生成一个 html 用来汇总和报告这个 Agent，你的 html 应该尽可能美观。