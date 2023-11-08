all: webhook server

webhook:
	@pm2 start webhook.py --name webhooks --interpreter python3

server:
	@pm2 start ../lab-socket-programming2/tcp-server.py --name tcp-receiver --interpreter python3 --watch

clean:
	pm2 stop all
	pm2 delete all
