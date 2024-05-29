def print_file_info(file_name):
    list1=[]
    try:
        with open(file_name,'r',encoding='utf-8') as f:
            list1=f.read()
            print(list1)
    except Exception as e:
        print(f'存在异常为：{e}')

def append_to_file(file_name,date):
    with open(file_name,'a',encoding='utf-8') as f:
        f.write(date)
        f.write('\n')


if __name__=='__main__':
    print_file_info('my_package\\1.txt')
    append_to_file('my_package\\text.txt','gajkawghKFHlk')