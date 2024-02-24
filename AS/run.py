import socket

HOST = ""
PORT = 53533


# Check if the request is a registration
def is_registration(request):
    decoded = request.decode("utf-8")
    return (
        "TYPE=A" in decoded
        and "NAME=" in decoded
        and "VALUE=" in decoded
        and "TTL=" in decoded
    )


# Check if the request is a query
def is_query(request):
    decoded = request.decode("utf-8")
    return (
        "TYPE=A" in decoded
        and "NAME=" in decoded
        and "VALUE=" not in decoded
        and "TTL=" not in decoded
    )


# Start a socket server that
# accepts DNS requests over UDP
def start():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    while True:
        request, address = sock.recvfrom(1024)
        request = request.upper()
        print(f"Received {request} from {address}")
        if is_registration(request):
            # Record should be stored in a database
            file = open("record.txt", "w", encoding="utf-8")
            file.write(request.decode("utf-8"))
            file.close()
            response = "SUCCESS"
            sock.sendto(bytes(response, "utf-8"), address)
        elif is_query(request):
            # This should be retrieved from a database
            file = open("record.txt", "r", encoding="utf-8")
            # response = "TYPE=A\nNAME=fibonacci.com\nVALUE=0.0.0.0\nTTL=10"
            response = file.read()
            if response == "":
                response = "FAILURE"
            file.close()
            sock.sendto(bytes(response, "utf-8"), address)
        else:
            response = "FAILURE"
            sock.sendto(bytes(response, "utf-8"), address)


start()
