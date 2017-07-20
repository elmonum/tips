#docker commands

docker build イメージを作成。
docker run コンテナを作成。
docker start コンテナを起動。
docker stop コンテナを停止。
docker rm コンテナを削除。
docker rmi イメージを削除。
docker ps コンテナの確認。
boot2docker ip ホストのIPアドレス表示


MySQLコンテナ起動
docker run --name container_mysql -e MYSQL_ROOT_PASSWORD=password -d -p 3306:3306 mysql
MySQLコンテナ接続
docker exec -it container_mysql bash


CREATE TABLE test(name char(20),tell char(20));
insert into test (name, tell) values ('34,0077,77', 'a');

select * from test WHERE CONCAT(",", `name`, ",") REGEXP ",(77),";

コンテナを作成する．-dオプションでバックグラウンドで実行する．

docker run -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"
コンテナを停止する．

docker stop `dl`
コンテナを起動する．

docker start `dl`
コンテナを再起動する．

docker restart `dl`
起動中のコンテナに接続する．

docker attach `dl`
コンテナ内のファイルをホストにコピーする．

docker cp `dl`:/etc/passwd .
ホストのディレクトリをコンテナにマウントする．

docker run -v /home/vagrant/test:/root/test ubuntu echo yo
コンテナを削除する．

dockr rm `dl`

コンテナの情報
起動中のコンテナを表示する．停止中のコンテナも表示するには，-aオプション．

docker ps
コンテナの情報（IPなど）を表示する.

docker inspect `dl`
コンテナのログを表示する．

docker logs `dl`
コンテナのプロセスを表示する．

docker top `dl`
