from scapy.all import *
import os
from collections import defaultdict
import time

# Dictionnaire pour suivre le nombre de paquets par adresse IP
packet_count = defaultdict(int)
first_seen = {}

# Seuil de bannissement
THRESHOLD = 100

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        
        # Incrémente le compteur de paquets pour cette IP
        packet_count[src_ip] += 1
        
        # Enregistre le temps de la première requête
        if src_ip not in first_seen:
            first_seen[src_ip] = time.time()
        
        # Vérifie combien de temps s'est écoulé depuis la première requête
        elapsed_time = time.time() - first_seen[src_ip]
        
        # Si l'IP dépasse le seuil dans un temps réduit
        if elapsed_time < 1:  # Vérifie si les paquets arrivent dans la dernière seconde
            if packet_count[src_ip] > THRESHOLD:
                print(f"Bannir l'adresse IP: {src_ip} (plus de {THRESHOLD} requêtes en 1 seconde)")
                os.system(f"iptables -A INPUT -s {src_ip} -j DROP")  # Bloque l'adresse IP
                # Réinitialiser le compteur et l'heure
                reset_ip(src_ip)
        
        # Si plus d'une seconde s'est écoulée, réinitialiser le compteur
        if elapsed_time > 1:
            reset_ip(src_ip)

def reset_ip(src_ip):
    packet_count.pop(src_ip, None)
    first_seen.pop(src_ip, None)

# Capture des paquets (affichage en temps réel)
sniff(prn=packet_callback, filter="ip", store=0)
