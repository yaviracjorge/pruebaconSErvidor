deployconip:
	@ docker run -d --name appflask -p 7000:5000 ghcr.io/yaviracjorge/holaflask


#para hacer stacks#
deploy:
	@ docker stack deploy --with-registry-auth -c stack.yml jcorella

#para crear redes#
network:
	@ docker network create --driver overlay --scope swarn jcorella_net || true

#crear un volumen#
volume:
	@ docker volume create v_jcorella


