
# Relatório da saúde do modelo
## Índice
 - [Overview](#overview)
 - [Configurações](#config)
 - [Intenções](#intention)
 - [Entidades](#entity)
 - [NLU](#nlu)
 - [Respostas](#response)

[Voltar para o início](../../index.md)

## Overview <a name='overview'></a>
|Bot|Versão|Rasa|Data de criação|Data de atualização|Modelo|
|:-:|:-:|:-:|:-:|:-:|:-:|
|<span style='font-size:16px'>**teste**</span>|            <span style='font-size:16px'>not identified</span>|            <span style='font-size:16px'>0.0.0</span>|            <span style='font-size:16px'>11/11/22 23:16:33</span>|            <span style='font-size:16px'>12/11/22 00:33:06</span>|            [Link](https://ps-nightcity-bucket.s3.amazonaws.com/models/teste/teste-vNone.tar.gz)|

|Intenção|Entidade|NLU|Resposta|<span style='font-size:20px'>Geral</span>|
|:-:|:-:|:-:|:-:|:-:|
|0            |0            |0            |10            |<span style='font-size:20px'>**10**</span>|
❌            |❌            |❌            |🟢            |<span style='font-size:20px'>🟢</span>|

## Configurações <a name='config'></a>
Configurações que foram utilizadas na *pipeline* de treinamento e nas *policies*.
```yaml
recipe: default.v1
language: pt
pipeline:
- name: WhitespaceTokenizer
- name: RegexFeaturizer
  case_sensitive: false
- name: LexicalSyntacticFeaturizer
- name: CountVectorsFeaturizer
  analyzer: word
  lowercase: true
  strip_accents: unicode
- name: CountVectorsFeaturizer
  analyzer: char_wb
  lowercase: true
  max_ngram: 5
  min_ngram: 2
  strip_accents: unicode
- name: DIETClassifier
  epochs: 20
  tensorboard_log_directory: ".tensorboard_diet"
  tensorboard_log_level: "epoch"
  constrain_similarities: true
- name: EntitySynonymMapper
- name: ResponseSelector
  epochs: 20
  constrain_similarities: true
- name: FallbackClassifier
  ambiguity_threshold: 0.05
  threshold: 0.8
policies:
- name: TEDPolicy
  epochs: 20
  max_history: 5
  tensorboard_log_directory: ".tensorboard_ted"
  tensorboard_log_level: "epoch"
  constrain_similarities: true
- name: RulePolicy
  core_fallback_action_name: action_default_fallback
  core_fallback_threshold: 0.5
  enable_fallback_prediction: true
- name: AugmentedMemoizationPolicy
  max_history: 5
  tensorboard_log_directory: ".tensorboard_memo"
  tensorboard_log_level: "epoch"

```

## Intenções <a name='intention'></a>
Seção que aborda métricas sobre as intenções do modelo.

### Métricas
Tabela com as métricas das intenções.

Não foram encontradas intenções nesse modelo.

### Intenções confusas
Aqui vão constar todas as frases confusas ou erradas do modelo.

Não foram encontradas confusões ou erros de intenções nesse modelo.

## Entidades <a name='entity'></a>
Seção que aborda métricas sobre as entidades do modelo.

### Métricas
Tabela com as métricas das entidades.


Não foram encontradas entidades nesse modelo.

### Entidades confusas
Aqui vão constar todas as entidades confusas ou erradas do modelo.

Não foram encontradas confusões ou erros de intenções nesse modelo.

## Respostas <a name='response'></a>
Seção que aborda métricas sobre as respostas e histórias do bot.

### Métricas
Tabela com as métricas das respostas do bot.

||Resposta|Precisão|Recall|F1 Score|Número de ocorrências|
|-|-|-|-|-|-|
|🟢|utter_explica_video|100.0%|100.0%|100.0%|7|
|🟢|action_link_ajuda|100.0%|100.0%|100.0%|7|
|🟢|action_bot_info|100.0%|100.0%|100.0%|1|
|🟢|action_listen|100.0%|100.0%|100.0%|11|
|🟢|action_transbordo|100.0%|100.0%|100.0%|1|
|🟢|action_finalizar_transbordo|100.0%|100.0%|100.0%|2|
|🟢|utter_finalizacao|100.0%|100.0%|100.0%|2|
### Matriz de Confusão
![Matriz de Confusão](story_confusion_matrix.png 'Teste')
