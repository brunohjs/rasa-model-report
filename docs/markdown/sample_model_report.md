
# Model health report
## Index
 - [Overview](#overview)
 - [Config](#configs)
 - [Intents](#intents)
 - [Entities](#entities)
 - [NLU](#nlu)
 - [Responses](#responses)


## Overview <a name='overview'></a>
|Bot|Version|Creation date|Updated date|
|:-:|:-:|:-:|:-:|
|<span style='font-size:16px'>**My Project**</span>|            <span style='font-size:16px'>not identified</span>|            <span style='font-size:16px'>10/12/22 20:59:20</span>|            <span style='font-size:16px'>10/12/22 20:59:20</span>|

|Intent|Entity|NLU|Response|<span style='font-size:20px'>General</span>|
|:-:|:-:|:-:|:-:|:-:|
|10            |0            |10            |10            |<span style='font-size:20px'>**10**</span>|
🟢            |❌            |🟢            |🟢            |<span style='font-size:20px'>🟢</span>|

## Configs <a name='configs'></a>
Settings that were used in the training *pipeline* and *policies*.
```yaml
# The config recipe.
# https://rasa.com/docs/rasa/model-configuration/
recipe: default.v1

# Configuration for Rasa NLU.
# https://rasa.com/docs/rasa/nlu/components/
language: en

pipeline:
# # No configuration for the NLU pipeline was provided. The following default pipeline was used to train your model.
# # If you'd like to customize it, uncomment and adjust the pipeline.
# # See https://rasa.com/docs/rasa/tuning-your-model for more information.
#   - name: WhitespaceTokenizer
#   - name: RegexFeaturizer
#   - name: LexicalSyntacticFeaturizer
#   - name: CountVectorsFeaturizer
#   - name: CountVectorsFeaturizer
#     analyzer: char_wb
#     min_ngram: 1
#     max_ngram: 4
#   - name: DIETClassifier
#     epochs: 100
#     constrain_similarities: true
#   - name: EntitySynonymMapper
#   - name: ResponseSelector
#     epochs: 100
#     constrain_similarities: true
#   - name: FallbackClassifier
#     threshold: 0.3
#     ambiguity_threshold: 0.1

# Configuration for Rasa Core.
# https://rasa.com/docs/rasa/core/policies/
policies:
# # No configuration for policies was provided. The following default policies were used to train your model.
# # If you'd like to customize them, uncomment and adjust the policies.
# # See https://rasa.com/docs/rasa/policies for more information.
#   - name: MemoizationPolicy
#   - name: RulePolicy
#   - name: UnexpecTEDIntentPolicy
#     max_history: 5
#     epochs: 100
#   - name: TEDPolicy
#     max_history: 5
#     epochs: 100
#     constrain_similarities: true

```

## Intents <a name='intents'></a>
Section that discusses metrics on model intents.

### Metrics
Table with the metrics of intentions.
||intent|Precision|Recall|F1 Score|Examples|
|-|-|-|-|-|-|
|🟢|deny|100.0%|100.0%|100.0%|7|
|🟢|affirm|100.0%|100.0%|100.0%|6|
|🟢|goodbye|100.0%|100.0%|100.0%|10|
|🟢|greet|100.0%|100.0%|100.0%|13|
|🟢|bot_challenge|100.0%|100.0%|100.0%|4|
|🟢|mood_great|100.0%|100.0%|100.0%|14|
|🟢|mood_unhappy|100.0%|100.0%|100.0%|14|

### Confused intentions
Where all the confusing or wrong sentences of the model are listed.

No confusions or errors of intent were found in this model.
### Histogram
![Histogram](../image/sample_intent_histogram.png 'Histogram')
### Confusion Matrix
![Confusion Matrix](../image/sample_intent_confusion_matrix.png 'Confusion Matrix')

## Entities <a name='entities'></a>
Section that discusses metrics about the model entities.

### Metrics
Table with entity metrics.


No entities were found in this model.

### Confused entities
Where all the confusing or wrong entities of the model are listed.

No confusions of entities were found in this model.

## NLU <a name='nlu'></a>
Section that discusses metrics about NLU and its example phrases.

### Sentences
Table with metrics for bot training phrases.

||Text|Intent|Predicted intent|Confidence|Understood|
|-|-|-|-|-|-|
|🟢|amazing|mood_great|mood_great|100.0%|✅|
|🟢|I am amazing|mood_great|mood_great|100.0%|✅|
|🟢|perfect|mood_great|mood_great|100.0%|✅|
|🟢|great|mood_great|mood_great|100.0%|✅|
|🟢|so perfect|mood_great|mood_great|100.0%|✅|
|🟢|wonderful|mood_great|mood_great|100.0%|✅|
|🟢|extremely good|mood_great|mood_great|100.0%|✅|
|🟢|I am going to save the world|mood_great|mood_great|100.0%|✅|
|🟢|extremly sad|mood_unhappy|mood_unhappy|100.0%|✅|
|🟢|so saad|mood_unhappy|mood_unhappy|100.0%|✅|
|🟢|I am great|mood_great|mood_great|100.0%|✅|
|🟢|so sad|mood_unhappy|mood_unhappy|100.0%|✅|
|🟢|very sad|mood_unhappy|mood_unhappy|100.0%|✅|
|🟢|so so perfect|mood_great|mood_great|100.0%|✅|
|🟢|I am feeling very good|mood_great|mood_great|100.0%|✅|
|🟢|sad|mood_unhappy|mood_unhappy|100.0%|✅|
|🟢|hey|greet|greet|100.0%|✅|
|🟢|I am sad|mood_unhappy|mood_unhappy|100.0%|✅|
|🟢|super sad|mood_unhappy|mood_unhappy|100.0%|✅|
|🟢|feeling like a king|mood_great|mood_great|100.0%|✅|
|🟢|super stoked|mood_great|mood_great|100.0%|✅|
|🟢|hello|greet|greet|100.0%|✅|
|🟢|I'm so sad|mood_unhappy|mood_unhappy|100.0%|✅|
|🟢|hey dude|greet|greet|100.0%|✅|
|🟢|my day was horrible|mood_unhappy|mood_unhappy|100.0%|✅|
|🟢|hey there|greet|greet|100.0%|✅|
|🟢|unhappy|mood_unhappy|mood_unhappy|100.0%|✅|
|🟢|hi|greet|greet|100.0%|✅|
|🟢|hello there|greet|greet|100.0%|✅|
|🟢|goodmorning|greet|greet|100.0%|✅|
|🟢|I am disappointed|mood_unhappy|mood_unhappy|100.0%|✅|
|🟢|good morning|greet|greet|100.0%|✅|
|🟢|goodevening|greet|greet|100.0%|✅|
|🟢|good evening|greet|greet|100.0%|✅|
|🟢|bye|goodbye|goodbye|100.0%|✅|
|🟢|no|deny|deny|100.0%|✅|
|🟢|n|deny|deny|100.0%|✅|
|🟢|moin|greet|greet|100.0%|✅|
|🟢|so good|mood_great|mood_great|100.0%|✅|
|🟢|good afternoon|greet|greet|100.0%|✅|
|🟢|not very good|mood_unhappy|mood_unhappy|100.0%|✅|
|🟢|goodbye|goodbye|goodbye|100.0%|✅|
|🟢|let's go|greet|greet|100.0%|✅|
|🟢|I don't feel very well|mood_unhappy|mood_unhappy|100.0%|✅|
|🟢|bye bye|goodbye|goodbye|100.0%|✅|
|🟢|good night|goodbye|goodbye|100.0%|✅|
|🟢|not good|mood_unhappy|mood_unhappy|100.0%|✅|
|🟢|no way|deny|deny|100.0%|✅|
|🟢|cu|goodbye|goodbye|100.0%|✅|
|🟢|good by|goodbye|goodbye|100.0%|✅|
|🟢|see you around|goodbye|goodbye|100.0%|✅|
|🟢|I don't think so|deny|deny|100.0%|✅|
|🟢|see you later|goodbye|goodbye|100.0%|✅|
|🟢|have a nice day|goodbye|goodbye|100.0%|✅|
|🟢|never|deny|deny|100.0%|✅|
|🟢|cee you later|goodbye|goodbye|100.0%|✅|
|🟢|of course|affirm|affirm|100.0%|✅|
|🟢|yes|affirm|affirm|100.0%|✅|
|🟢|don't like that|deny|deny|100.0%|✅|
|🟢|not really|deny|deny|100.0%|✅|
|🟢|indeed|affirm|affirm|100.0%|✅|
|🟢|y|affirm|affirm|100.0%|✅|
|🟢|that sounds good|affirm|affirm|100.0%|✅|
|🟢|correct|affirm|affirm|100.0%|✅|
|🟢|are you a human?|bot_challenge|bot_challenge|100.0%|✅|
|🟢|am I talking to a human?|bot_challenge|bot_challenge|100.0%|✅|
|🟢|are you a bot?|bot_challenge|bot_challenge|100.0%|✅|
|🟢|am I talking to a bot?|bot_challenge|bot_challenge|100.0%|✅|

### Sentences with problems
Table with the sentences that were not understood correctly by the model.


There are no sentences that were not understood in this model.

## Responses <a name='responses'></a>
Section that discusses metrics about bot responses and stories.

### Metrics
Table with bot response metrics.

||Response|Precision|Recall|F1 Score|Number of occurrences|
|-|-|-|-|-|-|
|🟢|action_listen|100.0%|100.0%|100.0%|16|
|🟢|utter_happy|100.0%|100.0%|100.0%|3|
|🟢|utter_goodbye|100.0%|100.0%|100.0%|4|
|🟢|utter_iamabot|100.0%|100.0%|100.0%|1|
|🟢|utter_greet|100.0%|100.0%|100.0%|5|
|🟢|utter_cheer_up|100.0%|100.0%|100.0%|3|
|🟢|utter_did_that_help|100.0%|100.0%|100.0%|3|
### Confusion Matrix
![Confusion Matrix](../image/sample_story_confusion_matrix.png 'Confusion Matrix')

##### Generated by rasa-model-report, collaborative open-source project for Rasa projects. Github repository at this [link](https://github.com/brunohjs/rasa-model-report).
