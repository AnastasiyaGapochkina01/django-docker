блог DjangoGirls в докере 

#### GitlabCI
* Билдит образ, если в мастере изменился Dockerfile или код; пушит в docker-hub
* Прогоняет тесты, если был билд
* Деплоит, если два предыдущих шага успешны и ветка - мастер

#### Jenkinsfile:

* На вход принимает ветку, из которой билдится образ
* Апдейтит локальный реп
* Если изменился Dockerfile или код билдит с тегом <имя ветки-хэш коммита> и пушит на docker-hub (ставится переменная skip_next_step для определения, нужно ли выполнять следующие stage)
* Прогоняет тесты (docker-compose запускается с --env-file, который генерится на предыдущем шаге); стопает и удаляет за собой контейнеры
* Деплоит на prod/staging в зависимости от ветки

### ToDo
* прикрутить линтер на Dockerfile и на yml (docker-compose)
* добавить возможность Rollback
