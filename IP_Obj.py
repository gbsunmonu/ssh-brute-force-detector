class IPGroup():
    def __init__(self, key, packet_count, total_packet_size, process_number):
        self.packet_count = packet_count
        self.total_packet_size = total_packet_size
        self.process_number = process_number
        self.groupname = key

    @property
    def averagePacketSize(self):
        return self.total_packet_size / self.packet_count
    @property
    def averagePacketCountPerProcess(self):
        return self.packet_count / self.process_number