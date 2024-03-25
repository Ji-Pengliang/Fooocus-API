from gradio_client import Client

client = Client("http://127.0.0.1:7865/")
result = client.predict(
				fn_index=43
)
print(result)