from kafka import KafkaConsumer

consumer = KafkaConsumer('order_details', bootstrap_servers='localhost:29092')

print("Started listening")
i=1
while True:
    for message in consumer:
        print("Recieved: {}".format(i))
        print (message)
        i=i+1