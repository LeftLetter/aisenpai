FROM python:3.7

WORKDIR /workspace
RUN pip install poetry
RUN poetry config virtualenvs.create false
# RUN pip install ginza
# COPY poetry.lock /workspace
# COPY pyproject.toml /workspace
# RUN poetry install


# ENV DEBIAN_FRONTEND=noninteractive
# ARG project_dir=/workspace/
# WORKDIR $project_dir

# RUN apt update
# RUN apt install -y wget build-essential libboost-all-dev
# RUN apt install sudo

# # install mecab
# RUN apt install mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file -y
# # install neologd
# RUN git clone https://github.com/neologd/mecab-ipadic-neologd.git
# WORKDIR $project_dir/mecab-ipadic-neologd
# RUN ./bin/install-mecab-ipadic-neologd -n -a -y

# # install cmake
# RUN apt install cmake -y

# # install juman
# WORKDIR $project_dir
# RUN wget http://lotus.kuee.kyoto-u.ac.jp/nl-resource/jumanpp/jumanpp-1.02.tar.xz
# RUN tar Jxf jumanpp-1.02.tar.xz
# RUN cd jumanpp-1.02 && ./configure && make && make install

# # move BERT model to appropriate directory
# #ai_senpai_apiserver/modules/sentence_embedding

# # move qiita json to appropriate directory
# #ai_senpai_apiserver/modules/sentence_embedding

# # COPY ./.devcontainer/requirements.txt.temp ./requirements.txt* $project_dir
# # RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt && rm requirements.txt*; fi

# WORKDIR $project_dir
# RUN rm -rf $project_dir

# ENV DEBIAN_FRONTEND=dialog
