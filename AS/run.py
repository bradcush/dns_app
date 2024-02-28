import socket

HOST = ""
PORT = 53533


# Check if the request is a registration
def is_registration(request):
    decoded = request.decode()
    return (
        "TYPE=A" in decoded
        and "NAME=" in decoded
        and "VALUE=" in decoded
        and "TTL=" in decoded
    )


# Check if the request is a query
def is_query(request):
    decoded = request.decode()
    return (
        "TYPE=A" in decoded
        and "NAME=" in decoded
        and "VALUE=" not in decoded
        and "TTL=" not in decoded
    )


# Start a socket server that
# accepts DNS requests over UDP
def start():
    print("Starting DNS server...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    while True:
        request, address = sock.recvfrom(2048)
        request = request.upper()
        print(f"Received {request} from {address}")
        if is_registration(request):
            # Store the record in a file database where we
            # only support storing one record at a time
            file = open("record.txt", "w", encoding="utf-8")
            file.write(request.decode())
            file.close()
            response = "SUCCESS"
            sock.sendto(response.encode(), address)
        elif is_query(request):
            # Retrieve record from file database
            # response = "TYPE=A\nNAME=fibonacci.com\nVALUE=0.0.0.0\nTTL=10"
            file = open("record.txt", "r", encoding="utf-8")
            response = file.read()
            if response == "":
                response = "FAILURE"
            file.close()
            sock.sendto(response.encode(), address)
        else:
            response = "FAILURE"
            sock.sendto(response.encode(), address)


start()
