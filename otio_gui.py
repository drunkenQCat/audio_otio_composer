import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from datetime import datetime
from otio_generator import get_audio_clips, audio_to_tracks, make_otio

def launch_gui():
    def browse_path():
        directory = filedialog.askdirectory()
        if directory:
            path_entry.delete(0, tk.END)
            path_entry.insert(0, directory)
            refresh_task_list()

    def refresh_task_list():
        """刷新任务列表，显示最新的20个文件夹"""
        path = path_entry.get()
        if not path or not os.path.exists(path):
            return
        
        # 清空现有列表
        task_listbox.delete(0, tk.END)
        
        try:
            # 获取所有文件夹
            folders = []
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    # 获取文件夹创建时间
                    creation_time = os.path.getctime(item_path)
                    folders.append((item, creation_time))
            
            # 按创建时间排序，取最新的20个
            folders.sort(key=lambda x: x[1], reverse=True)
            latest_folders = folders[:20]
            
            # 添加到列表
            for folder_name, _ in latest_folders:
                task_listbox.insert(tk.END, folder_name)
                
        except Exception as e:
            messagebox.showerror("错误", f"读取文件夹失败：{e}")

    def select_all():
        """全选所有任务"""
        task_listbox.selection_set(0, tk.END)

    def deselect_all():
        """取消全选"""
        task_listbox.selection_clear(0, tk.END)

    def generate_otio_gui():
        """批量生成OTIO文件"""
        path = path_entry.get()
        if not path:
            messagebox.showerror("错误", "请输入音频文件夹路径。")
            return
        
        # 获取选中的任务
        selected_indices = task_listbox.curselection()
        if not selected_indices:
            messagebox.showerror("错误", "请选择至少一个任务。")
            return
        
        selected_tasks = [task_listbox.get(i) for i in selected_indices]
        
        # 创建export文件夹
        export_dir = "export"
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)
        
        success_count = 0
        failed_tasks = []
        
        for task_name in selected_tasks:
            try:
                task_path = os.path.join(path, task_name)
                if not os.path.exists(task_path):
                    failed_tasks.append(f"{task_name} (文件夹不存在)")
                    continue
                
                # 生成输出文件名
                timestamp = datetime.now().strftime("%y%m%d_%H%M%S")
                output_filename = os.path.join(export_dir, f"{task_name}_{timestamp}")
                
                # 生成OTIO文件
                global_start_hour = 0  # 时间轴全局起始时间（小时）
                fps = 24  # 帧率
                audio_list = get_audio_clips(task_path)
                tracks = audio_to_tracks(audio_list)
                make_otio(tracks, global_start_hour, fps, output_filename)
                
                success_count += 1
                
            except Exception as e:
                failed_tasks.append(f"{task_name} ({str(e)})")
        
        # 显示结果
        if success_count > 0:
            message = f"成功导出 {success_count} 个OTIO文件到 {export_dir} 文件夹"
            if failed_tasks:
                message += f"\n\n失败的任务：\n" + "\n".join(failed_tasks)
            messagebox.showinfo("批量导出完成", message)
        else:
            messagebox.showerror("导出失败", f"所有任务都失败了：\n" + "\n".join(failed_tasks))

    gui = tk.Tk()
    gui.title("OTIO 批量生成器")
    gui.geometry("600x500")

    # 路径选择区域
    path_frame = tk.Frame(gui)
    path_frame.pack(fill=tk.X, padx=10, pady=10)
    
    tk.Label(path_frame, text="音频文件夹路径:").pack(anchor=tk.W)
    path_entry_frame = tk.Frame(path_frame)
    path_entry_frame.pack(fill=tk.X, pady=5)
    
    path_entry = tk.Entry(path_entry_frame)
    path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    browse_button = tk.Button(path_entry_frame, text="浏览", command=browse_path)
    browse_button.pack(side=tk.RIGHT, padx=(5, 0))
    refresh_button = tk.Button(path_entry_frame, text="刷新", command=refresh_task_list)
    refresh_button.pack(side=tk.RIGHT, padx=(5, 0))

    # 任务列表区域
    task_frame = tk.Frame(gui)
    task_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    tk.Label(task_frame, text="任务列表 (最新20个文件夹):").pack(anchor=tk.W)
    
    # 创建带滚动条的列表框
    list_frame = tk.Frame(task_frame)
    list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
    
    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    task_listbox = tk.Listbox(list_frame, selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set)
    task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=task_listbox.yview)

    # 选择按钮区域
    select_frame = tk.Frame(task_frame)
    select_frame.pack(fill=tk.X, pady=5)
    
    select_all_button = tk.Button(select_frame, text="全选", command=select_all)
    select_all_button.pack(side=tk.LEFT, padx=(0, 5))
    deselect_all_button = tk.Button(select_frame, text="取消全选", command=deselect_all)
    deselect_all_button.pack(side=tk.LEFT)

    # 生成按钮
    generate_button = tk.Button(gui, text="批量生成 OTIO", command=generate_otio_gui, 
                               bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
    generate_button.pack(pady=20)

    # 初始化时设置默认路径
    default_path = r"C:\TechProjects\About_Voice_Cloning\xtts_gatcha_machine\output"
    if os.path.exists(default_path):
        path_entry.insert(0, default_path)
        refresh_task_list()

    gui.mainloop()

if __name__ == "__main__":
    launch_gui() 