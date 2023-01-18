# Repthon - UserBot
# Copyright (C) 2021-2022 TeamRepthon
# This file is a part of < https://github.com/rogerpq/Repthon/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/rogerpq/Repthon/blob/main/LICENSE/>.

FROM thejmthon/Repthon:main

# set timezone
ENV TZ=Asia/Baghdad
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY installer.sh .

RUN bash installer.sh

# changing workdir
WORKDIR "/root/rogerpq"

# start the bot.
CMD ["bash", "startup"]
