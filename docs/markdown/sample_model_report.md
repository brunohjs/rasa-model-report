
# Model health report
## Index
 - [Overview](#overview)
 - [Config](#configs)
 - [Intents](#intents)
 - [Entities](#entities)
 - [NLU](#nlu)
 - [Core](#core)
 - [E2E Coverage](#e2e)


## Overview <a name='overview'></a>

### Bot info
|Bot Name|Creation date|Updated date|
|:-:|:-:|:-:|
|<span style='font-size:16px'>My project</span>|<span style='font-size:16px'>23/10/23 16:22:35</span>|<span style='font-size:16px'>23/10/23 16:22:37</span>|


### Score
|Intent|Entity|NLU|Core|E2E Coverage|<span style='font-size:20px'>Overall</span>|
|:-:|:-:|:-:|:-:|:-:|:-:|
|10            |-            |10            |10            |10            |<span style='font-size:20px'>**10**</span>|
🟢            |❌            |🟢            |🟢            |🟢            |<span style='font-size:20px'>🟢</span>|
### Element count
Describe the number of elements in the chatbot.

|Element type|Total|
|:-:|:-:|
|Intents|7|
|Entities|0|
|Actions and Utters|6|
|Stories|3|
|Rules|2|



## Configs <a name='configs'></a>
Settings that were used in the training *pipeline* and *policies*.
```yaml
# The config recipe.
# https://rasa.com/docs/rasa/model-configuration/
recipe: default.v1

# The assistant project unique identifier
# This default value must be replaced with a unique assistant name within your deployment
assistant_id: placeholder_default

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
|#||intent|Precision|Recall|F1 Score|Examples|
|:-:|-|-|-|-|-|-|
|1|🟢|greet|100.0%|100.0%|100.0%|13|
|2|🟢|affirm|100.0%|100.0%|100.0%|6|
|3|🟢|deny|100.0%|100.0%|100.0%|7|
|4|🟢|goodbye|100.0%|100.0%|100.0%|10|
|5|🟢|mood_great|100.0%|100.0%|100.0%|14|
|6|🟢|bot_challenge|100.0%|100.0%|100.0%|4|
|7|🟢|mood_unhappy|100.0%|100.0%|100.0%|14|

### Confused intentions
Where all the confusing or wrong sentences of the model are listed.

No confusions or errors of intent were found in this model.
### Histogram
![Histogram](results/intent_histogram.png 'Histogram')
### Confusion Matrix
![Confusion Matrix](results/intent_confusion_matrix.png 'Confusion Matrix')

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

|#||Text|Intent|Predicted intent|Confidence|Understood|
|:-:|-|-|-|-|-|-|
|1|🟢|bye|goodbye|goodbye|100.0%|✅|
|2|🟢|y|affirm|affirm|100.0%|✅|
|3|🟢|perfect|mood_great|mood_great|100.0%|✅|
|4|🟢|great|mood_great|mood_great|100.0%|✅|
|5|🟢|amazing|mood_great|mood_great|100.0%|✅|
|6|🟢|feeling like a king|mood_great|mood_great|100.0%|✅|
|7|🟢|wonderful|mood_great|mood_great|100.0%|✅|
|8|🟢|I am great|mood_great|mood_great|100.0%|✅|
|9|🟢|I am amazing|mood_great|mood_great|100.0%|✅|
|10|🟢|so so perfect|mood_great|mood_great|100.0%|✅|
|11|🟢|so perfect|mood_great|mood_great|100.0%|✅|
|12|🟢|I am sad|mood_unhappy|mood_unhappy|100.0%|✅|
|13|🟢|super sad|mood_unhappy|mood_unhappy|100.0%|✅|
|14|🟢|sad|mood_unhappy|mood_unhappy|100.0%|✅|
|15|🟢|very sad|mood_unhappy|mood_unhappy|100.0%|✅|
|16|🟢|unhappy|mood_unhappy|mood_unhappy|100.0%|✅|
|17|🟢|extremly sad|mood_unhappy|mood_unhappy|100.0%|✅|
|18|🟢|so saad|mood_unhappy|mood_unhappy|100.0%|✅|
|19|🟢|so sad|mood_unhappy|mood_unhappy|100.0%|✅|
|20|🟢|hey|greet|greet|100.0%|✅|
|21|🟢|cu|goodbye|goodbye|100.0%|✅|
|22|🟢|goodbye|goodbye|goodbye|100.0%|✅|
|23|🟢|yes|affirm|affirm|100.0%|✅|
|24|🟢|super stoked|mood_great|mood_great|100.0%|✅|
|25|🟢|extremely good|mood_great|mood_great|100.0%|✅|
|26|🟢|my day was horrible|mood_unhappy|mood_unhappy|100.0%|✅|
|27|🟢|I am disappointed|mood_unhappy|mood_unhappy|100.0%|✅|
|28|🟢|I'm so sad|mood_unhappy|mood_unhappy|100.0%|✅|
|29|🟢|bye bye|goodbye|goodbye|100.0%|✅|
|30|🟢|see you later|goodbye|goodbye|100.0%|✅|
|31|🟢|of course|affirm|affirm|100.0%|✅|
|32|🟢|I am feeling very good|mood_great|mood_great|100.0%|✅|
|33|🟢|so good|mood_great|mood_great|100.0%|✅|
|34|🟢|hi|greet|greet|100.0%|✅|
|35|🟢|good by|goodbye|goodbye|100.0%|✅|
|36|🟢|cee you later|goodbye|goodbye|100.0%|✅|
|37|🟢|I am going to save the world|mood_great|mood_great|100.0%|✅|
|38|🟢|not very good|mood_unhappy|mood_unhappy|100.0%|✅|
|39|🟢|hello|greet|greet|100.0%|✅|
|40|🟢|correct|affirm|affirm|100.0%|✅|
|41|🟢|hey there|greet|greet|100.0%|✅|
|42|🟢|hey dude|greet|greet|100.0%|✅|
|43|🟢|hello there|greet|greet|100.0%|✅|
|44|🟢|goodmorning|greet|greet|100.0%|✅|
|45|🟢|goodevening|greet|greet|100.0%|✅|
|46|🟢|good morning|greet|greet|100.0%|✅|
|47|🟢|moin|greet|greet|100.0%|✅|
|48|🟢|good evening|greet|greet|100.0%|✅|
|49|🟢|I don't feel very well|mood_unhappy|mood_unhappy|100.0%|✅|
|50|🟢|not good|mood_unhappy|mood_unhappy|100.0%|✅|
|51|🟢|good afternoon|greet|greet|100.0%|✅|
|52|🟢|see you around|goodbye|goodbye|100.0%|✅|
|53|🟢|good night|goodbye|goodbye|100.0%|✅|
|54|🟢|let's go|greet|greet|100.0%|✅|
|55|🟢|n|deny|deny|100.0%|✅|
|56|🟢|no|deny|deny|100.0%|✅|
|57|🟢|indeed|affirm|affirm|100.0%|✅|
|58|🟢|never|deny|deny|100.0%|✅|
|59|🟢|have a nice day|goodbye|goodbye|100.0%|✅|
|60|🟢|that sounds good|affirm|affirm|100.0%|✅|
|61|🟢|no way|deny|deny|100.0%|✅|
|62|🟢|not really|deny|deny|100.0%|✅|
|63|🟢|I don't think so|deny|deny|100.0%|✅|
|64|🟢|don't like that|deny|deny|100.0%|✅|
|65|🟢|am I talking to a human?|bot_challenge|bot_challenge|100.0%|✅|
|66|🟢|are you a human?|bot_challenge|bot_challenge|100.0%|✅|
|67|🟢|are you a bot?|bot_challenge|bot_challenge|100.0%|✅|
|68|🟢|am I talking to a bot?|bot_challenge|bot_challenge|100.0%|✅|

### Sentences with problems
Table with the sentences that were not understood correctly by the model.


There are no sentences that were not understood in this model.

## Core <a name='core'></a>
Section that discusses metrics about bot responses and actions.

### Metrics
Table with bot core metrics.

|#||Response|Precision|Recall|F1 Score|Number of occurrences|
|:-:|-|-|-|-|-|-|
|1|🟢|action_listen|100.0%|100.0%|100.0%|16|
|2|🟢|utter_did_that_help|100.0%|100.0%|100.0%|3|
|3|🟢|utter_goodbye|100.0%|100.0%|100.0%|4|
|4|🟢|utter_iamabot|100.0%|100.0%|100.0%|1|
|5|🟢|utter_greet|100.0%|100.0%|100.0%|5|
|6|🟢|utter_happy|100.0%|100.0%|100.0%|3|
|7|🟢|utter_cheer_up|100.0%|100.0%|100.0%|3|
### Confusion Matrix
![Confusion Matrix](results/story_confusion_matrix.png 'Confusion Matrix')

## E2E Coverage <a name='e2e'></a>
Section that shows data from intents and responses that aren't covered by end-to-end tests.

### Not covered elements
List with not covered elements by end-to-end tests.

#### Intents
 - (no elements not covered)

#### Actions
 - (no elements not covered)

Total number of elements: 13

Total number of not covered elements: 0

Total number of excluded elements: 0

Coverage rate: 100.0% (🟢)


##### Generated by rasa-model-report v1.4.2b14, collaborative open-source project for Rasa projects. Github repository at this [link](https://github.com/brunohjs/rasa-model-report).
