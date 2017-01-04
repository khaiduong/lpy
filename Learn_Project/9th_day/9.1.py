'''
Viết chương trình in ra 10 dòng cuối cùng của một file (có khả năng xử lý
file có kích thước bất kỳ, ví dụ > 10GB).
Yêu cầu không dùng quá 100 MB bộ nhớ trong (RAM) khi chạy chương trình.
Gợi ý:
- Không dùng method file.readlines()
'''

import argparse
import os
'''
def parse_args():
    parser = argparse.ArgumentParser(description="Takes servers temporarily offline and applies updates")
    parser.add_argument("master_host", action="store", type=str, default="reader",
                        help="The host will become master one")
    parser.add_argument("slave_hosts", type=str, nargs='+',
                    help="Two hosts will become master's slaves")
    parser.add_argument("--nfs-setup", dest="nfs-setup", action="store_true",
                    help="Install DTX system with nfs file server")
    parser.add_argument("--gpfs-setup", dest="nfs-setup", action="store_true",
                    help="Install DTX system with gpfs file server")
    return parser.parse_args()
    #master = args.master_host
    #slaves = args.slave_hosts
    #print("Master is: {master_host} and its slaves are: {slave_hosts}".format(master_host = master, slave_hosts = slaves))
    #print(type(slaves))
    #print()

if __name__ == "__main__":
    args = parse_args()
    master = args.master_host
    slaves = args.slave_hosts
    print('master is: {master}'.format(master = master))
    print('slaves are: {slaves}'.format(slaves = slaves))
    '''
print(os.path.abspath('.'))
slaves = ['ld7186', 'ld2821']

with open('C:/Users/i324011/.ssh/known_hosts') as f1:
    know_host = f1.readlines()
    slave_key = [key for key in know_host if any(txt in key for txt in slaves)]
    print(slave_key)

slaves = ['ld1111', 'ld2222']
with open('C:/Users/i324011/Desktop/config-tmp', 'w') as f:
    f.write('Host {slave1} {slave2}\n\tStrictHostKeyChecking no'.format(slave1 = slaves[0], slave2 = slaves[1]))
    return os.path.abspath(filename)