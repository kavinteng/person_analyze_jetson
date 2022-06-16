from module import *

def run_config():
    rtsp_split = rtsp_source.split('/', 4)
    root = Tk()
    root.title('Edit_polygon')
    root.geometry('250x300+0+0')

    host_name = Label(root, text=rtsp_split[2], fg='green', font=('Arial', 10))
    host_name.pack(padx=5, pady=5)

    ch1 = Button(root, text="CH1", width=20, bg='red', fg='white', command=lambda
        cam=rtsp_url1: set_polycon_tk(cam))
    ch1.pack(padx=5, pady=5)
    ch2 = Button(root, text="CH2", width=20, bg='red', fg='white', command=lambda
        cam=rtsp_url2: set_polycon_tk(cam))
    ch2.pack(padx=5, pady=5)
    ch3 = Button(root, text="CH3", width=20, bg='red', fg='white', command=lambda
        cam=rtsp_url3: set_polycon_tk(cam))
    ch3.pack(padx=5, pady=5)
    ch4 = Button(root, text="CH4", width=20, bg='red', fg='white', command=lambda
        cam=rtsp_url4: set_polycon_tk(cam))
    ch4.pack(padx=5, pady=5)

    # root.attributes('-topmost', True)

    root.mainloop()

def confirm_yesno(message = 'ยืนยันที่จะปิดโปรแกรมหรือไม่'):
    if messagebox.askyesno(title='confirmation',message=message):
        root.destroy()
        sys.exit(1)

def run_app():
    cam_threading(rtsp_source + rtsp_url1, 1)
    cam_threading(rtsp_source + rtsp_url2, 2)
    cam_threading(rtsp_source + rtsp_url3, 3)
    cam_threading(rtsp_source + rtsp_url4, 4)

if __name__ == '__main__':
    write_nvr()
    rtsp_source = read_nvr(1)

    rtsp_url1 = 'av0_0'
    rtsp_url2 = 'av0_1'
    rtsp_url3 = 'av0_2'
    rtsp_url4 = 'av0_3'
    if os.path.isfile('logfile.db') == False:
        create_logfile()
    load_all_model()
    get_image_threading()
    root = Tk()
    root.title('Application Controller')
    root.geometry('250x300+0+0')

    start_app = Button(root, text="START", width=20, bg='red', fg='white', command=run_app)
    start_app.pack(padx=5, pady=5)
    start_app = Button(root, text="Edit_polygon", width=20, bg='red', fg='white', command=run_config)
    start_app.pack(padx=5, pady=5)

    admin = Button(root, text="ADMIN", width=20, bg='red', fg='white', command=admin_control)
    admin.pack(padx=5, pady=5, side="bottom")

    root.protocol('WM_DELETE_WINDOW', confirm_yesno)
    # root.attributes('-topmost', True)

    root.mainloop()