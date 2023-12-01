import base64
file_path = input("Nhập đường dẫn tới file ps: ")

with open(file_path, "r") as file:
    content = file.read()

bat = "powershell -executionpolicy bypass -WindowStyle hidden -e "
encoded_content = base64.b64encode(content.encode("utf-16")[2:]).decode()
bat = bat + encoded_content
print(bat)

with open("output.bat", "w") as file:
    file.write(bat)