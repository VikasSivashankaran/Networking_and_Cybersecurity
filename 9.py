from scapy.all import rdpcap

# Load the capture file
packets = rdpcap('capture.pcap')

# Dictionary to hold the frequency of IP addresses
ip_counts = {}

# Loop through each packet
for packet in packets:
    if packet.haslayer('IP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst

        # Count occurrences of each IP
        if src_ip in ip_counts:
            ip_counts[src_ip] += 1
        else:
            ip_counts[src_ip] = 1

        if dst_ip in ip_counts:
            ip_counts[dst_ip] += 1
        else:
            ip_counts[dst_ip] = 1

# Sort and display top 5 IP addresses
top_ips = sorted(ip_counts.items(), key=lambda item: item[1], reverse=True)[:5]
print("Top 5 IP addresses:")
for ip, count in top_ips:
    print(f"{ip}: {count} packets")
