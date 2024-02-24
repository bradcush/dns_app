import requests
import socket
from flask import Flask
from flask import request

app = Flask(__name__)


# Get the ip address of the hostname
# from an authoritative name server
def get_ip_address(hostname, as_ip, as_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    request = f"TYPE=A\nNAME={hostname}"
    sock.sendto(bytes(request, "utf-8"), (as_ip, as_port))

    try:
        response = sock.recvfrom(1024)
        print(f"Received {response}")
        # Parse the IP address from response in expected location
        return response[0].decode("utf-8").split("\n")[2].split("=")[1]
    except socket.timeout:
        print("An error occurred")
    # Understand how to deal with closing
    # sockets on the client and server


@app.route("/fibonacci")
def fibonacci():
    args = request.args
    hostname = args.get("hostname")
    fs_port = args.get("fs_port")
    number = args.get("number")
    as_ip = args.get("as_ip")
    as_port = args.get("as_port")

    if not (hostname) or not (fs_port) or not (number) or not (as_ip) or not (as_port):
        return "Bad Request", 400

    ip_address = get_ip_address(hostname, as_ip, int(as_port))
    return requests.get(
        f"http://{ip_address}:{fs_port}/fibonacci?number={number}"
    ).content


app.run(host="0.0.0.0", port=8080, debug=True)
