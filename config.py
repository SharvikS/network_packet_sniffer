# SETTINGS
# interface        "wlan0"             network card to sniff
# packet_count     100                 stop after this many packets (0 = no limit)
# capture_timeout  90                  stop after this many seconds
# bpf_filter       ""                  optional filter, empty = capture everything
# db_path          "data/traffic.db"   where the database file goes
# batch_size       50                  save packets in groups of this size
# log_level        "INFO"              DEBUG / INFO / WARNING / ERROR
# log_file         "logs/sniffer.log"  where logs are written

from dataclasses import dataclass


@dataclass
class Config:
    interface: str = "wlan0"
    packet_count: int = 100
    capture_timeout: int = 90
    bpf_filter: str = ""
    db_path: str = "/home/tatya/Projects/network_packet_sniffer/db"
    batch_size: int = 50
    log_level: str = "INFO"
    logs: str = "/home/tatya/Projects/network_packet_sniffer/logs"


if __name__ == "__main__":
    network = Config()
    print(network)
