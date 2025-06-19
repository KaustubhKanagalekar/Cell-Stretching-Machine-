import matplotlib.pyplot as plt
import pandas as pd  
'''
#loading all data (change path to match true path )
load_1_data = pd.read_csv('/Users/kaustubhkanagalekar/Downloads/load1.csv',names=['Value', 'Time'], sep=r'\t+', engine='python')
load_2_data = pd.read_csv('/Users/kaustubhkanagalekar/Downloads/load2.csv',names=['Value', 'Time'], sep=r'\t+', engine='python')
load_3_data = pd.read_csv('/Users/kaustubhkanagalekar/Downloads/load3.csv', names=['Value', 'Time'], sep=r'\t+', engine='python')

#############################################
#load data 1 
with open('/Users/kaustubhkanagalekar/Downloads/load1.csv', 'r') as f:
    raw_lines = [line.strip().replace(',', '') for line in f if line.strip()]

# Step 2: Separate even and odd rows
values_raw = raw_lines[::2]   # 0, 2, 4... → values
times_raw = raw_lines[1::2]   # 1, 3, 5... → times

# Step 3: Construct the cleaned DataFrame
df1 = pd.DataFrame({
    'Value': pd.to_numeric(values_raw, errors='coerce'),
    'Time': pd.to_datetime(times_raw, format='%I:%M:%S %p', errors='coerce')
})

# Drop any rows that failed to parse
df1 = df1.dropna().reset_index(drop=True)

df1['Elapsed_s'] = (df1['Time'] - df1['Time'].iloc[0]).dt.total_seconds()

# Or seconds
df1['Elapsed_s'] = df1['Elapsed_s'] 

print(df1[['Value', 'Elapsed_s']])

df1['Value_N'] = df1['Value'] * 4.44822

plt.figure(figsize=(10, 5))
plt.plot(df1['Elapsed_s'], df1['Value_N'], marker='o', linestyle='-')
plt.xlabel('Time (s)')
plt.ylabel('Load (N)')
plt.title('Test Involving 10mm sample, strain of 30% 10Hz')
plt.grid(True)
plt.tight_layout()
plt.show()

#################################################

#load data 2 
with open('/Users/kaustubhkanagalekar/Downloads/load2.csv', 'r') as f:
    raw_lines = [line.strip().replace(',', '') for line in f if line.strip()]

# Step 2: Separate even and odd rows
values_raw = raw_lines[::2]   # 0, 2, 4... → values
times_raw = raw_lines[1::2]   # 1, 3, 5... → times

# Step 3: Construct the cleaned DataFrame
df2 = pd.DataFrame({
    'Value': pd.to_numeric(values_raw, errors='coerce'),
    'Time': pd.to_datetime(times_raw, format='%I:%M:%S %p', errors='coerce')
})

# Drop any rows that failed to parse
df2 = df2.dropna().reset_index(drop=True)

df2['Elapsed_s'] = (df2['Time'] - df2['Time'].iloc[0]).dt.total_seconds()

# Or seconds
df2['Elapsed_s'] = df2['Elapsed_s'] 

print(df2[['Value', 'Elapsed_s']])
plt.figure(figsize=(10, 5))
plt.plot(df2['Elapsed_s'], df2['Value'], marker='o', linestyle='-')
plt.xlabel('Time (s)')
plt.ylabel('Load (N)')
plt.title('Test Involving 20mm sample, strain of 25%, 2 Hz ')
plt.grid(True)
plt.tight_layout()
plt.show()


###################################################
#Load data 3 
with open('/Users/kaustubhkanagalekar/Downloads/load3.csv', 'r') as f:
    raw_lines = [line.strip().replace(',', '') for line in f if line.strip()]

# Step 2: Separate even and odd rows
values_raw = raw_lines[::2]   # 0, 2, 4... → values
times_raw = raw_lines[1::2]   # 1, 3, 5... → times

# Step 3: Construct the cleaned DataFrame
df3 = pd.DataFrame({
    'Value': pd.to_numeric(values_raw, errors='coerce'),
    'Time': pd.to_datetime(times_raw, format='%I:%M:%S %p', errors='coerce')
})

# Drop any rows that failed to parse
df3 = df3.dropna().reset_index(drop=True)

df3['Elapsed_s'] = (df3['Time'] - df3['Time'].iloc[0]).dt.total_seconds()

# Or seconds
df3['Elapsed_s'] = df3['Elapsed_s'] 

print(df3[['Value', 'Elapsed_s']])
plt.figure(figsize=(10, 5))
plt.plot(df3['Elapsed_s'], df3['Value'], marker='o', linestyle='-')
plt.xlabel('Time (s)')
plt.ylabel('Load (N)')
plt.title('Test Involving No Load, 10 Hz ')
plt.grid(True)
plt.tight_layout()
plt.show()

'''
#################################
load_4_data = pd.read_csv('/Users/kaustubhkanagalekar/Downloads/loadmay20000smacpower20000.csv',names=['Value', 'Time'], sep=r'\t+', engine='python')

#Load data 3 
with open('/Users/kaustubhkanagalekar/Downloads/loadmay20000smacpower20000.csv', 'r') as f:
    raw_lines = [line.strip().replace(',', '') for line in f if line.strip()]

# Step 2: Separate even and odd rows
values_raw = raw_lines[::2]   # 0, 2, 4... → values
times_raw = raw_lines[1::2]   # 1, 3, 5... → times

# Step 3: Construct the cleaned DataFrame
df3 = pd.DataFrame({
    'Value': pd.to_numeric(values_raw, errors='coerce'),
    'Time': pd.to_datetime(times_raw, format='%I:%M:%S %p', errors='coerce')
})

# Drop any rows that failed to parse
df3 = df3.dropna().reset_index(drop=True)

df3['Elapsed_s'] = (df3['Time'] - df3['Time'].iloc[0]).dt.total_seconds()

# Or seconds
df3['Elapsed_s'] = df3['Elapsed_s'] 

print(df3[['Value', 'Elapsed_s']])
plt.figure(figsize=(10, 5))
plt.plot(df3['Elapsed_s'], df3['Value'], marker='o', linestyle='-')
plt.xlabel('Time (s)')
plt.ylabel('Load (N)')
plt.title('Test Involving Load from String, 0.2 Hz ')
plt.grid(True)
plt.tight_layout()
plt.show()