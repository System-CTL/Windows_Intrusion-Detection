import os 
import csv
from csv import writer
import subprocess



path_to_script = os.path.dirname(os.path.abspath(__file__))
net_process_txt = os.path.join(path_to_script, "net_Processed.txt")
nbt_process_txt = os.path.join(path_to_script, "nbt_Processed.txt")
net_start_process_txt = os.path.join(path_to_script, "net_start_Processes.txt")

net_stat = subprocess.check_output("Netstat -aon", shell=True)
print("-----------------------------------------RESPONSE------------------------------------------")
net_new_var=net_stat.decode('utf-8').split('\r\n\r\n', 1)[1]

#files operation
with open(net_process_txt, 'w') as var:
    lines=var.write(net_new_var)

with open(net_process_txt, 'rt') as var:
    con_sline=[]
    lines=var.readlines()
    
    for line in lines:
        
        sline=line.strip().split(None, 8) 
        con_sline.append(sline)
        #print(sline)        
    #sline.append(line.strip().split(None, 8))

#delete first column
del con_sline[0]

path_to_script = os.path.dirname(os.path.abspath(__file__))
my_filename = os.path.join(path_to_script, "windows_intru.csv")
fields=['Netstat Output']

sub_fields=["Proto","Local Address","Foreign Address","State","PID"]




#net start data for unsual process 


net_start = subprocess.check_output("net start", shell=True)
net_start_var=net_start.decode('utf-8').split('\r\n\r\n', 1)[1]
#print(net_start_var)

with open(net_start_process_txt, 'w') as net_var:
    net_var.write(net_start_var)

f1=open(net_start_process_txt,'rt', encoding='latin1')
input=f1.read()
input=input.replace(' ','_')
f2=open(net_start_process_txt,'w', encoding='latin1')
f2.write(input)
f2.close()


with open(net_start_process_txt, 'rt') as net_var_secnd:
    net_start_array=[]
    lines=net_var_secnd.readlines()
    for line in lines: 
        sline=line.strip().split(None, 8)
        net_start_array.append(sline)

        #sline=line.strip().split(None, 8) 





#nbtstat data 

nbt_stat = subprocess.check_output("nbtstat -S", shell=True)
nbt_new_var=nbt_stat.decode('utf-8').split('\r\n\r\n', 1)[1]

with open(nbt_process_txt, 'w') as nbt_var:
    lines=nbt_var.write(nbt_new_var)

with open(nbt_process_txt, 'rt') as nbt_var:
    con_sline_nbt=[]
    lines=nbt_var.readlines()
    
    for line in lines:
        sline=line.strip().split(None, 8) 
        con_sline_nbt.append(sline)





with open(my_filename, mode='w',encoding="ISO-8859-1",newline='') as csv_file:
    file_writer = writer(csv_file,dialect='excel')
    file_writer.writerow(fields)
    file_writer.writerow([sub_fields])


with open(my_filename, mode='a+',encoding="ISO-8859-1",newline='') as csv_file:
    file_writer = writer(csv_file,dialect='excel')
    for c in range(len(con_sline)):
        file_writer.writerow([con_sline[c]])
    for c in range(len(con_sline_nbt)):
        file_writer.writerow(con_sline_nbt[c])
    file_writer.writerow(" "+" "+" "+"-------------------------"+"------------------------------"+"-------------------------")
    file_writer.writerow(" "+" "+" "+"NET START OUTPUT")
    file_writer.writerow(" "+" "+" "+"-------------------------"+"------------------------------"+"-------------------------")
    file_writer.writerow([["Net Start Outpot - Looking for unsuall processes"]])
    file_writer.writerow(" ")
    for c in range(len(net_start_array)):
        file_writer.writerow(net_start_array[c])
    
