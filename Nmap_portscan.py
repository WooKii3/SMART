import subprocess
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", required=True, type=str, help="Scan IP")
args = vars(parser.parse_args())

ip_address = args['ip']
output_file = "nmap_scan_results.txt"

# 1000개 단위로 포트를 나누어 검사
for start_port in range(0, 65536, 1000):
    end_port = start_port + 999
    if end_port > 65535:
        end_port = 65535
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Nmap 명령 구성
    nmap_command = f"nmap -sT {ip_address} -p {start_port}-{end_port}"
    print(f"실행중: {nmap_command}\n실행시간 : {current_time}")

    # Nmap 명령 실행 및 결과 저장
    result = subprocess.run(nmap_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    
    with open(output_file, "a") as file:
        file.write(f"스캔 시간 : {current_time}\n")
        file.write(result.stdout)
        file.write("\n\n")

    
    if end_port == 65535:
        break

print(f"Scan complete. Results saved to {output_file}")

