import pandas as pd
import numpy as np

df = pd.read_csv(
    "data/Data/Friday-WorkingHours-Afternoon-DDoS.pcap_ISCX.csv"
)

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("/", "_")
)

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

df["is_attack"] = df["label"].apply(
    lambda x: 0 if x == "BENIGN" else 1
)

features = [
    "destination_port",
    "flow_duration",
    "total_fwd_packets",
    "total_backward_packets",
    "total_length_of_fwd_packets",
    "total_length_of_bwd_packets",
    "fwd_packet_length_mean",
    "bwd_packet_length_mean",
    "packet_length_mean",
    "packet_length_variance",
]

available_features = [f for f in features if f in df.columns]
final_df = df[available_features + ["is_attack"]]
