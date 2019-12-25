from scapy.all import *
from scapy.layers.inet import TCP, IP
from IP_Obj import IPGroup
import glob
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.font_manager import FontProperties
import imgkit

def aggregate_ssh(filename):
    packets = rdpcap(filename)
    aggregation_map_packet_size = {}
    aggregation_map_packet_count = {}
    aggregation_map_count_port_number = {}
    for packet in packets:
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            if TCP in packet:
                tcp_dport = packet[TCP].dport
                tcp_sport = packet[TCP].sport
                # if tcp_dport == 22 or tcp_sport == 22:
                map_key = ip_src + "-"+ip_dst
                if map_key in aggregation_map_packet_size:
                    aggregation_map_packet_size[map_key] = aggregation_map_packet_size.get(map_key) + len(packet)
                    aggregation_map_packet_count[map_key] = aggregation_map_packet_count.get(map_key) + 1
                    aggregation_map_count_port_number[map_key].append(tcp_dport)
                else:
                    temp_list = [tcp_dport]
                    aggregation_map_count_port_number[map_key] = temp_list
                    aggregation_map_packet_size[map_key] = len(packet)
                    aggregation_map_packet_count[map_key] = 1

    for key in aggregation_map_count_port_number:
        aggregation_map_count_port_number[key] = len(set(aggregation_map_count_port_number[key]))

    # todo: add a error checking for map size
    ip_pair_group_list = []
    for key in aggregation_map_packet_count:
        ip_pair_group_item = IPGroup(key, aggregation_map_packet_count[key], aggregation_map_packet_size[key], aggregation_map_count_port_number[key])
        ip_pair_group_list.append(ip_pair_group_item)
    # map is for calculation packet number
    return ip_pair_group_list

def make_table(file_list):
    avgPacketSize_main_map = {}
    avgPacketCountPerProcess_main_map = {}
    # file_list = glob.glob("/Users/PycharmProjects/brute-force-detection/pcap_file*.pcap")
    # file_list = os.listdir("pcap_file")
    for file in file_list:
        ipgroup_object_list = aggregate_ssh(file)
        for ipgroup_object in ipgroup_object_list:
            tempkey = ipgroup_object.groupname
            if tempkey in avgPacketCountPerProcess_main_map:
                avgPacketSize_main_map[tempkey].append(ipgroup_object.averagePacketSize)
                avgPacketCountPerProcess_main_map[tempkey].append(ipgroup_object.averagePacketCountPerProcess)
            else:
                templistPacketSizeList = [ipgroup_object.averagePacketSize]
                templistPacketCountPerProcessList = [ipgroup_object.averagePacketCountPerProcess]

                avgPacketSize_main_map[tempkey] = templistPacketSizeList
                avgPacketCountPerProcess_main_map[tempkey] = templistPacketCountPerProcessList

    map2csv(avgPacketSize_main_map, "avgPacketSize.csv")
    map2csv(avgPacketCountPerProcess_main_map, "avgPacketSizePerProcess.csv")
    drawGraph(avgPacketSize_main_map, "avgPacketSize.png")
    drawGraph(avgPacketCountPerProcess_main_map, "avgPacketSizePerProcess.png")
    drawTable("avgPacketSize.csv")
    drawTable("avgPacketSizePerProcess.csv")
    # return avgPacketSize_main_map, avgPacketCountPerProcess_main_map

def drawTable(filename):
    data_origninal = pd.read_csv(filename, sep='\n', header=None)
    data_table = data_origninal[0].str.split(',', expand=True)
    data_numeric = data_table.apply(pd.to_numeric, errors='ignore')
    data_numeric.fillna(value=pd.np.nan, inplace=True)
    # data_numeric.replace(r'^\s*$', np.nan, regex=True)
    # data_numeric.replace(' ', np.nan, regex=False)
    std_column = data_numeric.std(axis=1, ddof=0, numeric_only=True, skipna=True)
    data_final = data_numeric.assign(Standard_Deveation=std_column)
    data_final_sorted = data_final.sort_values(by=["Standard_Deveation"], ascending=False)

    # render dataframe as html
    html = data_final_sorted.to_html()

    # write html to file
    html_filename = filename.replace('.csv', '.html')
    text_file = open(html_filename, "w")
    text_file.write(html)
    text_file.close()

def map2csv(ip_group_map, filename):
    with open(filename, 'w') as the_file:
        for key in ip_group_map:
            content = key + ','
            for item in ip_group_map[key]:
                content += str(item) + ','
            the_file.write(content + "\n")

def drawGraph(main_map, png_filename):
    fontP = FontProperties()
    fontP.set_size('small')
    for key in main_map:
        y = main_map[key]
        # if data point lower than 10
        if len(y) < 10:
            continue
        x = list(range(0, len(y)*10, 10))

        plt.plot(x, y, label = key, markersize=12)
    # plt.xlabel('ippair name')
    plt.xticks([])
    plt.legend(loc = 'center left', bbox_to_anchor=(1,0.5))
    plt.title(png_filename)
    # plt.show()

    fig = plt.gcf()
    fig.set_size_inches(15, 5)
    fig.savefig(png_filename, dpi=50, bbox_inches='tight')
    fig.savefig("high_dpi_"+png_filename, dpi=100, bbox_inches='tight')
