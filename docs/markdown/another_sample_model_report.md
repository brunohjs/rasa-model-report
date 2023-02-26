
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
|Bot Name|Rasa Version|Creation date|Updated date|
|:-:|:-:|:-:|:-:|
|<span style='font-size:16px'>Sara - the Rasa Demo Bot</span>|<span style='font-size:16px'>2.8.25</span>|<span style='font-size:16px'>25/02/23 23:54:27</span>|<span style='font-size:16px'>25/02/23 23:56:33</span>|

|Intent|Entity|NLU|Core|E2E Coverage|<span style='font-size:20px'>General</span>|
|:-:|:-:|:-:|:-:|:-:|:-:|
|9            |9            |9            |9            |3            |<span style='font-size:20px'>**8**</span>|
🟢            |🟢            |🟢            |🟢            |🔴            |<span style='font-size:20px'>🟡</span>|

## Configs <a name='configs'></a>
Settings that were used in the training *pipeline* and *policies*.
```yaml
language: en
pipeline:
- name: WhitespaceTokenizer
  token_pattern: (?u)\b\w+\b
- name: RegexFeaturizer
- name: LexicalSyntacticFeaturizer
- name: CountVectorsFeaturizer
  OOV_token: oov
- name: CountVectorsFeaturizer
  analyzer: char_wb
  min_ngram: 1
  max_ngram: 4
- name: DIETClassifier
  epochs: 200
  ranking_length: 5
- name: DucklingEntityExtractor
  url: http://localhost:8000
  dimensions:
  - email
  - number
  - amount-of-money
- name: EntitySynonymMapper
- name: ResponseSelector
  retrieval_intent: out_of_scope
  scale_loss: false
  epochs: 100
- name: ResponseSelector
  retrieval_intent: faq
  scale_loss: false
  epochs: 100
- name: ResponseSelector
  retrieval_intent: chitchat
  scale_loss: false
  epochs: 100
- name: FallbackClassifier
  threshold: 0.7
policies:
- name: RulePolicy
  core_fallback_threshold: 0.3
  core_fallback_action_name: "action_default_fallback"
  enable_fallback_prediction: True
- max_history: 6
  name: AugmentedMemoizationPolicy
- name: TEDPolicy
  max_history: 10
  epochs: 20
  batch_size:
  - 32
  - 64

```

## Intents <a name='intents'></a>
Section that discusses metrics on model intents.

### Metrics
Table with the metrics of intentions.
||intent|Precision|Recall|F1 Score|Examples|
|-|-|-|-|-|-|
|🟢|signup_newsletter|100.0%|100.0%|100.0%|141|
|🟢|pipeline_recommendation|100.0%|100.0%|100.0%|19|
|🟢|explain|100.0%|100.0%|100.0%|16|
|🟢|ask_why_contribute|100.0%|100.0%|100.0%|21|
|🟢|nlu_generation_tool_recommendation|100.0%|100.0%|100.0%|14|
|🟢|react_negative|100.0%|100.0%|100.0%|47|
|🟢|technical_question|100.0%|100.0%|100.0%|221|
|🟢|restart|100.0%|100.0%|100.0%|10|
|🟢|thank|100.0%|100.0%|100.0%|39|
|🟢|need_help_broad|100.0%|100.0%|100.0%|41|
|🟢|contact_sales|100.0%|100.0%|100.0%|155|
|🟢|why_rasa|100.0%|100.0%|100.0%|45|
|🟢|install_rasa|100.0%|100.0%|100.0%|108|
|🟢|ask_question_in_forum|100.0%|100.0%|100.0%|42|
|🟢|source_code|100.0%|100.0%|100.0%|34|
|🟢|switch|100.0%|100.0%|100.0%|54|
|🟢|human_handoff|100.0%|100.0%|100.0%|69|
|🟢|broken|100.0%|100.0%|100.0%|15|
|🟢|book_demo|100.0%|100.0%|100.0%|6|
|🟢|ask_which_events|100.0%|100.0%|100.0%|107|
|🟢|greet|100.0%|100.0%|100.0%|147|
|🟢|faq|99.9%|100.0%|99.9%|880|
|🟢|chitchat|99.8%|99.9%|99.8%|812|
|🟢|affirm|100.0%|99.6%|99.8%|224|
|🟢|how_to_get_started|100.0%|99.5%|99.8%|211|
|🟢|enter_data|99.7%|99.7%|99.7%|759|
|🟢|out_of_scope|99.5%|99.5%|99.5%|410|
|🟢|deny|100.0%|99.0%|99.5%|100|
|🟢|react_positive|98.5%|100.0%|99.2%|65|
|🟢|nlu_info|100.0%|98.4%|99.2%|62|
|🟢|ask_how_contribute|98.1%|100.0%|99.1%|53|
|🟢|bye|100.0%|97.6%|98.8%|42|
|🟢|canthelp|96.3%|100.0%|98.1%|26|

### Confused intentions
Where all the confusing or wrong sentences of the model are listed.
|Text|Intent|Predicted Intent|Confidence|
|-|-|-|-|
|4 + 2 = ?|out_of_scope|enter_data|100.0%|
|german|enter_data|out_of_scope|96.8%|
|Exit|bye|canthelp|96.6%|
|Sweet|affirm|react_positive|94.0%|
|how|out_of_scope|chitchat|86.8%|
|What can I do?|chitchat|ask_how_contribute|83.8%|
|time|enter_data|chitchat|78.7%|
|I want to build a chatbot|how_to_get_started|faq|77.1%|
|i don't want to give you my email|deny|out_of_scope|68.3%|
|Rasa NLu|nlu_info|enter_data|55.4%|
### Histogram
![Histogram](https://raw.githubusercontent.com/brunohjs/rasa-model-report/main/docs/image/another_sample_intent_histogram.png 'Histogram')
### Confusion Matrix
![Confusion Matrix](https://raw.githubusercontent.com/brunohjs/rasa-model-report/main/docs/image/another_sample_intent_confusion_matrix.png 'Confusion Matrix')

## Entities <a name='entities'></a>
Section that discusses metrics about the model entities.

### Metrics
Table with entity metrics.

||Entity|Precision|Recall|F1 Score|Examples|
|-|-|-|-|-|-|
|🟢|language|100.0%|100.0%|100.0%|297|
|🟢|location|100.0%|100.0%|100.0%|42|
|🟢|company|100.0%|100.0%|100.0%|88|
|🟢|install_type|100.0%|100.0%|100.0%|13|
|🟢|user_type|100.0%|100.0%|100.0%|19|
|🟢|current_api|100.0%|100.0%|100.0%|64|
|🟢|name|100.0%|100.0%|100.0%|155|
|🟢|nlu_part|100.0%|100.0%|100.0%|94|
|🟢|entity|100.0%|100.0%|100.0%|16|
|🟢|product|99.8%|100.0%|99.9%|554|
|🟢|job_function|98.8%|100.0%|99.4%|160|

### Confused entities
Where all the confusing or wrong entities of the model are listed.
<table>
            <thead>
                <tr>
                    <th>Text</th>
                    <th>Entity</th>
                    <th>Predicted entities</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>I'm a bot developer</td>
                    <td>
                        <details>
                            <summary>job_function</summary>
                            <pre>start: 10
                            <br>end: 19
                            <br>value: developer
                            </pre>
                        </details>
                    </td>
                    <td>
                        <details>
                            <summary>job_function</summary>
                            <pre>start: 6
                            <br>end: 19
                            <br>value: bot developer
                            </pre>
                        </details>
                    </td>
                </tr>
                <tr>
                    <td>i'm a developer</td>
                    <td>
                        -
                    </td>
                    <td>
                        <details>
                            <summary>job_function</summary>
                            <pre>start: 6
                            <br>end: 15
                            <br>value: developer
                            </pre>
                        </details>
                    </td>
                </tr>
                <tr>
                    <td>Rasa NLu</td>
                    <td>
                        -
                    </td>
                    <td>
                        <details>
                            <summary>product</summary>
                            <pre>start: 5
                            <br>end: 8
                            <br>value: nlu
                            </pre>
                        </details>
                    </td>
                </tr>
            </tbody>
        </table>

### Histogram
![Histogram](https://raw.githubusercontent.com/brunohjs/rasa-model-report/main/docs/image/another_sample_DIETClassifier_histogram.png 'Histogram')
### Confusion Matrix
![Confusion Matrix](https://raw.githubusercontent.com/brunohjs/rasa-model-report/main/docs/image/another_sample_DIETClassifier_confusion_matrix.png 'Confusion Matrix')

## NLU <a name='nlu'></a>
Section that discusses metrics about NLU and its example phrases.

### Sentences
Table with metrics for bot training phrases.

||Text|Intent|Predicted intent|Confidence|Understood|
|-|-|-|-|-|-|
|🟢|Do you know how you were built?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|HI Sara, what are you up to?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|What's new?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how are things going|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how is your day going|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how's your day going|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|okay hi how are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|whatchya upto ?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|whats goin on|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|whats new|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|and you are how many years old?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|how many years old are you?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|Are you a bot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|Are you the bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|are you a BOT|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|are you a bot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|are you a bot ?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|are you a bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|are you a real bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|are you artificial intelligence|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|are you sure that you're a bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|Can you speak more than one language?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|Do you speak any other languages?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|How many languages can you speak?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|In what languages are you fluent enough?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|In which languages can you speak?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|Speak any other languages?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|What are all of the different languages you can speak?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|What are the languages you can speak?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|What languages can you converse in?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|What languages do you know how to use?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|What languages do you know?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|What languages do you speak?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|Which languages do you speak?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|can you speak Spanish?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|do you speak any other languages?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|what foreign languages are you fluent in?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|what foreign languages do you know?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|what languages are you comfortable speaking at?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|what languages are you good at speaking?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|what languages do you know?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|what languages do you speak|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|what languages you can be comfortable speaking?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|what languages you can speak ?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|what languages you prefer more speaking at?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|you speak french ?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|Could you find me a restaurant to eat at?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Find a restaurant for me to eat at.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Find a restaurant for me where I can eat.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Find me a fast food restaurant.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Find me a restaurant where I can eat.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Hey help me find a restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|I need to find this restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|I'm gonna need help finding a restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Would you find me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Can we expect any thunderstorms?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|How is the weather today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|How is the weather?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|How is weather today|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|Is it hot or cold?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|Is it humid out there today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|What is the temperature today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|What is the weather at your place?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|What is the weather in newyork?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|What's the weather like over there?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|What's the weather like where I am right now?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|What's the weather like?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|how is the weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|how is the weather ?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|how is the weather in berlin?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|how is the weather?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|how's the weather in berlin|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|hows the weather in bot world|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|hows the weather today in berlin?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|is it hot outside ?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|the weather today|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|well, if you wish: what about the weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what about the weather in [Lüneburg](location)|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what is the weather in Berlin|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what is the weather in zurich?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what is the weather like where you are?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what is the weather like?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what's the weather like|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what's the weather like in LA|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what's the weather like?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what's the weather today|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what's the weather today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|whats the weather in berlin?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|whats the weather like tomorrow?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|Can you explain me in one sentence what you are doing?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|Can you help me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|Could you please show me what you can|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|How can you help me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|What can you do for me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|can I ask you anything else?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|can you do anything else?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|can you help me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|can you help me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|hello what can you do for me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|hm that doesnt quite help me is there anything else you can do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|how can you help me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|how can you help me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|how u can help me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|show me what's possible|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|so what can you help me with?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what are the options?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what can u do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what can you do for me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what cn u do for me ?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what else can you do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what else can you help with?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what u can do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what u can do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what you can do for me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|de que lugar eres?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|kalhmera sara ti kaneis|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|kannst du auch deutsch?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|kannst du dies auch auf deutsch?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|oui je besoine de l'aide|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|tu parles francais?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|kannst du mir helfen|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|I'm speaking a non-english language.|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|我该如何使用|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|你懂中文吗？|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|αστεία λές|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|I am asking you an out of scope question|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|After registration I see that I have an available balance of 0.00000000. What does this balance represent?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Are you ready?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Can I ask you questions first?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Can I get a hamburger?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Can YouTube talk?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Can you call me back ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Can you give me your datacenter's password|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Can you give me your datacenter's password?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Can you make sandwiches?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Can you please send me an uber|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Do I have to accept?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Do you know Kevin Pelton|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Find nearest pizzahut|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|HomeBase is advertised as a community. Is there a way to interact with other members of the community?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|How long does it take to set up a Rasa bot?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I already told you! I'm a shitmuncher|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I am an opioid addic|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I am an opioid addict|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I am hungry|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I am trying to build one, and did some research before, but I have not do hand-on work yet|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I can barely see this white text on light gray background ...|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I changed my mind|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I have installed it|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I ned a GP in 94301|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I need a GP in 94301|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I need a girl friend!|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I need to eat cake|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I wan to buy a plane|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I wanna marry you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I want a new laptop|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I want book a hotel|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I want french cuisine|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I want pizza|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I want to die|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I want to order pizza|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I want to use pipe|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I will check|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I'm a shitmuncher|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Is Rasa really smart?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Is this Goal-Oriented Chatbot?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Is today saturday?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Mail me the guide|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Make me a sandwich|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|SEL ME SOMETHING|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|The Try it out is not working|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|The weather is good|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Try it out broken|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What day is it today?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What did you eat yesterday?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What do you prefer?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What is todays date|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What is your hobbies?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What makes you better than a human?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What's 1 + 1?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What's do YouTube do|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What's your backend system?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Where am I right now?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Where am I?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Who are your customers|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Why don’t you answer?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Why is my TRUST score set to 50 after I completed the registration process?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Won't you ask me how I am?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Kristin, I want to marry you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|a tamed mouse will arrive at your doorstep in the next couple of days|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|aRE YOU SINGLE|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|alexa, order 5 tons of natrium chloride|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|and make chicken noises into the phone|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|are the newsletter worth the subscription?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|are u facebook|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|are u, facebook?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|are you single?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|are you dev?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|are you russian?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|are you sick|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|are you vegan|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|better than you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|book a ticket|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|but I just told you that :(|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|but if rasa is open source why do you have a sales team|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|buy groceries|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|call me father|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|can we keep chatting?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|can you book dinner|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|can you cheer me up|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|can you cook dinner|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|can you give me a cup of coffee|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|can you help me with the docs?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|can you help me with your docs|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|can you help me with your docs?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|can you learn from our conversation?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|can you speak about politic ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|can you understand ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|cannot see|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|connect to alexa|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|custom service|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|did i break you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|do you believe in god?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|do you have a phone number?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|do you have your photo?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|do you know me|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|do you know ras|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|do you liek cheese?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|do you like football|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|do you like movies|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|do you sell vacuum robots?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|do you want to marry me?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|example of a chatbot|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|get me a club mate|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|give me a girl friend|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|give me food|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|great, I'd like to buy a house|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|hang on let me find it|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|have you ever seen Keith Reilly?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|help with Alma Abrams|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|help with my life|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|hey little mama let em whisper in your ear|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|hey, I contacted you a couple of days ago but didn't get any response, any news?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how about NYC|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how are Alicia Jackson's cats doing?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how are the kids|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how can i get them?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how can i test this|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how come you say ok ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how do you learn|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how good is Rasa|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how it compares to alexa|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how long have you been online?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how long will the next version will launch?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how many lines of codes|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how much is 10 + 89 ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how much is 10 + 89|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how to get rasa studio|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how to go to newyork ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i am hungry|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i am hungry, what should i do?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i am not a developer but need this for business|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i can't deal with _your_ request|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i do not care how are you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i hope you will be better|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i immediately need help with implementing the coolest bot you can imagine|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i m looking for job|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i told you already|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i wanna party|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want a non dripping ice cream|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want caffe|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want food|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want good flycam|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want more of you in my life!|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want pizza|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want pizza!!|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want to book a hotel|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want to buy a roomba for my grandson|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want to eat|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want to find new friends|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want to find out what you can build with rasa|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want to fly|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want to grab lunch|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want to know current situtation in pakistan|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want to order a pizza|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want to see your happy customers|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i will tame a mouse for you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|is John Lewis still married to you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|is it a wasteland full of broken robot parts?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|is it allow to|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|is rasa a studio?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|is rasa any good|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|is that any of your business|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|isn't the newsletter just spam?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|it's a pity|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|mail me the steps|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|mascot means?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|my name k|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|no wait go back i want a dripping ice cream but a cone that catches it so you can drink the ice cream later|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|offer me lunch|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|oh my god, not again!|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|oh wait i gave you my work email address can i change it?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|on wiche nlp based system are you build?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|only that?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|order good|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|order pizza|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|personal or work?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|please help with my ice cream it's dripping|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|please hjave lunchj|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|please hurry, i have deadline in two weeks to deliver the bot it is for very big company|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|please play music|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|really? you're so touchy?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|region with no. of records|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|remember my name|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|search wikipedia|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|shitmuncher|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|show me a picture of a chicken|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|so, I'm helping right now to training you?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|someone call the police i think the bot died|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|sorry, i cannot rephrase|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|sudo make me a sandwich|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|tell me about yourself|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|tell me more about next best action|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|that doesn't sound like a joke|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|that link doesn't work!|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|the one that is better than you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|turn off my stove|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|wait a bit i am still reading|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what about wheather|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what are contextual AI assistants and how different are they from chatbots?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what are you doing now?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what are your uses for universities|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what did you eat for lunch?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what do oyu think about siri?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what do you think abou siri?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what do you think about Stanley Ramirez?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what do you think of alexa|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what does your soul feel my friend|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what doing|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what else?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what films do you like|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what i do after cd starter-pack-rasa-stack?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is a discourse?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is a mascot|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is adlingo|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is differance between bot and mascot?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is evolution ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is google rcs|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is machine learning|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is nice?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is the capital of delhi|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is the capital of india|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is the current petrol price|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is the day ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is the real use case where we can use this one|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is your address?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what is your purpose|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what lnu mean?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what the latest news ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what you ate today?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what's 5 + 5|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what's a newsletter?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what's gingerale|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what's your wife doing this weekend|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|whats that|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|whats the sign|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|when is the next train is coming?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|where do i get install files for mac?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|where is Oslo?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|where is mexico?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|wheres the party?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|which city are you talking about?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|which email|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|which email should i send to ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|which file is created first while developing chat bot|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|which is the LNU asynchronism ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|who are the engineers at rasa?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|who are they?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|who is Sharon Zeches|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|who is the MD of samsung bangalore ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|who is the president of india ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|who is your favourite robot?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|who let the dog out|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|who was hitler|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|who will anser my email?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|who's Bill Gates?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|whta you think about gdpr?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|why do you need that?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|why its called rasa ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|will u kill me|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|will u kill me?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|winter is already leaving|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|with you recommend me?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|would you like some water|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|yeah, my dog was drinking a couple of litres of water per day and tried drinking the swimming pool|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|you already have that|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|you can learn how to make a coffe|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|you have children?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|you have job opening|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|you lock sweety|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|you should learn to count|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|you will know it from the single red rose it carries between its teeth|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|you're a woman|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|ı am learning python|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|CALL THE POLICE|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|tertyryutyi|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|wsdrcftvgybhnj|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|why sky is blue?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what kind of bird are you?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|contextual|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|talk to me about voulette|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|voulette voulette|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Do you have a demo?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|please voulette|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Out of scope question.|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i need money|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|no, i need cash, money! Do you have it ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Hi i want to go palghar|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|I want to go palghar|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|your contry name|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|you girl|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want play ball|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|flight catch up|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how do you like your coffee|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Can you get analytics on who I'm chatting with when I use Rasa|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|have you heard of corona?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|where do i type in commandy|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|where to type in commands|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|you have to|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what type of bot?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|asdkjasdhjkasd|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|eshdtjfjfyk|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|drhdtjfjfyj|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|sudo reboot|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|asdfgasd|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|asdfgasdas|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What are some ways that nlu is different from core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|Do I need programming skills to develop a chatbot in rasa|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|Rasa can be programmed in python|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|programming language use|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|what programming language do i need?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|shall i use Nodejs as a programming language|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|must i have to be a good programmer to use RasA|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|what programming language is rasa written in?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|what programming languages does Rasa support?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|which programming languages do you support?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|which programming languages does rasa supports?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|what programming language do you recommend|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|programming language|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|what programming language does rasa use|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|But what kind of programming language is the code written in?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|I would like to know about using Java as a programming language with Rasa|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|what programming languages do you support|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|what is the your programming language|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|which programming language are you written in?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|which programming language uses rasa?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|in what programming language is your api|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|Which programming language is rasa written in?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|What languages can rasa handle?|faq/languages|faq/languages|100.0%|✅|
|🟢|What languages will the utility rasa support?|faq/languages|faq/languages|100.0%|✅|
|🟢|does Rasa support other languages like spanish?|faq/languages|faq/languages|100.0%|✅|
|🟢|how can I add new language to rasa|faq/languages|faq/languages|100.0%|✅|
|🟢|support for serbian language|faq/languages|faq/languages|100.0%|✅|
|🟢|what language list can I find for rasa|faq/languages|faq/languages|100.0%|✅|
|🟢|How much do you cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|How much does it cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|How much does rasa cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|how much costs the rasa platform|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|how much do you cost|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|how much does Rasa cost|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|how much does RASA cost ?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|how much does it cost|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|how much does it cost normally?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|how much does it cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|how much does rasa cost|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|how much does rasa cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is rasa free of cost|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is rasa stack free|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Are you open-source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|How do I find out if rasa is open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Is rasa open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Is rasa open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Is the rasa software open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Is your software open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|are you full open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|are you open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is rasa open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is rasa open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is it open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is it open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is rasa Open-Source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is rasa a type of open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is rasa an open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is rasa considered open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is rasa is open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is rasa like an open source software|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is rasa software that is classified as open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is the Rasa project open sourced?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is the project open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is the software rasa open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is this open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is this open source license|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is your product open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|ist es freie open source software|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|rasa is the open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|How is it opensource|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|you are open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|do you support alexa voice?|faq/voice|faq/voice|100.0%|✅|
|🟢|rasa can't be used to build a voice bot, can it?|faq/voice|faq/voice|100.0%|✅|
|🟢|240k/year|enter_data|enter_data|100.0%|✅|
|🟢|Flexible, but looking for low-cost alternative to proof of concept|enter_data|enter_data|100.0%|✅|
|🟢|I am a Data Scientist|enter_data|enter_data|100.0%|✅|
|🟢|I am a data scientist|enter_data|enter_data|100.0%|✅|
|🟢|I am responsible for our innovation department|enter_data|enter_data|100.0%|✅|
|🟢|I work as a frontend dev|enter_data|enter_data|100.0%|✅|
|🟢|I work at EXAMPLE insurance group as Head of Innovation|enter_data|enter_data|100.0%|✅|
|🟢|I'm Jeanine Hwang|enter_data|enter_data|100.0%|✅|
|🟢|I'm a software engineer|enter_data|enter_data|100.0%|✅|
|🟢|I'm the lead engineer|enter_data|enter_data|100.0%|✅|
|🟢|I’ve trained it in mandarin|enter_data|enter_data|100.0%|✅|
|🟢|My email is Richard@Simmons.com|enter_data|enter_data|100.0%|✅|
|🟢|My name is chelsea Parker|enter_data|enter_data|100.0%|✅|
|🟢|My name is jessie maglione|enter_data|enter_data|100.0%|✅|
|🟢|The name of the company is Daimler|enter_data|enter_data|100.0%|✅|
|🟢|300k|enter_data|enter_data|100.0%|✅|
|🟢|ACME Mops|enter_data|enter_data|100.0%|✅|
|🟢|AI engieer|enter_data|enter_data|100.0%|✅|
|🟢|Al Capone|enter_data|enter_data|100.0%|✅|
|🟢|BCG digital ventures|enter_data|enter_data|100.0%|✅|
|🟢|BigBotsInc|enter_data|enter_data|100.0%|✅|
|🟢|BigBots|enter_data|enter_data|100.0%|✅|
|🟢|Bosch|enter_data|enter_data|100.0%|✅|
|🟢|Ebony@gmail.com|enter_data|enter_data|100.0%|✅|
|🟢|Linda Mchone|enter_data|enter_data|100.0%|✅|
|🟢|Michele Perry|enter_data|enter_data|100.0%|✅|
|🟢|Michelle Garcia|enter_data|enter_data|100.0%|✅|
|🟢|Michelle Vinion|enter_data|enter_data|100.0%|✅|
|🟢|Software engineer.|enter_data|enter_data|100.0%|✅|
|🟢|Steven Carter's company|enter_data|enter_data|100.0%|✅|
|🟢|William Zelkind|enter_data|enter_data|100.0%|✅|
|🟢|Willie@gmail.com|enter_data|enter_data|100.0%|✅|
|🟢|abhbose3k@gmail.com|enter_data|enter_data|100.0%|✅|
|🟢|allianz|enter_data|enter_data|100.0%|✅|
|🟢|amounts|enter_data|enter_data|100.0%|✅|
|🟢|chinese is the language of my bot|enter_data|enter_data|100.0%|✅|
|🟢|chinese is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|🟢|data analyst|enter_data|enter_data|100.0%|✅|
|🟢|data science engineer|enter_data|enter_data|100.0%|✅|
|🟢|dutch is the language of my bot|enter_data|enter_data|100.0%|✅|
|🟢|french is the language of my bot|enter_data|enter_data|100.0%|✅|
|🟢|google enginer|enter_data|enter_data|100.0%|✅|
|🟢|italian is the language of my bot|enter_data|enter_data|100.0%|✅|
|🟢|italina|enter_data|enter_data|100.0%|✅|
|🟢|klara health|enter_data|enter_data|100.0%|✅|
|🟢|mandarin is the language of my bot|enter_data|enter_data|100.0%|✅|
|🟢|ml researcher|enter_data|enter_data|100.0%|✅|
|🟢|numbers|enter_data|enter_data|100.0%|✅|
|🟢|software engineer|enter_data|enter_data|100.0%|✅|
|🟢|vodafone|enter_data|enter_data|100.0%|✅|
|🟢|xyz|enter_data|enter_data|100.0%|✅|
|🟢|a sentient robot|enter_data|enter_data|100.0%|✅|
|🟢|around 200k|enter_data|enter_data|100.0%|✅|
|🟢|around one millon euros|enter_data|enter_data|100.0%|✅|
|🟢|conversational|enter_data|enter_data|100.0%|✅|
|🟢|customer service automation|enter_data|enter_data|100.0%|✅|
|🟢|customer service automation bot|enter_data|enter_data|100.0%|✅|
|🟢|email = Patti.Salazar@gmail.com|enter_data|enter_data|100.0%|✅|
|🟢|get dates from messages|enter_data|enter_data|100.0%|✅|
|🟢|i am self emplayed|enter_data|enter_data|100.0%|✅|
|🟢|i am a projject manager|enter_data|enter_data|100.0%|✅|
|🟢|i am interested in ordinals|enter_data|enter_data|100.0%|✅|
|🟢|i need a bot for customer service automation|enter_data|enter_data|100.0%|✅|
|🟢|i ues chinese|enter_data|enter_data|100.0%|✅|
|🟢|i want to extract names|enter_data|enter_data|100.0%|✅|
|🟢|i work in biz dev|enter_data|enter_data|100.0%|✅|
|🟢|i'm a solutions architect|enter_data|enter_data|100.0%|✅|
|🟢|i'm in customer success|enter_data|enter_data|100.0%|✅|
|🟢|it is in chinese|enter_data|enter_data|100.0%|✅|
|🟢|it is in dutch|enter_data|enter_data|100.0%|✅|
|🟢|it is in french|enter_data|enter_data|100.0%|✅|
|🟢|it is in italian|enter_data|enter_data|100.0%|✅|
|🟢|it is in mandarin|enter_data|enter_data|100.0%|✅|
|🟢|it speaks chinese|enter_data|enter_data|100.0%|✅|
|🟢|it speaks english|enter_data|enter_data|100.0%|✅|
|🟢|it speaks italian|enter_data|enter_data|100.0%|✅|
|🟢|it speaks mandarin|enter_data|enter_data|100.0%|✅|
|🟢|it speaks portuguese|enter_data|enter_data|100.0%|✅|
|🟢|it's Katie Betz|enter_data|enter_data|100.0%|✅|
|🟢|it's Robert Weir|enter_data|enter_data|100.0%|✅|
|🟢|it's a small company from the US, the name is Microsoft|enter_data|enter_data|100.0%|✅|
|🟢|it's a tech company, apple|enter_data|enter_data|100.0%|✅|
|🟢|it's the moabit yoga studio|enter_data|enter_data|100.0%|✅|
|🟢|it’s an chinese bot|enter_data|enter_data|100.0%|✅|
|🟢|it’s available in chinese|enter_data|enter_data|100.0%|✅|
|🟢|it’s available in dutch|enter_data|enter_data|100.0%|✅|
|🟢|it’s available in italian|enter_data|enter_data|100.0%|✅|
|🟢|it’s available in mandarin|enter_data|enter_data|100.0%|✅|
|🟢|it’s in chinese|enter_data|enter_data|100.0%|✅|
|🟢|it’s in dutch|enter_data|enter_data|100.0%|✅|
|🟢|it’s in french|enter_data|enter_data|100.0%|✅|
|🟢|it’s in italian|enter_data|enter_data|100.0%|✅|
|🟢|it’s in mandarin|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained in chinese|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained in dutch|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained in french|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained in italian|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained in mandarin|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained only in chinese|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained only in dutch|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained only in english|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained only in french|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained only in italian|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained only in mandarin|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained only in spanish|enter_data|enter_data|100.0%|✅|
|🟢|language = mandarin|enter_data|enter_data|100.0%|✅|
|🟢|language: mandarin|enter_data|enter_data|100.0%|✅|
|🟢|my bot is in chinese|enter_data|enter_data|100.0%|✅|
|🟢|my bot is in dutch|enter_data|enter_data|100.0%|✅|
|🟢|my bot is in french|enter_data|enter_data|100.0%|✅|
|🟢|my bot is in mandarin|enter_data|enter_data|100.0%|✅|
|🟢|my email is K_Spivey@yahoo.com|enter_data|enter_data|100.0%|✅|
|🟢|my email is Mia_Gainey@gmail.com|enter_data|enter_data|100.0%|✅|
|🟢|my email is S_Calderon@Cofield.com|enter_data|enter_data|100.0%|✅|
|🟢|my name is Alexander Kohn|enter_data|enter_data|100.0%|✅|
|🟢|my name is betty mclendon|enter_data|enter_data|100.0%|✅|
|🟢|my name is Frances Kunkle|enter_data|enter_data|100.0%|✅|
|🟢|my name is Greg King|enter_data|enter_data|100.0%|✅|
|🟢|my name is John Evers|enter_data|enter_data|100.0%|✅|
|🟢|my name is Joseph Parson|enter_data|enter_data|100.0%|✅|
|🟢|my name is Nigel Partida|enter_data|enter_data|100.0%|✅|
|🟢|my name is susan crandall|enter_data|enter_data|100.0%|✅|
|🟢|n/a|enter_data|enter_data|100.0%|✅|
|🟢|so far it only speaks chinese|enter_data|enter_data|100.0%|✅|
|🟢|so far it only speaks dutch|enter_data|enter_data|100.0%|✅|
|🟢|so far it only speaks english|enter_data|enter_data|100.0%|✅|
|🟢|so far it only speaks french|enter_data|enter_data|100.0%|✅|
|🟢|so far it only speaks italian|enter_data|enter_data|100.0%|✅|
|🟢|so far it only speaks mandarin|enter_data|enter_data|100.0%|✅|
|🟢|so far it only speaks portuguese|enter_data|enter_data|100.0%|✅|
|🟢|so far it only speaks spanish|enter_data|enter_data|100.0%|✅|
|🟢|something to talk to my friends while I'm busy working|enter_data|enter_data|100.0%|✅|
|🟢|the New York Times|enter_data|enter_data|100.0%|✅|
|🟢|the assistant is in chinese|enter_data|enter_data|100.0%|✅|
|🟢|the assistant is in dutch|enter_data|enter_data|100.0%|✅|
|🟢|the assistant is in mandarin|enter_data|enter_data|100.0%|✅|
|🟢|the assistant speaks chinese|enter_data|enter_data|100.0%|✅|
|🟢|the assistant speaks mandarin|enter_data|enter_data|100.0%|✅|
|🟢|the bot speaks chinese|enter_data|enter_data|100.0%|✅|
|🟢|the bot speaks french|enter_data|enter_data|100.0%|✅|
|🟢|the bot speaks mandarin|enter_data|enter_data|100.0%|✅|
|🟢|the language is chinese|enter_data|enter_data|100.0%|✅|
|🟢|the language is dutch|enter_data|enter_data|100.0%|✅|
|🟢|the language is english|enter_data|enter_data|100.0%|✅|
|🟢|the language is french|enter_data|enter_data|100.0%|✅|
|🟢|the language is italian|enter_data|enter_data|100.0%|✅|
|🟢|the language is mandarin|enter_data|enter_data|100.0%|✅|
|🟢|the language of the ai assistant is chinese|enter_data|enter_data|100.0%|✅|
|🟢|the language of the ai assistant is french|enter_data|enter_data|100.0%|✅|
|🟢|the people speak chinese|enter_data|enter_data|100.0%|✅|
|🟢|the people speak dutch|enter_data|enter_data|100.0%|✅|
|🟢|the people speak english|enter_data|enter_data|100.0%|✅|
|🟢|the people speak italian|enter_data|enter_data|100.0%|✅|
|🟢|the people speak mandarin|enter_data|enter_data|100.0%|✅|
|🟢|the people speak portuguese|enter_data|enter_data|100.0%|✅|
|🟢|the people speak spanish|enter_data|enter_data|100.0%|✅|
|🟢|until now it’s only in chinese|enter_data|enter_data|100.0%|✅|
|🟢|until now it’s only in dutch|enter_data|enter_data|100.0%|✅|
|🟢|until now it’s only in english|enter_data|enter_data|100.0%|✅|
|🟢|until now it’s only in french|enter_data|enter_data|100.0%|✅|
|🟢|until now it’s only in italian|enter_data|enter_data|100.0%|✅|
|🟢|until now it’s only in mandarin|enter_data|enter_data|100.0%|✅|
|🟢|until now it’s only in portuguese|enter_data|enter_data|100.0%|✅|
|🟢|until now it’s only in spanish|enter_data|enter_data|100.0%|✅|
|🟢|user can talk to my bot in chinese|enter_data|enter_data|100.0%|✅|
|🟢|user can talk to my bot in dutch|enter_data|enter_data|100.0%|✅|
|🟢|user can talk to my bot in english|enter_data|enter_data|100.0%|✅|
|🟢|user can talk to my bot in french|enter_data|enter_data|100.0%|✅|
|🟢|user can talk to my bot in italian|enter_data|enter_data|100.0%|✅|
|🟢|user can talk to my bot in mandarin|enter_data|enter_data|100.0%|✅|
|🟢|user can talk to my bot in portuguese|enter_data|enter_data|100.0%|✅|
|🟢|user can talk to my bot in spanish|enter_data|enter_data|100.0%|✅|
|🟢|My name is manuel|enter_data|enter_data|100.0%|✅|
|🟢|simple bpt|enter_data|enter_data|100.0%|✅|
|🟢|contexual|enter_data|enter_data|100.0%|✅|
|🟢|local|enter_data|enter_data|100.0%|✅|
|🟢|my computer|enter_data|enter_data|100.0%|✅|
|🟢|my machine|enter_data|enter_data|100.0%|✅|
|🟢|my laptop|enter_data|enter_data|100.0%|✅|
|🟢|local machine|enter_data|enter_data|100.0%|✅|
|🟢|dialogue management|enter_data|enter_data|100.0%|✅|
|🟢|DIALOGUE MANAGEMENT|enter_data|enter_data|100.0%|✅|
|🟢|dialog management|enter_data|enter_data|100.0%|✅|
|🟢|how is your day|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|What will be your age on your next birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|What languages can you communicate in?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|Could you find me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Would you find a restaurant for me?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|is the sun out where zou are?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what is the weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what's the weather like where you are?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|wheather be like at your place?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|But you're an english site :(|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Have we met before?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|You'r blue.|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|common, just try|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|genocide|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|machine learning|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|tricked  ya|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Do you know how many people are in the Rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|How many members in the community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|what programming language?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|What all languages does rasa support for us?|faq/languages|faq/languages|100.0%|✅|
|🟢|can rasa understand this language?|faq/languages|faq/languages|100.0%|✅|
|🟢|How much it costs|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|how much it costs?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Is it a open source or any premium offer is available|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Will it be correct if I said I can build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|I book a bus ticket|enter_data|enter_data|100.0%|✅|
|🟢|I'm a conversation designer|enter_data|enter_data|100.0%|✅|
|🟢|I’ve trained it in italian|enter_data|enter_data|100.0%|✅|
|🟢|My name is Sondra Boyd|enter_data|enter_data|100.0%|✅|
|🟢|20000k|enter_data|enter_data|100.0%|✅|
|🟢|200k|enter_data|enter_data|100.0%|✅|
|🟢|Allianz|enter_data|enter_data|100.0%|✅|
|🟢|Angel Robinson company|enter_data|enter_data|100.0%|✅|
|🟢|COO|enter_data|enter_data|100.0%|✅|
|🟢|Product Manager|enter_data|enter_data|100.0%|✅|
|🟢|brand manager|enter_data|enter_data|100.0%|✅|
|🟢|companies|enter_data|enter_data|100.0%|✅|
|🟢|engineer|enter_data|enter_data|100.0%|✅|
|🟢|french is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|🟢|growth manager|enter_data|enter_data|100.0%|✅|
|🟢|mandarin is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|🟢|microsoft|enter_data|enter_data|100.0%|✅|
|🟢|one billion|enter_data|enter_data|100.0%|✅|
|🟢|portuguese is the language of my bot|enter_data|enter_data|100.0%|✅|
|🟢|portuguese is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|🟢|project manager|enter_data|enter_data|100.0%|✅|
|🟢|wurst co kg|enter_data|enter_data|100.0%|✅|
|🟢|chief nerd at rasa technologies|enter_data|enter_data|100.0%|✅|
|🟢|i have none|enter_data|enter_data|100.0%|✅|
|🟢|it is in english|enter_data|enter_data|100.0%|✅|
|🟢|it speaks dutch|enter_data|enter_data|100.0%|✅|
|🟢|it speaks french|enter_data|enter_data|100.0%|✅|
|🟢|it's R_Iuliucci@yahoo.com|enter_data|enter_data|100.0%|✅|
|🟢|its an chinese bot|enter_data|enter_data|100.0%|✅|
|🟢|its an dutch bot|enter_data|enter_data|100.0%|✅|
|🟢|its an french bot|enter_data|enter_data|100.0%|✅|
|🟢|its an italian bot|enter_data|enter_data|100.0%|✅|
|🟢|its an mandarin bot|enter_data|enter_data|100.0%|✅|
|🟢|it’s an dutch bot|enter_data|enter_data|100.0%|✅|
|🟢|it’s an french bot|enter_data|enter_data|100.0%|✅|
|🟢|it’s an italian bot|enter_data|enter_data|100.0%|✅|
|🟢|it’s an mandarin bot|enter_data|enter_data|100.0%|✅|
|🟢|it’s available in english|enter_data|enter_data|100.0%|✅|
|🟢|it’s in english|enter_data|enter_data|100.0%|✅|
|🟢|it’s in portuguese|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained in english|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained in spanish|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained only in portuguese|enter_data|enter_data|100.0%|✅|
|🟢|language = chinese|enter_data|enter_data|100.0%|✅|
|🟢|language: chinese|enter_data|enter_data|100.0%|✅|
|🟢|my bot is in english|enter_data|enter_data|100.0%|✅|
|🟢|my bot is in italian|enter_data|enter_data|100.0%|✅|
|🟢|my name is james culpit|enter_data|enter_data|100.0%|✅|
|🟢|sales assitant|enter_data|enter_data|100.0%|✅|
|🟢|the assistant is in french|enter_data|enter_data|100.0%|✅|
|🟢|the assistant speaks dutch|enter_data|enter_data|100.0%|✅|
|🟢|the bot speaks dutch|enter_data|enter_data|100.0%|✅|
|🟢|the bot speaks portuguese|enter_data|enter_data|100.0%|✅|
|🟢|the language of the ai assistant is italian|enter_data|enter_data|100.0%|✅|
|🟢|the people speak french|enter_data|enter_data|100.0%|✅|
|🟢|user can communicate with the bot in mandarin|enter_data|enter_data|100.0%|✅|
|🟢|the company is called t10|enter_data|enter_data|100.0%|✅|
|🟢|Dialogue management|enter_data|enter_data|100.0%|✅|
|🟢|By what method were you fashioned?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|Can you say how you were constructed?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|How were you made into who you are?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|how are you doing today?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|hw r u?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|what are you up to?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|can you tell me what number represents your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|are you really a bot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|cuz you are a bot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|what languages you know?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|which languages do you understand?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|Can you find me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Help me find a restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|I am hungry, find me some place to go|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Recommend me a restaurant around here.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Show me how to find a restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Suggest me a good restaurant around|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|can you find me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Can you tell me the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|Is it quite breezy outside?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|What does Rasa do?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|explain me what rasa does|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|explain me what rasa is|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what does rasa do|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what does rasa do ?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what does rasa do?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|i asked you if you can do anything else|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what can i do now|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|Where are your origins?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|Wie fange ich mit Rasa an?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|日本語分かる？|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|你叫什么名字|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|contextua|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Can you tell which messaging channels does rasa support?|faq/channels|faq/channels|100.0%|✅|
|🟢|What channels for messaging does rasa support?|faq/channels|faq/channels|100.0%|✅|
|🟢|How many people are in the Rasa Community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|What makes core and nlu different?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what is different about core compared to nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what is the difference between core and nlu|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what is the difference between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what is the difference between nlu and core|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what is the difference between nlu and core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what's the difference between NLU and Core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what's the difference between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|Does rasa require programming knowledge|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|what programming languge do i use|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|Can i use python to program my bot?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|must i have to be a good programmer|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|what programming language is used by rasa|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|which programming language used for RASA.|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|what's your programming language|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|Is there API for any other programming languages?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|can rasa speak portuguese?|faq/languages|faq/languages|100.0%|✅|
|🟢|what languages are available?|faq/languages|faq/languages|100.0%|✅|
|🟢|what languages can be supported by rasa?|faq/languages|faq/languages|100.0%|✅|
|🟢|Is Rasa a software formatted as open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|The rasa software, is that open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|could I call rasa open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is this opensource?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is rasa opensource?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Can I use rasa to build a voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|Do you know if I can build a voice bot using rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|Do you see an application of rasa in voice bot building?|faq/voice|faq/voice|100.0%|✅|
|🟢|How can I use to rasa to build a voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|Is it possible to build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|Is it possible to use rasa to build a voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|It is possible to build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|can rasa be used to build a voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|1 euro|enter_data|enter_data|100.0%|✅|
|🟢|100000k|enter_data|enter_data|100.0%|✅|
|🟢|10000k|enter_data|enter_data|100.0%|✅|
|🟢|2 euro|enter_data|enter_data|100.0%|✅|
|🟢|5 euros|enter_data|enter_data|100.0%|✅|
|🟢|60 million INR|enter_data|enter_data|100.0%|✅|
|🟢|ACME brands|enter_data|enter_data|100.0%|✅|
|🟢|I am Christina Sullivan|enter_data|enter_data|100.0%|✅|
|🟢|I am Robert Starks|enter_data|enter_data|100.0%|✅|
|🟢|I want a bot that sales my product that Catherine Rodriguez finally can focus on important stuff|enter_data|enter_data|100.0%|✅|
|🟢|I work at the NYT|enter_data|enter_data|100.0%|✅|
|🟢|I wrote it in mandarin|enter_data|enter_data|100.0%|✅|
|🟢|I'm project manager|enter_data|enter_data|100.0%|✅|
|🟢|I'm a product manager|enter_data|enter_data|100.0%|✅|
|🟢|I'm a project manager|enter_data|enter_data|100.0%|✅|
|🟢|I'm a student|enter_data|enter_data|100.0%|✅|
|🟢|It is Drew@Mccarthy.com|enter_data|enter_data|100.0%|✅|
|🟢|I’ve trained it in chinese|enter_data|enter_data|100.0%|✅|
|🟢|I’ve trained it in dutch|enter_data|enter_data|100.0%|✅|
|🟢|I’ve trained it in french|enter_data|enter_data|100.0%|✅|
|🟢|None|enter_data|enter_data|100.0%|✅|
|🟢|2000k|enter_data|enter_data|100.0%|✅|
|🟢|500k|enter_data|enter_data|100.0%|✅|
|🟢|AI researcher|enter_data|enter_data|100.0%|✅|
|🟢|BCBSM|enter_data|enter_data|100.0%|✅|
|🟢|CEO|enter_data|enter_data|100.0%|✅|
|🟢|Club Mate|enter_data|enter_data|100.0%|✅|
|🟢|Denise Armstrong's company|enter_data|enter_data|100.0%|✅|
|🟢|I am a freelancer|enter_data|enter_data|100.0%|✅|
|🟢|IT manager|enter_data|enter_data|100.0%|✅|
|🟢|Jamie Moore|enter_data|enter_data|100.0%|✅|
|🟢|John Strickland|enter_data|enter_data|100.0%|✅|
|🟢|None?|enter_data|enter_data|100.0%|✅|
|🟢|Terri Cline|enter_data|enter_data|100.0%|✅|
|🟢|a@b.com|enter_data|enter_data|100.0%|✅|
|🟢|assistant to the CEO|enter_data|enter_data|100.0%|✅|
|🟢|bayer|enter_data|enter_data|100.0%|✅|
|🟢|data scientist|enter_data|enter_data|100.0%|✅|
|🟢|dutch is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|🟢|english is the language of my bot|enter_data|enter_data|100.0%|✅|
|🟢|english is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|🟢|fullstack|enter_data|enter_data|100.0%|✅|
|🟢|italian is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|🟢|mandarin|enter_data|enter_data|100.0%|✅|
|🟢|no job|enter_data|enter_data|100.0%|✅|
|🟢|none|enter_data|enter_data|100.0%|✅|
|🟢|one|enter_data|enter_data|100.0%|✅|
|🟢|product manager|enter_data|enter_data|100.0%|✅|
|🟢|reddit|enter_data|enter_data|100.0%|✅|
|🟢|spanish is the language of my bot|enter_data|enter_data|100.0%|✅|
|🟢|spanish is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|🟢|a big ol transformer|enter_data|enter_data|100.0%|✅|
|🟢|a shitty bot|enter_data|enter_data|100.0%|✅|
|🟢|all the training data was in dutch|enter_data|enter_data|100.0%|✅|
|🟢|all the training data was in french|enter_data|enter_data|100.0%|✅|
|🟢|around $500,000 per year|enter_data|enter_data|100.0%|✅|
|🟢|can you try E_Conder@gmail.com instead?|enter_data|enter_data|100.0%|✅|
|🟢|chief lemonade officer|enter_data|enter_data|100.0%|✅|
|🟢|eisenkleber limited co kg|enter_data|enter_data|100.0%|✅|
|🟢|half a million|enter_data|enter_data|100.0%|✅|
|🟢|i have about 200 bucks in my savings account|enter_data|enter_data|100.0%|✅|
|🟢|i sell turtles|enter_data|enter_data|100.0%|✅|
|🟢|i'm a product manager|enter_data|enter_data|100.0%|✅|
|🟢|it is in portuguese|enter_data|enter_data|100.0%|✅|
|🟢|it speaks spanish|enter_data|enter_data|100.0%|✅|
|🟢|it’s an portuguese bot|enter_data|enter_data|100.0%|✅|
|🟢|it’s available in french|enter_data|enter_data|100.0%|✅|
|🟢|it’s in spanish|enter_data|enter_data|100.0%|✅|
|🟢|it’s only in chinese but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|🟢|it’s only in dutch but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|🟢|it’s only in mandarin but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|🟢|it’s only in portuguese but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained in portuguese|enter_data|enter_data|100.0%|✅|
|🟢|language = dutch|enter_data|enter_data|100.0%|✅|
|🟢|language: dutch|enter_data|enter_data|100.0%|✅|
|🟢|my bot is in portuguese|enter_data|enter_data|100.0%|✅|
|🟢|my bot is in spanish|enter_data|enter_data|100.0%|✅|
|🟢|my business mail is s_Dibenedetto@Simpson.net|enter_data|enter_data|100.0%|✅|
|🟢|my email is Elinor_Stock@Higgenbotham.com|enter_data|enter_data|100.0%|✅|
|🟢|my name is Felicia Cosby|enter_data|enter_data|100.0%|✅|
|🟢|my name is Jermaine Mccleery|enter_data|enter_data|100.0%|✅|
|🟢|my name is Tabitha Schoenthal|enter_data|enter_data|100.0%|✅|
|🟢|not sure yet, we plan with 50 thousand euro at the moment|enter_data|enter_data|100.0%|✅|
|🟢|one trillion dollar|enter_data|enter_data|100.0%|✅|
|🟢|sales guy|enter_data|enter_data|100.0%|✅|
|🟢|the assistant speaks english|enter_data|enter_data|100.0%|✅|
|🟢|the assistant speaks italian|enter_data|enter_data|100.0%|✅|
|🟢|the assistant speaks portuguese|enter_data|enter_data|100.0%|✅|
|🟢|the assistant speaks spanish|enter_data|enter_data|100.0%|✅|
|🟢|the bot speaks english|enter_data|enter_data|100.0%|✅|
|🟢|the bot speaks italian|enter_data|enter_data|100.0%|✅|
|🟢|the bot speaks spanish|enter_data|enter_data|100.0%|✅|
|🟢|the language is spanish|enter_data|enter_data|100.0%|✅|
|🟢|the language of the ai assistant is dutch|enter_data|enter_data|100.0%|✅|
|🟢|the language of the ai assistant is english|enter_data|enter_data|100.0%|✅|
|🟢|the language of the ai assistant is mandarin|enter_data|enter_data|100.0%|✅|
|🟢|the language of the ai assistant is spanish|enter_data|enter_data|100.0%|✅|
|🟢|user can communicate with the bot in chinese|enter_data|enter_data|100.0%|✅|
|🟢|we think 4 million INR/ year|enter_data|enter_data|100.0%|✅|
|🟢|just NLU|enter_data|enter_data|100.0%|✅|
|🟢|are you artificial|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|Can you find a restaurant for me?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Could you find a restaurant for me?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Find a restaurant for me?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Hi, can you give me the nearest fast food place?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Will you find me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|hilf mir beim start|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|tschüssikowski|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|kya hindi me bat kar sakate ho|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|coronavirus|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Is Core different than NLU?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what are the difference between NLU and core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|How can I build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|I can build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|can a voice bot be built using rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|can i build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|with rasa can I build a voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|Could you please explain the Rasa forum to me?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|I am Hattie Rice|enter_data|enter_data|100.0%|✅|
|🟢|I want to build a health insurance bot|enter_data|enter_data|100.0%|✅|
|🟢|I work for Stanford University|enter_data|enter_data|100.0%|✅|
|🟢|I'm in project mgmt|enter_data|enter_data|100.0%|✅|
|🟢|My name is Ashleigh Mees|enter_data|enter_data|100.0%|✅|
|🟢|My name is Louise Caudill|enter_data|enter_data|100.0%|✅|
|🟢|This is Kim Vanderveen|enter_data|enter_data|100.0%|✅|
|🟢|1 million|enter_data|enter_data|100.0%|✅|
|🟢|1 million big ones|enter_data|enter_data|100.0%|✅|
|🟢|2 million|enter_data|enter_data|100.0%|✅|
|🟢|500 million|enter_data|enter_data|100.0%|✅|
|🟢|Carolyn.Eisenhauer@Watkins.com|enter_data|enter_data|100.0%|✅|
|🟢|David Carter|enter_data|enter_data|100.0%|✅|
|🟢|Developer Advocate|enter_data|enter_data|100.0%|✅|
|🟢|K_Claytor@yahoo.com|enter_data|enter_data|100.0%|✅|
|🟢|N26|enter_data|enter_data|100.0%|✅|
|🟢|ceo|enter_data|enter_data|100.0%|✅|
|🟢|a good one?|enter_data|enter_data|100.0%|✅|
|🟢|a health bot|enter_data|enter_data|100.0%|✅|
|🟢|all the training data was in english|enter_data|enter_data|100.0%|✅|
|🟢|boo|enter_data|enter_data|100.0%|✅|
|🟢|i don't have one|enter_data|enter_data|100.0%|✅|
|🟢|i use anaconda|enter_data|enter_data|100.0%|✅|
|🟢|it is in spanish|enter_data|enter_data|100.0%|✅|
|🟢|it's Shannon.Adelman@Hurt.com|enter_data|enter_data|100.0%|✅|
|🟢|it’s available in spanish|enter_data|enter_data|100.0%|✅|
|🟢|mi name is Kathy Wright|enter_data|enter_data|100.0%|✅|
|🟢|my email is Carole@Hart.com|enter_data|enter_data|100.0%|✅|
|🟢|my email is M_Jones@Luna.com|enter_data|enter_data|100.0%|✅|
|🟢|my emayl is V_Comley@Nelson.com|enter_data|enter_data|100.0%|✅|
|🟢|so far it only speaks german|enter_data|enter_data|100.0%|✅|
|🟢|the ice cream factory is the company|enter_data|enter_data|100.0%|✅|
|🟢|the assistant is in english|enter_data|enter_data|100.0%|✅|
|🟢|the assistant is in italian|enter_data|enter_data|100.0%|✅|
|🟢|the assistant is in portuguese|enter_data|enter_data|100.0%|✅|
|🟢|the assistant is in spanish|enter_data|enter_data|100.0%|✅|
|🟢|the language is portuguese|enter_data|enter_data|100.0%|✅|
|🟢|the language of the ai assistant is portuguese|enter_data|enter_data|100.0%|✅|
|🟢|Dialogue Management please|enter_data|enter_data|100.0%|✅|
|🟢|dialogue management please|enter_data|enter_data|100.0%|✅|
|🟢|Do you know how you were made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|is everything okay|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|what's up sara|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|What was your age on your last birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|what age were you when you celebrated your last birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|are you bot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|are you bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|What languages are you fluent in?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|Do you find me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Can you tell me what time it is?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|Pardon me, but do you know the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|What's the time right now?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|What is the weather for tomorrow?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|excellent - is it hot in Berlin?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|hows the waether|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what is the whether today|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|whats the temperature in delhi?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|can you pls explain what rasa does|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|i want to know what rasa does|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|What are my options|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|What city do you claim to for your birth?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|como inicio en rasa|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|Pizza bot|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|buy one please|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|chinese ok?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|silly bot|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|some thing else|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What components does Rasa have?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|rasa supports which messaging channels?|faq/channels|faq/channels|100.0%|✅|
|🟢|How many people are in your community|faq/community_size|faq/community_size|100.0%|✅|
|🟢|How many people are in your community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|Is nlu different to core and, if so, how?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|What is the difference between NLU and Core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|What makes core different from nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what differences are there between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what makes core different from nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|whats the difference between core and nlu|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|do i need to be able to program to use rasa?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|Do I have to be a programmer to use rasa?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|Can you use other language than English?|faq/languages|faq/languages|100.0%|✅|
|🟢|available for German?|faq/languages|faq/languages|100.0%|✅|
|🟢|hich languages supports rasa|faq/languages|faq/languages|100.0%|✅|
|🟢|would you call rasa open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Can I use my voice to speak to these bots?|faq/voice|faq/voice|100.0%|✅|
|🟢|Can you build a voice bot using rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|How to use rasa to build a voice bot.|faq/voice|faq/voice|100.0%|✅|
|🟢|I can build a voice bot with rasa, right?|faq/voice|faq/voice|100.0%|✅|
|🟢|I could build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|When can I build a voice bot using rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|is there an alexa integration|faq/voice|faq/voice|100.0%|✅|
|🟢|what is the chance of building a rasa voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|What can a person do in the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|what can a person in Rasa do at the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|what do people do in the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|what does a person do in the Rasa forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|$1|enter_data|enter_data|100.0%|✅|
|🟢|10000 dollars|enter_data|enter_data|100.0%|✅|
|🟢|150,000$/ year|enter_data|enter_data|100.0%|✅|
|🟢|20k|enter_data|enter_data|100.0%|✅|
|🟢|50,000 dollar|enter_data|enter_data|100.0%|✅|
|🟢|75000-150000 euro|enter_data|enter_data|100.0%|✅|
|🟢|A customer service bot|enter_data|enter_data|100.0%|✅|
|🟢|I work as a project manager|enter_data|enter_data|100.0%|✅|
|🟢|I wrote it in chinese|enter_data|enter_data|100.0%|✅|
|🟢|I'm Virginia Mason|enter_data|enter_data|100.0%|✅|
|🟢|I'm an engineer|enter_data|enter_data|100.0%|✅|
|🟢|Im a full stack developer|enter_data|enter_data|100.0%|✅|
|🟢|I’ve trained it in english|enter_data|enter_data|100.0%|✅|
|🟢|I’ve trained it in spanish|enter_data|enter_data|100.0%|✅|
|🟢|My name is Shane Goodyear|enter_data|enter_data|100.0%|✅|
|🟢|No job|enter_data|enter_data|100.0%|✅|
|🟢|$1000|enter_data|enter_data|100.0%|✅|
|🟢|300 rupees|enter_data|enter_data|100.0%|✅|
|🟢|900 dollars|enter_data|enter_data|100.0%|✅|
|🟢|90k|enter_data|enter_data|100.0%|✅|
|🟢|Helvetia|enter_data|enter_data|100.0%|✅|
|🟢|dev|enter_data|enter_data|100.0%|✅|
|🟢|distances|enter_data|enter_data|100.0%|✅|
|🟢|full stack|enter_data|enter_data|100.0%|✅|
|🟢|hindi|enter_data|enter_data|100.0%|✅|
|🟢|saler|enter_data|enter_data|100.0%|✅|
|🟢|ubisoft|enter_data|enter_data|100.0%|✅|
|🟢|a chocolate bot|enter_data|enter_data|100.0%|✅|
|🟢|a turtle|enter_data|enter_data|100.0%|✅|
|🟢|all the training data was in chinese|enter_data|enter_data|100.0%|✅|
|🟢|all the training data was in italian|enter_data|enter_data|100.0%|✅|
|🟢|all the training data was in mandarin|enter_data|enter_data|100.0%|✅|
|🟢|all the training data was in spanish|enter_data|enter_data|100.0%|✅|
|🟢|bout 4,000,000 INR|enter_data|enter_data|100.0%|✅|
|🟢|how to extract relationship|enter_data|enter_data|100.0%|✅|
|🟢|head of biz deve|enter_data|enter_data|100.0%|✅|
|🟢|health care|enter_data|enter_data|100.0%|✅|
|🟢|i use chinese|enter_data|enter_data|100.0%|✅|
|🟢|i want to built a Eric Jones bot|enter_data|enter_data|100.0%|✅|
|🟢|i'm a glibber and glitter salesman|enter_data|enter_data|100.0%|✅|
|🟢|i'm in marketing|enter_data|enter_data|100.0%|✅|
|🟢|in health care domain|enter_data|enter_data|100.0%|✅|
|🟢|it's 500000000|enter_data|enter_data|100.0%|✅|
|🟢|its an portuguese bot|enter_data|enter_data|100.0%|✅|
|🟢|it’s an spanish bot|enter_data|enter_data|100.0%|✅|
|🟢|it’s only in english but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|🟢|it’s only in french but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|🟢|it’s only in italian but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained only in german|enter_data|enter_data|100.0%|✅|
|🟢|maybe then instead James@Anast.com|enter_data|enter_data|100.0%|✅|
|🟢|my function is to serve butter|enter_data|enter_data|100.0%|✅|
|🟢|my name is Earl Ring|enter_data|enter_data|100.0%|✅|
|🟢|my name is Staci Simpson|enter_data|enter_data|100.0%|✅|
|🟢|my name's Michael Peppers|enter_data|enter_data|100.0%|✅|
|🟢|my own|enter_data|enter_data|100.0%|✅|
|🟢|ok its P_Simpkins@Suehs.com|enter_data|enter_data|100.0%|✅|
|🟢|sales bot|enter_data|enter_data|100.0%|✅|
|🟢|user can communicate with the bot in english|enter_data|enter_data|100.0%|✅|
|🟢|user can communicate with the bot in italian|enter_data|enter_data|100.0%|✅|
|🟢|user can communicate with the bot in portuguese|enter_data|enter_data|100.0%|✅|
|🟢|botonic|enter_data|enter_data|100.0%|✅|
|🟢|botpress|enter_data|enter_data|100.0%|✅|
|🟢|Any good restaurants nearby?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|What might the time be?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|what"s the weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what's the weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|how can you help?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|doctor|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|expert of rasa|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|which messaging channels does rasa support?|faq/channels|faq/channels|100.0%|✅|
|🟢|What languages can be used with rasa?|faq/languages|faq/languages|100.0%|✅|
|🟢|give me the pricing|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|What to do if I want to build a voice bot using rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|150,000 USD|enter_data|enter_data|100.0%|✅|
|🟢|I wanna build a super bot to send me cute animal pictures|enter_data|enter_data|100.0%|✅|
|🟢|I work for Bayer|enter_data|enter_data|100.0%|✅|
|🟢|I work in project management|enter_data|enter_data|100.0%|✅|
|🟢|I wrote it in dutch|enter_data|enter_data|100.0%|✅|
|🟢|I’ve trained it in portuguese|enter_data|enter_data|100.0%|✅|
|🟢|The master of desaster|enter_data|enter_data|100.0%|✅|
|🟢|BBC|enter_data|enter_data|100.0%|✅|
|🟢|CSI|enter_data|enter_data|100.0%|✅|
|🟢|marketing|enter_data|enter_data|100.0%|✅|
|🟢|a sales bot|enter_data|enter_data|100.0%|✅|
|🟢|all the training data was in portuguese|enter_data|enter_data|100.0%|✅|
|🟢|customer service|enter_data|enter_data|100.0%|✅|
|🟢|its an spanish bot|enter_data|enter_data|100.0%|✅|
|🟢|it’s an english bot|enter_data|enter_data|100.0%|✅|
|🟢|it’s only in german but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|🟢|my name is Claude Ake|enter_data|enter_data|100.0%|✅|
|🟢|user can communicate with the bot in dutch|enter_data|enter_data|100.0%|✅|
|🟢|user can communicate with the bot in french|enter_data|enter_data|100.0%|✅|
|🟢|general and sales|enter_data|enter_data|100.0%|✅|
|🟢|tensorflow-text|technical_question|technical_question|100.0%|✅|
|🟢|host models|technical_question|technical_question|100.0%|✅|
|🟢|credentials.yml|technical_question|technical_question|100.0%|✅|
|🟢|How's it going|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|What's up|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how's it going?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|what's up|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|what's up?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|Hey Sara, how's it going|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|are you a robot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|you are a robot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|What languages can you use?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|Could you tell me the time, please?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|tell me the current time.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|how's the weather ?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|how's the weather?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what is the weatehr|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|How does Rasa work?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|What does rasa do exactly?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|how does RASA work?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|how does rasa work|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|how does rasa work?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what can you do, sara?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|you can hep me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|como te llamas|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|tu kaisi he|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|I am User|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|ok one then|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|the beatles|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|How to connect messaging channels to rasa?|faq/channels|faq/channels|100.0%|✅|
|🟢|Rasa supports some messaging channels, what are those?|faq/channels|faq/channels|100.0%|✅|
|🟢|How many people are in that community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|what is the main difference between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|do I need programming experience to use rasa|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|which programming languages|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|which programming language can I use?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|is Rasa available in java ?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|Building a voice bot using rasa.|faq/voice|faq/voice|100.0%|✅|
|🟢|Can I build a rasa voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|Could I build a rasa voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|How to build a voice bot using rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|What can I do to build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|can I form a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|with rasa can I form a voice bot|faq/voice|faq/voice|100.0%|✅|
|🟢|Could you please describe the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|What do people do in the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|what can people do in the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|what can people in Rasa do at the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|100k|enter_data|enter_data|100.0%|✅|
|🟢|5 mln|enter_data|enter_data|100.0%|✅|
|🟢|50,000,000 INR|enter_data|enter_data|100.0%|✅|
|🟢|My name si tom Harbin|enter_data|enter_data|100.0%|✅|
|🟢|25,000|enter_data|enter_data|100.0%|✅|
|🟢|CTO|enter_data|enter_data|100.0%|✅|
|🟢|Full Stack|enter_data|enter_data|100.0%|✅|
|🟢|Keith Donnell PhD|enter_data|enter_data|100.0%|✅|
|🟢|accenture|enter_data|enter_data|100.0%|✅|
|🟢|developer advocate|enter_data|enter_data|100.0%|✅|
|🟢|how long|enter_data|enter_data|100.0%|✅|
|🟢|a killer bot|enter_data|enter_data|100.0%|✅|
|🟢|all the training data was in german|enter_data|enter_data|100.0%|✅|
|🟢|amounts of money|enter_data|enter_data|100.0%|✅|
|🟢|don't have one|enter_data|enter_data|100.0%|✅|
|🟢|faq|enter_data|enter_data|100.0%|✅|
|🟢|im a dev|enter_data|enter_data|100.0%|✅|
|🟢|im in marketing|enter_data|enter_data|100.0%|✅|
|🟢|its an english bot|enter_data|enter_data|100.0%|✅|
|🟢|it’s available in portuguese|enter_data|enter_data|100.0%|✅|
|🟢|it’s only in spanish but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|🟢|my name is Monica Ser|enter_data|enter_data|100.0%|✅|
|🟢|pip is fine|enter_data|enter_data|100.0%|✅|
|🟢|please conda|enter_data|enter_data|100.0%|✅|
|🟢|problem solving|enter_data|enter_data|100.0%|✅|
|🟢|user can communicate with the bot in spanish|enter_data|enter_data|100.0%|✅|
|🟢|How were you built?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|I want to find some restauant nearby|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|What does Rasa make?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|so what can you do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|so what can you do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|What citizenship do you lay claim to?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|what languages do you support|faq/languages|faq/languages|100.0%|✅|
|🟢|My name is Richard smith|enter_data|enter_data|100.0%|✅|
|🟢|Im Phyllis Howard|enter_data|enter_data|100.0%|✅|
|🟢|arabic|enter_data|enter_data|100.0%|✅|
|🟢|one that flatters me every morning|enter_data|enter_data|100.0%|✅|
|🟢|software developer|enter_data|enter_data|100.0%|✅|
|🟢|language = portuguese|enter_data|enter_data|100.0%|✅|
|🟢|language: portuguese|enter_data|enter_data|100.0%|✅|
|🟢|my name is Brian Leung|enter_data|enter_data|100.0%|✅|
|🟢|the assistant speaks french|enter_data|enter_data|100.0%|✅|
|🟢|T10|enter_data|enter_data|100.0%|✅|
|🟢|technical side of things?|technical_question|technical_question|100.0%|✅|
|🟢|whatsapp|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|real bot then?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|what languages are you familiar with?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|Do you seek me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Tell me the time.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|Would you tell me what time it is?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|tell me the time.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|that's true. do you know what time it is?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|Beautiful day, isn't it?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|What's the weather forecast?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|is the sun out where you are?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|What name should I recognize for myself?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|i dont get what rasa is|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what else can I do here?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|de donde eres|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|everything|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Any integrations with WhatsApp and Facebook?|faq/channels|faq/channels|100.0%|✅|
|🟢|How does core differ to nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|which language is rasa programmed in|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|What languages can rasa support?|faq/languages|faq/languages|100.0%|✅|
|🟢|languages supported|faq/languages|faq/languages|100.0%|✅|
|🟢|Can you tell me whats the price for rasa platform?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|can you give me prices ?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Is rasa a good fit for building a voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|can I construct a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|can I use rasa to build alexa skills|faq/voice|faq/voice|100.0%|✅|
|🟢|with rasa can I construct a voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|what can be performed in the forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|whats the task of this forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|who is the forum for?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|5 bucks|enter_data|enter_data|100.0%|✅|
|🟢|50k|enter_data|enter_data|100.0%|✅|
|🟢|I am a head of business intelligence|enter_data|enter_data|100.0%|✅|
|🟢|I spend money|enter_data|enter_data|100.0%|✅|
|🟢|I wrote it in portuguese|enter_data|enter_data|100.0%|✅|
|🟢|I'm a business woman|enter_data|enter_data|100.0%|✅|
|🟢|I'm a full stack developer|enter_data|enter_data|100.0%|✅|
|🟢|200 bucks|enter_data|enter_data|100.0%|✅|
|🟢|Full stack.|enter_data|enter_data|100.0%|✅|
|🟢|K_Rainey@Yochum.net|enter_data|enter_data|100.0%|✅|
|🟢|manager|enter_data|enter_data|100.0%|✅|
|🟢|a bot to get a promotion|enter_data|enter_data|100.0%|✅|
|🟢|no idea|enter_data|enter_data|100.0%|✅|
|🟢|one bot|enter_data|enter_data|100.0%|✅|
|🟢|wordpress|enter_data|enter_data|100.0%|✅|
|🟢|I am Aniket|enter_data|enter_data|100.0%|✅|
|🟢|Sorry  it's not suleman is Shehzad|enter_data|enter_data|100.0%|✅|
|🟢|Are you a chat bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|are you robot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|Would you find any restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Could you tell me what time is it?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|what does rasa mean|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what can I do with this bot|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what else can i do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what else can i do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|Is rasa suitable to build voice bots?|faq/voice|faq/voice|100.0%|✅|
|🟢|how to add voice assitant to chat bot|faq/voice|faq/voice|100.0%|✅|
|🟢|I wrote it in french|enter_data|enter_data|100.0%|✅|
|🟢|I wrote it in italian|enter_data|enter_data|100.0%|✅|
|🟢|My budget is oov|enter_data|enter_data|100.0%|✅|
|🟢|Elise|enter_data|enter_data|100.0%|✅|
|🟢|Owner|enter_data|enter_data|100.0%|✅|
|🟢|sales manager|enter_data|enter_data|100.0%|✅|
|🟢|a great one|enter_data|enter_data|100.0%|✅|
|🟢|i'm Herbert Ball|enter_data|enter_data|100.0%|✅|
|🟢|im lonely|enter_data|enter_data|100.0%|✅|
|🟢|it’s trained in german|enter_data|enter_data|100.0%|✅|
|🟢|until now it’s only in german|enter_data|enter_data|100.0%|✅|
|🟢|£50k|enter_data|enter_data|100.0%|✅|
|🟢|server|enter_data|enter_data|100.0%|✅|
|🟢|whatchcha doing|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|can i be shown a gluten free restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Could you tell me the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|what do you know except this?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|What city were you born in?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|what are the components of rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|what are the components of RASA|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|what are the components of Rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|What are the components of Rasa?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|What are the components of rasa?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|What channels for messaging are supported by rasa?|faq/channels|faq/channels|100.0%|✅|
|🟢|what are the messaging channels that can be used with rasa?|faq/channels|faq/channels|100.0%|✅|
|🟢|Any languages that rasa supports?|faq/languages|faq/languages|100.0%|✅|
|🟢|Can rasa support any language?|faq/languages|faq/languages|100.0%|✅|
|🟢|what language would rasa use|faq/languages|faq/languages|100.0%|✅|
|🟢|Could you tell me whether rasa is open source or not?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|how do i get the open source rasa|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|How can i integrate voice in RASA CORE|faq/voice|faq/voice|100.0%|✅|
|🟢|How could I construct a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|How to build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|can I create a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|can I invent a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|with rasa can I invent a voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|what area is the forum for?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|5 quid|enter_data|enter_data|100.0%|✅|
|🟢|Scalable Minds|enter_data|enter_data|100.0%|✅|
|🟢|i'm head of sales|enter_data|enter_data|100.0%|✅|
|🟢|the language of the ai assistant is german|enter_data|enter_data|100.0%|✅|
|🟢|we plan to build a sales bot to increase our revenue by 100%.|enter_data|enter_data|100.0%|✅|
|🟢|where is rasa sdk?|technical_question|technical_question|100.0%|✅|
|🟢|Ar you a bot ?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|How many different languages are you fluent in?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|In which languages are you fluent?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|Show me the closest open restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Can you tell the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|What did my parents name me?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|WHAT IS RASA|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|What Is rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|What is Rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|What is rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what is rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what is rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what is in rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what is rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what is rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what is Rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|Do you know which messaging channels rasa supports?|faq/channels|faq/channels|100.0%|✅|
|🟢|10000000|enter_data|enter_data|100.0%|✅|
|🟢|I'm Gladys Bynum|enter_data|enter_data|100.0%|✅|
|🟢|I'm an AI researcher|enter_data|enter_data|100.0%|✅|
|🟢|My name is Kenneth Sherman|enter_data|enter_data|100.0%|✅|
|🟢|1000000|enter_data|enter_data|100.0%|✅|
|🟢|100000|enter_data|enter_data|100.0%|✅|
|🟢|120000|enter_data|enter_data|100.0%|✅|
|🟢|200000000|enter_data|enter_data|100.0%|✅|
|🟢|20000|enter_data|enter_data|100.0%|✅|
|🟢|300000|enter_data|enter_data|100.0%|✅|
|🟢|500000|enter_data|enter_data|100.0%|✅|
|🟢|50 p|enter_data|enter_data|100.0%|✅|
|🟢|6000000|enter_data|enter_data|100.0%|✅|
|🟢|BCG brazil|enter_data|enter_data|100.0%|✅|
|🟢|Kristin@yahoo.com|enter_data|enter_data|100.0%|✅|
|🟢|chinese|enter_data|enter_data|100.0%|✅|
|🟢|portuguese|enter_data|enter_data|100.0%|✅|
|🟢|a customer service support system|enter_data|enter_data|100.0%|✅|
|🟢|about 10 k|enter_data|enter_data|100.0%|✅|
|🟢|language = english|enter_data|enter_data|100.0%|✅|
|🟢|language: english|enter_data|enter_data|100.0%|✅|
|🟢|the people speak german|enter_data|enter_data|100.0%|✅|
|🟢|How were you conceived?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|are you a chatbot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|tell me, are you a bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|help me find restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|i'm looking for a Chinese restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Looks like a beautiful day hey?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what is rasa actually|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|What can you do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|What can you do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what can you do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what can you do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what you can do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what you can do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what are the messaging channels supported by rasa?|faq/channels|faq/channels|100.0%|✅|
|🟢|is support for rasa in this language?|faq/languages|faq/languages|100.0%|✅|
|🟢|what languages are supported by rasa?|faq/languages|faq/languages|100.0%|✅|
|🟢|what is pricing of rasa|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|How can I build my voice bot using rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|When is the best time to build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|can i build a voice bot|faq/voice|faq/voice|100.0%|✅|
|🟢|What is the advantage of rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|i'm a dev|enter_data|enter_data|100.0%|✅|
|🟢|we don't have one|enter_data|enter_data|100.0%|✅|
|🟢|how are you feeling|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|I need a new restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|What are the requirements for connecting messaging channel to rasa?|faq/channels|faq/channels|100.0%|✅|
|🟢|which messaging channels can I use with rasa?|faq/channels|faq/channels|100.0%|✅|
|🟢|does rasa fall into the open source software category?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Do you know how to build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|I'd like to use rasa to build a voice bot.|faq/voice|faq/voice|100.0%|✅|
|🟢|do you have voice recognition|faq/voice|faq/voice|100.0%|✅|
|🟢|0|enter_data|enter_data|100.0%|✅|
|🟢|1000|enter_data|enter_data|100.0%|✅|
|🟢|100|enter_data|enter_data|100.0%|✅|
|🟢|10|enter_data|enter_data|100.0%|✅|
|🟢|1231|enter_data|enter_data|100.0%|✅|
|🟢|12|enter_data|enter_data|100.0%|✅|
|🟢|3|enter_data|enter_data|100.0%|✅|
|🟢|5000|enter_data|enter_data|100.0%|✅|
|🟢|99|enter_data|enter_data|100.0%|✅|
|🟢|susi ai|enter_data|enter_data|100.0%|✅|
|🟢|pip|enter_data|enter_data|100.0%|✅|
|🟢|In what way were you made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|in what way were you made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|Is everything ok?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|Find me a place to eat|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Pick a restaurant for me, please|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|What's the current time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|I want to learn what rasa does|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what do you guys do at rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|What is your original location?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|german?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i´m hungry|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what language do I need to program?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|Rasa development in Java|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|What language you support?|faq/languages|faq/languages|100.0%|✅|
|🟢|so what is this forum for?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|what can I do in the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|what can you put in the forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|what do we do in the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|what is the forum in Rasa used for|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|I work for the AI research group of the turing centre of the UBC, Vancouver, Canada|enter_data|enter_data|100.0%|✅|
|🟢|I work for the New York Times|enter_data|enter_data|100.0%|✅|
|🟢|I wrote it in spanish|enter_data|enter_data|100.0%|✅|
|🟢|I'm a janitor|enter_data|enter_data|100.0%|✅|
|🟢|This is Norma Taylor|enter_data|enter_data|100.0%|✅|
|🟢|SAP|enter_data|enter_data|100.0%|✅|
|🟢|german|enter_data|out_of_scope/other|100.0%|❌|
|🟢|mail: Geneva.Favors@yahoo.com|enter_data|enter_data|100.0%|✅|
|🟢|pip please|enter_data|enter_data|100.0%|✅|
|🟢|locally|enter_data|enter_data|100.0%|✅|
|🟢|hello, how are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|What's the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|what's the time|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|Will I require my raincoat today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|tell me more about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|What messaging channels are supported by rasa?|faq/channels|faq/channels|100.0%|✅|
|🟢|Do you know the difference between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what differences exist between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|how mush does rasa cost|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|would rasa fall into the category of open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|can I make a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|with rasa can I make a voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|botium|enter_data|enter_data|100.0%|✅|
|🟢|my email is Virginia@Brown.com|enter_data|enter_data|100.0%|✅|
|🟢|we plan with 250.000 euro for one year|enter_data|enter_data|100.0%|✅|
|🟢|Can you give me an idea as to how you were created?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|How were you constructed?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|how are yuo|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how old were you when you celebrated your last birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|are you real lol|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|What is the current time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|what is the current time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|what is the temperature|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|Please let me know what my name is|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|Where are your roots?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|how can i integrate the rasa chat bot to my website|faq/channels|faq/channels|100.0%|✅|
|🟢|How do I do the programming?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|what language supported by rasa?|faq/languages|faq/languages|100.0%|✅|
|🟢|400 trilion|enter_data|enter_data|100.0%|✅|
|🟢|I work for the new york times|enter_data|enter_data|100.0%|✅|
|🟢|I'm a python developer|enter_data|enter_data|100.0%|✅|
|🟢|db processing|technical_question|technical_question|100.0%|✅|
|🟢|actions|technical_question|technical_question|100.0%|✅|
|🟢|what is an intemt|technical_question|technical_question|100.0%|✅|
|🟢|you're a bot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|whar are the components of rasa?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|Building a rasa voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|I work in innovation|enter_data|enter_data|100.0%|✅|
|🟢|Robert.Sparks@gmail.com|enter_data|enter_data|100.0%|✅|
|🟢|Zendesk|enter_data|enter_data|100.0%|✅|
|🟢|italian|enter_data|enter_data|100.0%|✅|
|🟢|how to use forms|technical_question|technical_question|100.0%|✅|
|🟢|What's a good place to eat nearby|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Excuse me, what time is it?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|whats the time now|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|epdi iruka|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|what the different with rasa nlu and rasa core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|you have to be a good programmer|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|What languages can rasa use?|faq/languages|faq/languages|100.0%|✅|
|🟢|which languages do you support|faq/languages|faq/languages|100.0%|✅|
|🟢|how do i build a voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|why should I join the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|language = italian|enter_data|enter_data|100.0%|✅|
|🟢|language: italian|enter_data|enter_data|100.0%|✅|
|🟢|my bot is in german|enter_data|enter_data|100.0%|✅|
|🟢|Hi Sara! How are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|hi sara, how are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|How old will you be on your next birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|Weather?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|weather?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|How large roughly speaking is the Rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|can rasa support this language?|faq/languages|faq/languages|100.0%|✅|
|🟢|i want to build a voice bot|faq/voice|faq/voice|100.0%|✅|
|🟢|I wrote it in english|enter_data|enter_data|100.0%|✅|
|🟢|I'm Harvey Cordano|enter_data|enter_data|100.0%|✅|
|🟢|what is a synonym called?|technical_question|technical_question|100.0%|✅|
|🟢|installation of tensorflow-text|technical_question|technical_question|100.0%|✅|
|🟢|What is COnvert?|technical_question|technical_question|100.0%|✅|
|🟢|How exactly were you made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|so how were you made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|tell me your age number?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|what languages you can handle well?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|What's the closest restaurant open near me|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|What is the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|do you know the current time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|what is the time ?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|what is the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|I want to learn what rasa is|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|yeah go on explaining what rasa is|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what can we talk about?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what chat channels does rasa uses|faq/channels|faq/channels|100.0%|✅|
|🟢|which particular messaging channels are supported by rasa?|faq/channels|faq/channels|100.0%|✅|
|🟢|what is the difference between nlu and rasa core|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what would you say the difference is between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|Which languages are supported by rasa?|faq/languages|faq/languages|100.0%|✅|
|🟢|does rasa use open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|what exactly is the forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|i'd like to build a transformer|enter_data|enter_data|100.0%|✅|
|🟢|knowledge base action|technical_question|technical_question|100.0%|✅|
|🟢|How's life treating you friend?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|what number represents your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|what is the primary difference between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what different languages does rasa support|faq/languages|faq/languages|100.0%|✅|
|🟢|I'm the boss|enter_data|enter_data|100.0%|✅|
|🟢|i want a great bot to impress my boss|enter_data|enter_data|100.0%|✅|
|🟢|education bot|enter_data|enter_data|100.0%|✅|
|🟢|credentials|technical_question|technical_question|100.0%|✅|
|🟢|How was your day?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how are you doing|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how are you doing?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how is your evening|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|What restaurant would you recommend for dinner?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|what can I ask ?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|Dumme sara|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|which kind|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|even non latin based languages?|faq/languages|faq/languages|100.0%|✅|
|🟢|What are the rules of the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|whats in the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|10 m|enter_data|enter_data|100.0%|✅|
|🟢|have no idea|enter_data|enter_data|100.0%|✅|
|🟢|there is no budget|enter_data|enter_data|100.0%|✅|
|🟢|we're building a conversational assistant for our employees to book meeting rooms.|enter_data|enter_data|100.0%|✅|
|🟢|python sdk|technical_question|technical_question|100.0%|✅|
|🟢|Which languages are you familiar with?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|How do core and nlu conflict?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|do you have a list of languages rasa supports|faq/languages|faq/languages|100.0%|✅|
|🟢|I would like to know the cost first.|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|what is the forum used for?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|We plan to build a sales bot to increase our sales by 500%.|enter_data|enter_data|100.0%|✅|
|🟢|Ten|enter_data|enter_data|100.0%|✅|
|🟢|How were you made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|What process was used to build you?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|how were you made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|How are you today?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how are you today|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|How many languages do you know?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|how many languages do you know?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|I'm looking for a Spanish restaurant.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|What is the exact time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|What can you demo|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|Around where are you from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|Nice name|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|How few members in the community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|Can I use Rasa with Thai language|faq/languages|faq/languages|100.0%|✅|
|🟢|What languages can rasa be relied upon to support?|faq/languages|faq/languages|100.0%|✅|
|🟢|Which languages can be used by rasa?|faq/languages|faq/languages|100.0%|✅|
|🟢|which languages supports rasa|faq/languages|faq/languages|100.0%|✅|
|🟢|would rasa be open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Could you please give me a description of the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|what can be done in the forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|A wolf bot|enter_data|enter_data|100.0%|✅|
|🟢|sdk|technical_question|technical_question|100.0%|✅|
|🟢|How many years have you been alive?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|developer|enter_data|enter_data|100.0%|✅|
|🟢|a bot which sends cute shiba pictures|enter_data|enter_data|100.0%|✅|
|🟢|Can you explain how you were created?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|I want to know how you were formed|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|I'd like to know how you were created|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|Do you know the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|What is rasa doing exactly?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|rasa topics|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|try out the playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|do you know what language rasa uses|faq/languages|faq/languages|100.0%|✅|
|🟢|which version of python do i need|faq/python_version|faq/python_version|100.0%|✅|
|🟢|Can one make a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|🟢|I want to build a kick ass bot|enter_data|enter_data|100.0%|✅|
|🟢|SCALABLE MINDS|enter_data|enter_data|100.0%|✅|
|🟢|Developer|enter_data|enter_data|100.0%|✅|
|🟢|one that will get me promoted|enter_data|enter_data|100.0%|✅|
|🟢|the language is german|enter_data|enter_data|100.0%|✅|
|🟢|ConveRTFeaturizer|technical_question|technical_question|100.0%|✅|
|🟢|which python libraries are used|technical_question|technical_question|100.0%|✅|
|🟢|you are chatbot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|IS there any near by restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|would you consider rasa open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|In what manner were you built?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|what language do you use|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|will you see any restaurant for me?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|wheather at you location?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|Inform me what my name is|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|What do my colleagues call me?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|what can you answer|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|sing me a song|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|can give tell me about components of Rosa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|my email is Kelly@Coulter.net|enter_data|enter_data|100.0%|✅|
|🟢|what is significance of domain.yml file|technical_question|technical_question|100.0%|✅|
|🟢|Help me with finding this restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|so what exactly is the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|designer|enter_data|enter_data|100.0%|✅|
|🟢|whatsapp bro|technical_question|technical_question|100.0%|✅|
|🟢|Let me know how you were made exactly|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|oh are you chatbot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|i want to know about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|What can I ask you?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what can I ask you?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|你是谁|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|which messaging channels are supported by rasa?|faq/channels|faq/channels|100.0%|✅|
|🟢|In what ways are core and nlu unalike?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what programming knowledge do I need to learn?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|Which languages can I use with rasa?|faq/languages|faq/languages|100.0%|✅|
|🟢|what is the enterprise pricing schedule?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|What is the scope of the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|I want to build a bot that can substitute our entire workforce|enter_data|enter_data|100.0%|✅|
|🟢|im a freelancer|enter_data|enter_data|100.0%|✅|
|🟢|our estimation is 10k|enter_data|enter_data|100.0%|✅|
|🟢|there are some python incompatibilities|technical_question|technical_question|100.0%|✅|
|🟢|How do core and nlu differ?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|How does nlu contrast to core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|Is rasa any good for building a voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|What happens in the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|what are the events?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|how to set threshold ?|technical_question|technical_question|100.0%|✅|
|🟢|how are xou|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|How long have you been alive?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|Have you seen me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|Will the skies be clear today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|I need some help|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|help me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|mountain|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|How many individuals reside in your community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|need to use portuguese|faq/languages|faq/languages|100.0%|✅|
|🟢|I'd like to build a voice bot with rasa.|faq/voice|faq/voice|100.0%|✅|
|🟢|what is a Rasa forum for?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|what is helm|technical_question|technical_question|100.0%|✅|
|🟢|can tell me about rasa_sdk|technical_question|technical_question|100.0%|✅|
|🟢|What is DIET|technical_question|technical_question|100.0%|✅|
|🟢|show me the menu|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what channels does rasa support|faq/channels|faq/channels|100.0%|✅|
|🟢|What channels does Rasa support?|faq/channels|faq/channels|100.0%|✅|
|🟢|which languages are supported?|faq/languages|faq/languages|100.0%|✅|
|🟢|which python version|faq/python_version|faq/python_version|100.0%|✅|
|🟢|ok I'm actually an engineer|enter_data|enter_data|100.0%|✅|
|🟢|is this test compatible with linux?|technical_question|technical_question|100.0%|✅|
|🟢|Hey, can you help me with locating this restaurant.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|I need help|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|i need help|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|Where were you at before you were here?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|chgfhgh|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Which specific languages does rasa support?|faq/languages|faq/languages|100.0%|✅|
|🟢|how many natural language that rasa supported?|faq/languages|faq/languages|100.0%|✅|
|🟢|does rasa support other language beside english?|faq/languages|faq/languages|100.0%|✅|
|🟢|I would like to build an ice cube dispenser bot|enter_data|enter_data|100.0%|✅|
|🟢|e commerce bot|enter_data|enter_data|100.0%|✅|
|🟢|I'm interested in local installation|enter_data|enter_data|100.0%|✅|
|🟢|How did they build you?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|Do you speak italian?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|tell me the time it is.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|Can you tell me more about rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|I want to know what rasa actually does that isn't clear to me yet|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|What exactly is Rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|What is the RASA Stack?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|i havent understood yet what rasa actually is|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what can I do with Sara?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|What country were you born in?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|more info on components of rasa pls|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|is it available in Spanish?|faq/languages|faq/languages|100.0%|✅|
|🟢|what about languages supported in rasa?|faq/languages|faq/languages|100.0%|✅|
|🟢|Which python version should I install to run Rasa example?|faq/python_version|faq/python_version|100.0%|✅|
|🟢|what does on-premise mean?|technical_question|technical_question|100.0%|✅|
|🟢|whats your birth year?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|Do you know other languages?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|how can we keep buttons to get slots|faq/slots|faq/slots|100.0%|✅|
|🟢|english|enter_data|enter_data|100.0%|✅|
|🟢|i'm in sales|enter_data|enter_data|100.0%|✅|
|🟢|how do you retrieve previous messages|technical_question|technical_question|100.0%|✅|
|🟢|websocket|technical_question|technical_question|100.0%|✅|
|🟢|Are you built using rasa?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|what can i do here|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|i need a help to integrate rasa with a messenger|faq/channels|faq/channels|100.0%|✅|
|🟢|Which different languages does rasa support?|faq/languages|faq/languages|100.0%|✅|
|🟢|Tell me how you were made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|whats the temperature|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|extracting durations|enter_data|enter_data|100.0%|✅|
|🟢|ok it's Hee@yahoo.com|enter_data|enter_data|100.0%|✅|
|🟢|help pls|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|where are your parents from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|rasa codigo abierto|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|what do i need for programming?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|What language u support?|faq/languages|faq/languages|100.0%|✅|
|🟢|What is included in rasa open source edition?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Rasa voice bot building.|faq/voice|faq/voice|100.0%|✅|
|🟢|what are the events for China?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|how cna i get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|What time is it right now?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|how cost to install Rasa?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|whats int he forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|how to use flask?|technical_question|technical_question|100.0%|✅|
|🟢|i want a french restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|What does core offer that nlu does not?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|nlu part|enter_data|enter_data|100.0%|✅|
|🟢|Do you know any other languages?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|Today|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|How to build a voice bot?|faq/voice|faq/voice|100.0%|✅|
|🟢|Country names|enter_data|enter_data|100.0%|✅|
|🟢|I want to build a lot of different bots|enter_data|enter_data|100.0%|✅|
|🟢|it’s available in german|enter_data|enter_data|100.0%|✅|
|🟢|my job function is developer|enter_data|enter_data|100.0%|✅|
|🟢|How many languages do you have knowledge of?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|Do you know what time it is?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|Nice day out today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|on what channels can I use rasa|faq/channels|faq/channels|100.0%|✅|
|🟢|does rasa support any languages?|faq/languages|faq/languages|100.0%|✅|
|🟢|is there anything specific to be done in this forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|$0.00|enter_data|enter_data|100.0%|✅|
|🟢|oov|enter_data|enter_data|100.0%|✅|
|🟢|oov per year|enter_data|enter_data|100.0%|✅|
|🟢|Does rasa support different languages|faq/languages|faq/languages|100.0%|✅|
|🟢|what community events are there?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|Lithuanian|enter_data|enter_data|100.0%|✅|
|🟢|How's it hanging?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|que puedes hacer?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|what channels do you support?|faq/channels|faq/channels|100.0%|✅|
|🟢|Please define the word slots for me.|faq/slots|faq/slots|100.0%|✅|
|🟢|what is the Rasa forum used for|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|action_restart in rasa|technical_question|technical_question|100.0%|✅|
|🟢|replace default nlu with custom component|technical_question|technical_question|100.0%|✅|
|🟢|how do i sstart|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|What's up man|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how are you doing this morning|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|What is your heritage?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|j  bhbhj|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|My name is Lee George|enter_data|enter_data|100.0%|✅|
|🟢|intel|enter_data|enter_data|100.0%|✅|
|🟢|operations|enter_data|enter_data|100.0%|✅|
|🟢|what is the latest version of rasa?|technical_question|technical_question|100.0%|✅|
|🟢|rasa shell|technical_question|technical_question|100.0%|✅|
|🟢|How many individuals are in your community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|would an example of open source software be rasa?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|I'm a real good engineer|enter_data|enter_data|100.0%|✅|
|🟢|how much money|enter_data|enter_data|100.0%|✅|
|🟢|are you ai|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|you are ai|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|こにちは|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|what can I post in the forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|it’s in german|enter_data|enter_data|100.0%|✅|
|🟢|what is the knowledge base server|technical_question|technical_question|100.0%|✅|
|🟢|no budget, that why i looking for open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Not sure what slots are.|faq/slots|faq/slots|100.0%|✅|
|🟢|Not sure what slots are?|faq/slots|faq/slots|100.0%|✅|
|🟢|What are the events now?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|booking a sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|ACME bank|enter_data|enter_data|100.0%|✅|
|🟢|how do i get started with rasa myself?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Can you give me the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|what are Rasa's components|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|What are Rasa's components?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|difference between Rasa and Rasa X|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|can I use rasa also for another laguage?|faq/languages|faq/languages|100.0%|✅|
|🟢|language support|faq/languages|faq/languages|100.0%|✅|
|🟢|what about slots|faq/slots|faq/slots|100.0%|✅|
|🟢|I'm in business|enter_data|enter_data|100.0%|✅|
|🟢|on that will get me promoted|enter_data|enter_data|100.0%|✅|
|🟢|dialogueflow|enter_data|enter_data|100.0%|✅|
|🟢|i am a new user|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|RASA sdk|technical_question|technical_question|100.0%|✅|
|🟢|Do you know how big the Rasa community is?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|i have never programed before|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|what is the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|What kinds of events are happening here?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|talk to sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|Able to integrate with paypal, wordpress, facebook andd twilio|enter_data|enter_data|100.0%|✅|
|🟢|we are a covert government organisation|enter_data|enter_data|100.0%|✅|
|🟢|Hot to get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|what is a webhook|technical_question|technical_question|100.0%|✅|
|🟢|What's going on?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|Do you speak german?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|do you speak german?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|i want to about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|DIFFERENCES BETWEEN CORE AND NLU|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what kind of events are there?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|how do i get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|there is error|technical_question|technical_question|100.0%|✅|
|🟢|are you a rasa bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|what can you teache me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|does mongodb works for rasax|technical_question|technical_question|100.0%|✅|
|🟢|could you elaborate more about rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|how do I get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|How exactly were you devised?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|What process was used to create you?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|What was the process for making you?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|Ahoy matey how are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|How you help me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|how you help me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|What are the specific languages that rasa is intended to work with?|faq/languages|faq/languages|100.0%|✅|
|🟢|so what exactly are these events?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|What are the events for Detroit?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|contact call with sales|contact_sales|contact_sales|100.0%|✅|
|🟢|clue|enter_data|enter_data|100.0%|✅|
|🟢|Whats your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|whats your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|google?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What are the events for New York?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|what are the events for berlin?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|dutch|enter_data|enter_data|100.0%|✅|
|🟢|Recharge|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|dinner|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Is rasa support message channels?|faq/channels|faq/channels|100.0%|✅|
|🟢|tell me about the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|[Mr. Sweney](name)|enter_data|enter_data|100.0%|✅|
|🟢|i'd like to build sentient glibber or glitter|enter_data|enter_data|100.0%|✅|
|🟢|can you speak in italian?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|What does Rasa build?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|How do you define the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|what is fallback policy in rasa|technical_question|technical_question|100.0%|✅|
|🟢|rasa sdk|technical_question|technical_question|100.0%|✅|
|🟢|fallback actions|technical_question|technical_question|100.0%|✅|
|🟢|How are You?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|How are you|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|How are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how are you|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how are you ?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how are you'|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how are you????|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how r u|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how r u ?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how r u>|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|I need a restaurant.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|tell me about Rasa Playground please|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|How large is the Rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|Founder|enter_data|enter_data|100.0%|✅|
|🟢|like 60 quid|enter_data|enter_data|100.0%|✅|
|🟢|hi how are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|How can you help me find a restaurant.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|what is the last version of rasa core?|technical_question|technical_question|100.0%|✅|
|🟢|are you really a bbot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|difference between rasa and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|booking sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|language = french|enter_data|enter_data|100.0%|✅|
|🟢|language: french|enter_data|enter_data|100.0%|✅|
|🟢|In what manner were you constructed?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|I want to add Romanian language support|faq/languages|faq/languages|100.0%|✅|
|🟢|What types of events are planned?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|What are the events in Detroit?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|what are the events in berlin?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|What's the next community event|ask_which_events|ask_which_events|100.0%|✅|
|🟢|user can talk to my bot in german|enter_data|enter_data|100.0%|✅|
|🟢|how do I get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|what is the wather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|help please|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|Where do you live?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|where do you live|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|where do you live?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|colder|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|try rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|What communication channels does rasa support?|faq/channels|faq/channels|100.0%|✅|
|🟢|do you know of the languages rasa supports|faq/languages|faq/languages|100.0%|✅|
|🟢|which language supports rasa|faq/languages|faq/languages|100.0%|✅|
|🟢|would people consider rasa an open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|An ice cube bot|enter_data|enter_data|100.0%|✅|
|🟢|how much is Rasa stack?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|which python version should i install|faq/python_version|faq/python_version|100.0%|✅|
|🟢|10k|enter_data|enter_data|100.0%|✅|
|🟢|none i will build it from scraps|enter_data|enter_data|100.0%|✅|
|🟢|im a new to rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|How are you men?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|Tell me your day, month and year of birth.|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|You were conceived in what location?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|what are the primary areas of difference between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|Is rasa forum reliable?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|hiii|greet|greet|100.0%|✅|
|🟢|When are the events in Paris?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|what are the events in Berlin?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|contact to sales|contact_sales|contact_sales|100.0%|✅|
|🟢|rasa-core error|technical_question|technical_question|100.0%|✅|
|🟢|weatger|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|i want to learn more about Rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|hellooo|greet|greet|100.0%|✅|
|🟢|What's the next rasa event|ask_which_events|ask_which_events|100.0%|✅|
|🟢|response selector?|technical_question|technical_question|100.0%|✅|
|🟢|are you multilingual?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|how many languages are you fluent in?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|What country are you from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|what country are you from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|is it free|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|is it free?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|What's the slots?|faq/slots|faq/slots|100.0%|✅|
|🟢|language = spanish|enter_data|enter_data|100.0%|✅|
|🟢|language: spanish|enter_data|enter_data|100.0%|✅|
|🟢|How do I get started with Rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|tell me how i can get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|In what way were you created?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|what is rasa cost ?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|List the characteristics of rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|what is the Rasa forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|What events are there?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|I'm a bot developer|enter_data|enter_data|100.0%|✅|
|🟢|I'm a bot developer|enter_data|enter_data|100.0%|✅|
|🟢|you robo|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|I would like to know about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|which messaging channels can be used with rasa?|faq/channels|faq/channels|100.0%|✅|
|🟢|what is the forum about|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|can u teach me|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Is there a Rasa event in San Francisco|ask_which_events|ask_which_events|100.0%|✅|
|🟢|how can i get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|ok i am new to Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|lunch|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|lunch??|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what do you think slots are?|faq/slots|faq/slots|100.0%|✅|
|🟢|What are the events available?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|get strarted with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Does it have a java library|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|helloooo|greet|greet|100.0%|✅|
|🟢|i want to build all the bots|enter_data|enter_data|100.0%|✅|
|🟢|How many candles were on your last birthday cake?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|what else do you know besides English?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|What is the magnitude of the Rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|which language do you support?|faq/languages|faq/languages|100.0%|✅|
|🟢|When are the events in paris?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|booking sales ca;;|contact_sales|contact_sales|100.0%|✅|
|🟢|Is there a technical paper about DIET?|technical_question|technical_question|100.0%|✅|
|🟢|In what way were you shaped?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|what lanquages do you support|faq/languages|faq/languages|100.0%|✅|
|🟢|I want to build a sales bot|enter_data|enter_data|100.0%|✅|
|🟢|Tell me how to get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|options|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|¿Qué pasa?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|i want to integrate my rasa bot to webex  may i know how|faq/channels|faq/channels|100.0%|✅|
|🟢|What are the events in Switzerland?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|do you have docker image for rasa?|technical_question|technical_question|100.0%|✅|
|🟢|So where are you from|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|so what events are there?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|How can I get started with rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|You originated through what means?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|Do you feel good?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|are you alright|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|which language can I use with rasa?|faq/languages|faq/languages|100.0%|✅|
|🟢|sales pl|contact_sales|contact_sales|100.0%|✅|
|🟢|get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|does rasa support prestashop?|technical_question|technical_question|100.0%|✅|
|🟢|i am having trouble setting this up|technical_question|technical_question|100.0%|✅|
|🟢|HELLO|greet|greet|100.0%|✅|
|🟢|the bot speaks german|enter_data|enter_data|100.0%|✅|
|🟢|how to build stories|technical_question|technical_question|100.0%|✅|
|🟢|tell me about rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|what is slots|faq/slots|faq/slots|100.0%|✅|
|🟢|will there be an event in my city?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|i want to build a health bot|enter_data|enter_data|100.0%|✅|
|🟢|get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|I need to know what time it is.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|what is price?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|What kinds of events do you host here?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|what sort of social events are we throwing?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|contact sales|contact_sales|contact_sales|100.0%|✅|
|🟢|please connect me to sales|contact_sales|contact_sales|100.0%|✅|
|🟢|how can I get a docker image|technical_question|technical_question|100.0%|✅|
|🟢|i don't know what i want|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|where are you from|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|where are you from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|please tell me more about rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|What languages does rasa work for?|faq/languages|faq/languages|100.0%|✅|
|🟢|what do you mean by slots?|faq/slots|faq/slots|100.0%|✅|
|🟢|i want to make intelligence chatbot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Can I use Rasa for E-Mail|technical_question|technical_question|100.0%|✅|
|🟢|how are u|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how are u?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|Which version of Python to install?|faq/python_version|faq/python_version|100.0%|✅|
|🟢|buttons|technical_question|technical_question|100.0%|✅|
|🟢|Can you tell me about rasa playground?|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|What is the definition of slots|faq/slots|faq/slots|100.0%|✅|
|🟢|a cool boy|enter_data|enter_data|100.0%|✅|
|🟢|hello|greet|greet|100.0%|✅|
|🟢|hello?|greet|greet|100.0%|✅|
|🟢|hello]|greet|greet|100.0%|✅|
|🟢|how can i get started with Rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|How massive is the Rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|what are the languages that is supported by rasa?|faq/languages|faq/languages|100.0%|✅|
|🟢|do you know what slots are?|faq/slots|faq/slots|100.0%|✅|
|🟢|where did you spend your youth?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|heeey|greet|greet|100.0%|✅|
|🟢|i choose the call with sales|contact_sales|contact_sales|100.0%|✅|
|🟢|What is the min requirements to run rasa|technical_question|technical_question|100.0%|✅|
|🟢|fallback|technical_question|technical_question|100.0%|✅|
|🟢|tell me what time you have.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|Explain my name to me.|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|What would be the name on my tombstone?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|Shall i know who am i?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|what are the components?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|how can i integrate rasa in my siteweb ?|faq/channels|faq/channels|100.0%|✅|
|🟢|what is the price of rasa|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|helleo|greet|greet|100.0%|✅|
|🟢|sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|Subscribe me to you newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|heyo|greet|greet|100.0%|✅|
|🟢|connect to sales|contact_sales|contact_sales|100.0%|✅|
|🟢|request sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|how to get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to get started with rasa ?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|what is endpoint|technical_question|technical_question|100.0%|✅|
|🟢|how's life been treating you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|can you tell me what languages rasa supports|faq/languages|faq/languages|100.0%|✅|
|🟢|I bet you can tell me all about slots.|faq/slots|faq/slots|100.0%|✅|
|🟢|sales contact|contact_sales|contact_sales|100.0%|✅|
|🟢|sales department|contact_sales|contact_sales|100.0%|✅|
|🟢|the assistant speaks german|enter_data|enter_data|100.0%|✅|
|🟢|i am new to rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Sign me up for the newsletter.|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Create ecommerce bot|technical_question|technical_question|100.0%|✅|
|🟢|Could you tell me more about Rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|could you tell me more about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|Where did you grow up?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|where did you grow up?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|more information on components in rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|What is the cost of RASA?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|What is the meaning of the word slots?|faq/slots|faq/slots|100.0%|✅|
|🟢|company: uber|enter_data|enter_data|100.0%|✅|
|🟢|how to get the metadata file|technical_question|technical_question|100.0%|✅|
|🟢|Can you communicate in any other languages?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|como estas|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|tell me about the components|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|List the dissimilar qualities of core and nlu|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|HEllo|greet|greet|100.0%|✅|
|🟢|What are all of the events you have?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|are you rasa bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|Do you have the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|do you have the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|what is time is US ?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|Can rasa do calculations?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|so... i trying to deploy my rasa bot on|faq/channels|faq/channels|100.0%|✅|
|🟢|When is the next community event?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|When will the next event occur in the community?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|when will the next community event be?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|please sign me up for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|tell me about slots|faq/slots|faq/slots|100.0%|✅|
|🟢|create chatbot steps|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|How far does the Rasa community spread?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|IBM|enter_data|enter_data|100.0%|✅|
|🟢|How can I get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|How can I get started with Rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|license|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|what languages does rasa support?|faq/languages|faq/languages|100.0%|✅|
|🟢|What kinds of events are scheduled?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|I want a sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|i want a sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|the difference between Rasa and Rasa X|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|HOW CAN I BOOK A SALES CALL ?|contact_sales|contact_sales|100.0%|✅|
|🟢|interactive playground|enter_data|enter_data|100.0%|✅|
|🟢|I want to implement rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|What do I Need for Rasa implementation?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to add dropdowns?|technical_question|technical_question|100.0%|✅|
|🟢|what the wheather like?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|yes i accept|affirm|affirm|100.0%|✅|
|🟢|Does Rasa host any events?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|what events will there be?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|i want to have a call with sales|contact_sales|contact_sales|100.0%|✅|
|🟢|request call with sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|picking my nose|enter_data|enter_data|100.0%|✅|
|🟢|do i need to know how to program to create a bot?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|hell9o|greet|greet|100.0%|✅|
|🟢|When does the upcoming event occur?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|connect to the sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|how to book a sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|how to book a sales call>|contact_sales|contact_sales|100.0%|✅|
|🟢|how to book a sales call?|contact_sales|contact_sales|100.0%|✅|
|🟢|the assistant is in german|enter_data|enter_data|100.0%|✅|
|🟢|how do i get started with rasa nlu|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|a chatbot for mops - mopbot|enter_data|enter_data|100.0%|✅|
|🟢|but please sign me up for the newsletter!|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|sign up to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|I want to speak binary with you|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|cool! can I do something else here?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what you talk about?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|Where do you come from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|where do you come from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|J_Herrera@gmail.com|enter_data|enter_data|100.0%|✅|
|🟢|Can you tell me what Rasa does?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|which are the topics covered in this forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|Hei|greet|greet|100.0%|✅|
|🟢|what events are there going to be?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|connect me to your sales department|contact_sales|contact_sales|100.0%|✅|
|🟢|i'd like to call Johnnie Essig|contact_sales|contact_sales|100.0%|✅|
|🟢|a voice bot|enter_data|enter_data|100.0%|✅|
|🟢|the bot should help with HR stuff|enter_data|enter_data|100.0%|✅|
|🟢|rasa templates|technical_question|technical_question|100.0%|✅|
|🟢|are you happy|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|How did rasa works?|technical_question|technical_question|100.0%|✅|
|🟢|how to connect mongodb|technical_question|technical_question|100.0%|✅|
|🟢|book a sale call|contact_sales|contact_sales|100.0%|✅|
|🟢|Please tell me how to get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Please install Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|🟢|Are we in for a scorcher?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|You can tell me info on slots.|faq/slots|faq/slots|100.0%|✅|
|🟢|how do slots work|faq/slots|faq/slots|100.0%|✅|
|🟢|helo|greet|greet|100.0%|✅|
|🟢|Which community events do you have|ask_which_events|ask_which_events|100.0%|✅|
|🟢|can you subscribe me to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|How big is the Rasa community|faq/community_size|faq/community_size|100.0%|✅|
|🟢|How big is the Rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|how to get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to get started with Rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|training model?|technical_question|technical_question|100.0%|✅|
|🟢|How were you devised?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|the components of Rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|the components of rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|The components of Rasa?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|subscribe me to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|is slot teh same as entity|technical_question|technical_question|100.0%|✅|
|🟢|How do I discover who I am?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|How do I discover who am I?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|tell me what is rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|What lanquages do you serve|faq/languages|faq/languages|100.0%|✅|
|🟢|what are the names of all the events?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|use of stories files|technical_question|technical_question|100.0%|✅|
|🟢|What is my first name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|Can you tell me who I am?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|Can you tell me who am I?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|can you tell me who I am?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|I need to know about Rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|iwant booking sales|contact_sales|contact_sales|100.0%|✅|
|🟢|can you sign me up for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|call sales|contact_sales|contact_sales|100.0%|✅|
|🟢|can i talk to your disagreeable sales man?|contact_sales|contact_sales|100.0%|✅|
|🟢|big old bot|enter_data|enter_data|100.0%|✅|
|🟢|do RASA has sdk to develop bot|technical_question|technical_question|100.0%|✅|
|🟢|what time is it|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|what time is it?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|what time it is|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|anything els|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|which UI channel is used by Rasa ?|faq/channels|faq/channels|100.0%|✅|
|🟢|languages|faq/languages|faq/languages|100.0%|✅|
|🟢|I want to contact sales|contact_sales|contact_sales|100.0%|✅|
|🟢|book sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|how to build chatbot using rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|hey sara|greet|greet|100.0%|✅|
|🟢|hey, sara!|greet|greet|100.0%|✅|
|🟢|what date is the next community event?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|book a sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|lets talk to sales|contact_sales|contact_sales|100.0%|✅|
|🟢|are you okay|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|Hello|greet|greet|100.0%|✅|
|🟢|Hello!|greet|greet|100.0%|✅|
|🟢|hw to get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|i want to join the newsletter list|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|subscribe me to newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Did you know the size of rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|I want to learn more about the pricing|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|i need a call from sales|contact_sales|contact_sales|100.0%|✅|
|🟢|i want to bookk a sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|let me talk to your sales guys|contact_sales|contact_sales|100.0%|✅|
|🟢|i want to get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|ow to get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|i need the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|subscribe to newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|What is the purpose of the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|heya|greet|greet|100.0%|✅|
|🟢|merhaba|greet|greet|100.0%|✅|
|🟢|sign up for newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|How were you formed?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|i guess you are a chatbot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|what is time is USA ?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|tell me about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|How large is the community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|When are the events for Paris?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|How to get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|How to get started with Rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|sign up newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Do you understand spanish?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|which languages does rasa support|faq/languages|faq/languages|100.0%|✅|
|🟢|i want ti booking about booking sales|contact_sales|contact_sales|100.0%|✅|
|🟢|slack|enter_data|enter_data|100.0%|✅|
|🟢|how to visualise dialogue flow|technical_question|technical_question|100.0%|✅|
|🟢|when is your birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|how's weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what can you offer me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|can you tell me prices|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|contact sales for me|contact_sales|contact_sales|100.0%|✅|
|🟢|let me talk to sales|contact_sales|contact_sales|100.0%|✅|
|🟢|whats tensorflow|technical_question|technical_question|100.0%|✅|
|🟢|i want to contact sales|contact_sales|contact_sales|100.0%|✅|
|🟢|subscribe to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|ok quick question here do i download this api|technical_question|technical_question|100.0%|✅|
|🟢|How've you been?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|Hi, I need the time.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|what is playground ?|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|hii|greet|greet|100.0%|✅|
|🟢|i need this dope newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Subscription cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|book a call|contact_sales|contact_sales|100.0%|✅|
|🟢|Do you know where you come from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|Tell me who I am.|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|Tell me who I am?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|Tell me who am I?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|tell me who I am?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|Do you know about rasa supporting channels?|faq/channels|faq/channels|100.0%|✅|
|🟢|yes, where I can find some hand-on tutorials to use RASA products?|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|What is the next event in san francisco?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|Now?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Tell me about rasa playgrounds|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|When are the events for paris?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|what is time in US ?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|refresh|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i want to contact sales now|contact_sales|contact_sales|100.0%|✅|
|🟢|lets do the newsletter signup|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|What channels of communication does rasa support?|faq/channels|faq/channels|100.0%|✅|
|🟢|newslettwr|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|sign up for the NL|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|How can i automate retraining of my rasa models|technical_question|technical_question|100.0%|✅|
|🟢|how's life|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|next the sales contact|contact_sales|contact_sales|100.0%|✅|
|🟢|it’s an german bot|enter_data|enter_data|100.0%|✅|
|🟢|do you speak dutch?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|卧槽|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|I said, helllllloooooO!!!!|greet|greet|100.0%|✅|
|🟢|having trouble with rasa installation|technical_question|technical_question|100.0%|✅|
|🟢|Let me install Rasa Stack.|install_rasa|install_rasa|100.0%|✅|
|🟢|Subscribe newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|now i want to signup for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|do you take voice input?|faq/voice|faq/voice|100.0%|✅|
|🟢|when is the next community event gonna be?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|register me for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|nah, I'm good - how are you doing?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|呵呵|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|I need help to make rasa in java|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|install rasa stack|install_rasa|install_rasa|100.0%|✅|
|🟢|can i sign up to the newsletter too?|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|i also want to sign up for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|i want to connect to sales|contact_sales|contact_sales|100.0%|✅|
|🟢|In what way were you formed?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|hey how are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|您好|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|when should i use rasa and when should i use rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|What are slots?|faq/slots|faq/slots|100.0%|✅|
|🟢|slots are what ?|faq/slots|faq/slots|100.0%|✅|
|🟢|what are slots|faq/slots|faq/slots|100.0%|✅|
|🟢|what slots are?|faq/slots|faq/slots|100.0%|✅|
|🟢|I need to study RASA step by step, which is the best site to study?|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|Could you please tell me more about Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|can i speak to the sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|Subscribe me to the newsletter please!|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|By what means were you made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|wer bist Du?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|Please schedule a sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|best policies to be used|technical_question|technical_question|100.0%|✅|
|🟢|Is there any Rasa meetups?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|what are the policy available|technical_question|technical_question|100.0%|✅|
|🟢|can you show me buttons|technical_question|technical_question|100.0%|✅|
|🟢|Give me more information about Rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|What kinds of events are on your schedule?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|I would like to contact your sales team please|contact_sales|contact_sales|100.0%|✅|
|🟢|sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|i am a new|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Where is next community event held?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|i'm new to rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|tell me how to get started with core|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|do the newsletter then|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|ljljl|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What's new in Rasa X compared to Rasa?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|heelio|greet|greet|100.0%|✅|
|🟢|i want to book a sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|how do I get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how do I get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how do i start|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|what's your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|What's your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|Where did you originate?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|What facts diverge core from nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what kind of events will be held?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|how do i get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how do i get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|conda threw some weird error|technical_question|technical_question|100.0%|✅|
|🟢|howareyou|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|Tell me my name|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|Tell me my name.|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|hello hi|greet|greet|100.0%|✅|
|🟢|i need to talk to sales|contact_sales|contact_sales|100.0%|✅|
|🟢|I am new to Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|what model do you use|technical_question|technical_question|100.0%|✅|
|🟢|How many in the community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|Is there any special in next community event?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|I want to talk to your sales guys|contact_sales|contact_sales|100.0%|✅|
|🟢|how to handle sending scheduled message to custom webhooks|technical_question|technical_question|100.0%|✅|
|🟢|What could be my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|when can you tell me what a slot is ?|faq/slots|faq/slots|100.0%|✅|
|🟢|do rasa provide speech intent|faq/voice|faq/voice|100.0%|✅|
|🟢|im a developer|enter_data|enter_data|100.0%|✅|
|🟢|How do I get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|How do I get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|How do i get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to create a basic chat bot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to get started with rassa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|multipass issue|technical_question|technical_question|100.0%|✅|
|🟢|How do I install Rasa Stack?|install_rasa|install_rasa|100.0%|✅|
|🟢|best tutorial for rasa|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|a chatbot for our company|enter_data|enter_data|100.0%|✅|
|🟢|i want to join the newsletter mails|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|what is default fall back|technical_question|technical_question|100.0%|✅|
|🟢|slots can be described as ?|faq/slots|faq/slots|100.0%|✅|
|🟢|how to integrate speech to text in rasa|faq/voice|faq/voice|100.0%|✅|
|🟢|yeah|affirm|affirm|100.0%|✅|
|🟢|yeah'=|affirm|affirm|100.0%|✅|
|🟢|hallo|greet|greet|100.0%|✅|
|🟢|where should i start from|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Can you recommend a restaurant open right now|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|What are the events that you have?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|can you tell all of the events?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|I also want to book a sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|a cool bot|enter_data|enter_data|100.0%|✅|
|🟢|domain|technical_question|technical_question|100.0%|✅|
|🟢|tell me about the different parts of rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|what is Rasa Playground ?|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|what is rasa playground ?|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|show me comparison between rasa x and rasa|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|halloo|greet|greet|100.0%|✅|
|🟢|Is there an event in Montreal?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|I want the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|I want to sign up for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|I want to sign up for the newsletter.|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|i want to signup for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|what is the forum in your community used for|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|is there an event in Montreal|ask_which_events|ask_which_events|100.0%|✅|
|🟢|I want to install Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|🟢|i want the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|i want to receive the newsletter emails|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|i want to sign up for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|subscribe Denise@gmail.com to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|hosting|technical_question|technical_question|100.0%|✅|
|🟢|What is the magnitude of the community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|halloooo|greet|greet|100.0%|✅|
|🟢|when will the community event take place?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|can i get a ssales call|contact_sales|contact_sales|100.0%|✅|
|🟢|can you pelase subscribe me to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|tell me difference between Rasa and Rasa X|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|Yea|affirm|affirm|100.0%|✅|
|🟢|I'm the developer|enter_data|enter_data|100.0%|✅|
|🟢|sign me up for the rasa newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|are you a Skynet ?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|r u a human|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|what languages you are well versed ?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|你好|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|pizza|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What exactly are slots?|faq/slots|faq/slots|100.0%|✅|
|🟢|slots are what exactly?|faq/slots|faq/slots|100.0%|✅|
|🟢|noooooooooo|deny|deny|100.0%|✅|
|🟢|how can i build a chatbot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|How can i launch a bot?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|interactive learning?|technical_question|technical_question|100.0%|✅|
|🟢|Are there any meteorological changes that I need to be aware of?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|i want to be in touch with sales|contact_sales|contact_sales|100.0%|✅|
|🟢|Which events are available?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|custom entity|enter_data|enter_data|100.0%|✅|
|🟢|i'm a race car driver|enter_data|enter_data|100.0%|✅|
|🟢|Only NLU|enter_data|enter_data|100.0%|✅|
|🟢|rasa basics|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|install rasa x with or without rasa open source ?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|are you really free|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|are you really free?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|how can i start with rasa core?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Can I use the rasa code for my own website?|faq/channels|faq/channels|100.0%|✅|
|🟢|whats the purpose of this forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|jop|greet|greet|100.0%|✅|
|🟢|just gimme a call|contact_sales|contact_sales|100.0%|✅|
|🟢|How to start using Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to get sarted|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|which messaging channels are compatible with rasa?|faq/channels|faq/channels|100.0%|✅|
|🟢|I want to build a bot in Hindi|faq/languages|faq/languages|100.0%|✅|
|🟢|are there any languages that rasa supports?|faq/languages|faq/languages|100.0%|✅|
|🟢|Is there a Rasa meetup|ask_which_events|ask_which_events|100.0%|✅|
|🟢|I would like to have a call with sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|let' contact sales now|contact_sales|contact_sales|100.0%|✅|
|🟢|I'm a machine learning engineer|enter_data|enter_data|100.0%|✅|
|🟢|I’ve trained it in german|enter_data|enter_data|100.0%|✅|
|🟢|hi, can you help in understanding NLU|faq/nlu|faq/nlu|100.0%|✅|
|🟢|how slots are filled|faq/slots|faq/slots|100.0%|✅|
|🟢|ssup?|greet|greet|100.0%|✅|
|🟢|Can you tell me what kinds of events you have?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|gimme the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|help|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|help?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|slots, what do youi mean?|faq/slots|faq/slots|100.0%|✅|
|🟢|Heya|greet|greet|100.0%|✅|
|🟢|when is the event within the community gonna happen?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|I am a driver|enter_data|enter_data|100.0%|✅|
|🟢|how start|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|I wanna sign up for the newsletter.|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Hello sara|greet|greet|100.0%|✅|
|🟢|how t oget started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Hellllooooooo|greet|greet|100.0%|✅|
|🟢|temperature?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|Cars|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how to integrate rasa chatbot with my website|faq/channels|faq/channels|100.0%|✅|
|🟢|how big is your community|faq/community_size|faq/community_size|100.0%|✅|
|🟢|Yeah|affirm|affirm|100.0%|✅|
|🟢|hi sara|greet|greet|100.0%|✅|
|🟢|I wanna talk to your sales guy|contact_sales|contact_sales|100.0%|✅|
|🟢|are you having a good day|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|When is it planned the next event in Montreal?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|id like to receive the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|I'd like to know how you were put together?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|how about your age|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|tell me something you can do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|contact any sales person|contact_sales|contact_sales|100.0%|✅|
|🟢|lets try the newsletter signup|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|which technology is used to create you|technical_question|technical_question|100.0%|✅|
|🟢|hey bot|greet|greet|100.0%|✅|
|🟢|hey bot!|greet|greet|100.0%|✅|
|🟢|please teach me|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Do you have good weather?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|What is the number of people in this community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|yesh|affirm|affirm|100.0%|✅|
|🟢|What is the next event in Paris?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|When is the next event in detroit?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|let me contact sales|contact_sales|contact_sales|100.0%|✅|
|🟢|how do i get startd?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|What kinds of events are on your calendar?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|a sales call with Rufus Gardner would be nice|contact_sales|contact_sales|100.0%|✅|
|🟢|how toget strated?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|get the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|How big is this community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|i want to contact your sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|german is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|🟢|What are the prerequisites for installing RASA|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|I want to install rasa|install_rasa|install_rasa|100.0%|✅|
|🟢|how to run sdk endpoint in background|technical_question|technical_question|100.0%|✅|
|🟢|cost|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|hellio|greet|greet|100.0%|✅|
|🟢|request sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|i am new|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|I'll subscribe to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|i want newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|sign me up for that newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|How long have you been around?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|Give me the time.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|find out how to get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|i would like to join the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Should I run the 'rasa init' command in the anaconda prompt ?|technical_question|technical_question|100.0%|✅|
|🟢|how to keep button system for slot selection|faq/slots|faq/slots|100.0%|✅|
|🟢|How many languages are you familiar with?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|do you have a large community|faq/community_size|faq/community_size|100.0%|✅|
|🟢|Will it work for german|faq/languages|faq/languages|100.0%|✅|
|🟢|hai|greet|greet|100.0%|✅|
|🟢|hiihihi|greet|greet|100.0%|✅|
|🟢|how can I get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how can I get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how do you restart a story?|technical_question|technical_question|100.0%|✅|
|🟢|I want to book a call|contact_sales|contact_sales|100.0%|✅|
|🟢|i want to connect your sales|contact_sales|contact_sales|100.0%|✅|
|🟢|How get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to start rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|wassup>|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how does Rasa Playground work?|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|Rasa is good for messaging chanels|faq/channels|faq/channels|100.0%|✅|
|🟢|what's the difference between rasa and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|Explain slots to me?|faq/slots|faq/slots|100.0%|✅|
|🟢|Tell me the events you have|ask_which_events|ask_which_events|100.0%|✅|
|🟢|When is the next event in Berlin|ask_which_events|ask_which_events|100.0%|✅|
|🟢|Yes I am new|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|i m new|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|i need help with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|i'm new|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how can i get stared|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|What is the difference between rasa nlu and rasa core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what is the difference between rasa nlu and rasa core|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what is the difference between rasa nlu and rasa core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|how to programe rasa|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|what is python version required?|faq/python_version|faq/python_version|100.0%|✅|
|🟢|hi|greet|greet|100.0%|✅|
|🟢|hi !|greet|greet|100.0%|✅|
|🟢|hi!|greet|greet|100.0%|✅|
|🟢|hi.........................................................|greet|greet|100.0%|✅|
|🟢|hi?|greet|greet|100.0%|✅|
|🟢|i want to talk to sales|contact_sales|contact_sales|100.0%|✅|
|🟢|intent classificaton|nlu_info|nlu_info|100.0%|✅|
|🟢|tell me some languages you know?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|yea|affirm|affirm|100.0%|✅|
|🟢|i choose the call|contact_sales|contact_sales|100.0%|✅|
|🟢|how do i build a chatbot?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how old will you be this year?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|hola|greet|greet|100.0%|✅|
|🟢|when will our next group event be?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|I want to talk to sales|contact_sales|contact_sales|100.0%|✅|
|🟢|I want to talk to your sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|how to start with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to start with rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|tell me how to start|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|yes accept please|affirm|affirm|100.0%|✅|
|🟢|I would like to sign up for the newsletter.|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|What is your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|what is your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|when is the next event?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|how to learn rasa core|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|technical question|technical_question|technical_question|100.0%|✅|
|🟢|I want to contact the sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|What Python version should I use?|faq/python_version|faq/python_version|100.0%|✅|
|🟢|what python version should i use|faq/python_version|faq/python_version|100.0%|✅|
|🟢|Yepp|affirm|affirm|100.0%|✅|
|🟢|may i receive the newsletter from now on|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|What is the next event for Seattle?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|What is the next event for paris?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|Is there any restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|more info on components|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|Bonjour|greet|greet|100.0%|✅|
|🟢|how can I meet eh community?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|Do you know the exact date for the next community event?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|what is components|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|when is the next group event going to be?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|what's the  difference between rasa nlu and rasa core|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|sorry tell me about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|i don't know|enter_data|enter_data|100.0%|✅|
|🟢|subscribe Bruce_harryman@Olsen.com to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|How can I change the language|faq/languages|faq/languages|100.0%|✅|
|🟢|how do i set up a chatbot?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Hello, where can I find the paper about DIET?|technical_question|technical_question|100.0%|✅|
|🟢|What do I do with slots?|faq/slots|faq/slots|100.0%|✅|
|🟢|fuck yeah!|affirm|affirm|100.0%|✅|
|🟢|How can I get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|I am new|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Please tell me how I can start?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|what is componenbts|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|I would like to book a sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|how can i get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|i want to  suscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|components of Rasa?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|components of rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|hey there boy|greet|greet|100.0%|✅|
|🟢|german is the language of my bot|enter_data|enter_data|100.0%|✅|
|🟢|entity recognition|nlu_info|nlu_info|100.0%|✅|
|🟢|wasssup|greet|greet|100.0%|✅|
|🟢|wasssup!|greet|greet|100.0%|✅|
|🟢|Do you know when is the next event in Montreal?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|how to start RASA|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|go back|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|can you explain rasa playground to me|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|Any other event like rasa meetup in future?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|I want to book a call with your sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|hello sara|greet|greet|100.0%|✅|
|🟢|whats up|greet|greet|100.0%|✅|
|🟢|book call|contact_sales|contact_sales|100.0%|✅|
|🟢|When is it scheduled the next community event?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|What exactly is my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|Help me understand what slots are.|faq/slots|faq/slots|100.0%|✅|
|🟢|i want to subsribe to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|newletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|How can i talk to RASA through the url|technical_question|technical_question|100.0%|✅|
|🟢|Tell me how to get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|howdy|greet|greet|100.0%|✅|
|🟢|Evaluate Rasa :-)|enter_data|enter_data|100.0%|✅|
|🟢|I would love to subscribe to a newsletter!|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|What do you do at Rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|When is the next event in california?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|the bot that helps you choose insurance for the car ;)|enter_data|enter_data|100.0%|✅|
|🟢|i want to talk to a real person|human_handoff|human_handoff|100.0%|✅|
|🟢|tell me about rasa enterprise|faq/ee|faq/ee|100.0%|✅|
|🟢|between 100 to 200.000|enter_data|enter_data|100.0%|✅|
|🟢|subscribe to our newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|what is your exact age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|What is the price ?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|what is the price?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|sup|greet|greet|100.0%|✅|
|🟢|have a call with the sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|How to get started with Rasa core?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|what i have to do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|Where do you consider home?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|You live around here?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|hey hey|greet|greet|100.0%|✅|
|🟢|how to get started with|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Are you from around here?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|are you from around here?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|How big is the community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|i want to install rasa|install_rasa|install_rasa|100.0%|✅|
|🟢|tell me what is rasa x ee|faq/ee|faq/ee|100.0%|✅|
|🟢|talk to me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|talk to me!|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|Definition of slots please.|faq/slots|faq/slots|100.0%|✅|
|🟢|how easy is it to use rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|I want to know more about tracker|technical_question|technical_question|100.0%|✅|
|🟢|No, I mean how it is possible to use Skype as channel?|faq/channels|faq/channels|100.0%|✅|
|🟢|do you cost anything?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|what slots are there?|faq/slots|faq/slots|100.0%|✅|
|🟢|Tell me when the next community event is happening;|ask_which_events|ask_which_events|100.0%|✅|
|🟢|How to install Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|🟢|How are things?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|Good mourning|greet|greet|100.0%|✅|
|🟢|Which events do you have?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|I want to speak with sales|contact_sales|contact_sales|100.0%|✅|
|🟢|how to integrate u in my react application|faq/channels|faq/channels|100.0%|✅|
|🟢|request a call|contact_sales|contact_sales|100.0%|✅|
|🟢|Can I have multiple .md data files?|technical_question|technical_question|100.0%|✅|
|🟢|I'd like to know what my name is|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|i'd like to talk to sales|contact_sales|contact_sales|100.0%|✅|
|🟢|it speaks german|enter_data|enter_data|100.0%|✅|
|🟢|How to install rasa stack|install_rasa|install_rasa|100.0%|✅|
|🟢|rasa uses deep learning ?|technical_question|technical_question|100.0%|✅|
|🟢|first lets sign up for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|get newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|relationship between rasa open source and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|yo|greet|greet|100.0%|✅|
|🟢|When is the next event for Detroit?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|integrate rasa with ui|faq/channels|faq/channels|100.0%|✅|
|🟢|What is the date of the next community event?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|call with sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|i want to connect to your sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|How long have you occupied the earth?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|how many words can you handle?|technical_question|technical_question|100.0%|✅|
|🟢|i need to be on the newsletter list|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|i'm craving the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|subsribing to our newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|an I use Rasa for e-mail applications|technical_question|technical_question|100.0%|✅|
|🟢|i want to receive the newsletter from now on|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|What are slots used for?|faq/slots|faq/slots|100.0%|✅|
|🟢|Yes, I accept|affirm|affirm|100.0%|✅|
|🟢|how to install rasa stack|install_rasa|install_rasa|100.0%|✅|
|🟢|中文|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|what are you ding|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|When is the next event scheduled?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|Show me learning resources about Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|subscribing to our newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Is there a connector for skype?|faq/channels|faq/channels|100.0%|✅|
|🟢|Please connect me to someone from sales|contact_sales|contact_sales|100.0%|✅|
|🟢|intent recognition|nlu_info|nlu_info|100.0%|✅|
|🟢|You have rasa meetups?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|how does entity recognition work?|nlu_info|nlu_info|100.0%|✅|
|🟢|Can you brief me about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|Where can I meet Rasas|ask_which_events|ask_which_events|100.0%|✅|
|🟢|By chance do you know the date of next community event?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|what are the componensts of RASA|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|hey|greet|greet|100.0%|✅|
|🟢|can you connect me to sales|contact_sales|contact_sales|100.0%|✅|
|🟢|I'm new|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to get started with rasa nlu|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|is it sunny|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|What are you able to do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|bonjour|greet|greet|100.0%|✅|
|🟢|sales please|contact_sales|contact_sales|100.0%|✅|
|🟢|yeaaah lets go for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|what is the difference between rasa and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|conda throws some unexpected error|technical_question|technical_question|100.0%|✅|
|🟢|yaah|affirm|affirm|100.0%|✅|
|🟢|yez|affirm|affirm|100.0%|✅|
|🟢|where can I see a calendar of community events?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|how can i start|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|get starte|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|intents|nlu_info|nlu_info|100.0%|✅|
|🟢|are there any other options?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|Subscription price|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|talk to human|human_handoff|human_handoff|100.0%|✅|
|🟢|i want to get the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|hey can i run this onpremise|technical_question|technical_question|100.0%|✅|
|🟢|What are the two components that make up Rasa Open Source?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|Can you find me a burger joint?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|What time have we got?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|eres humana|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|halo|greet|greet|100.0%|✅|
|🟢|Can you help me with forms|technical_question|technical_question|100.0%|✅|
|🟢|yoo|greet|greet|100.0%|✅|
|🟢|Please help me install Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|🟢|Talk slots over with me.|faq/slots|faq/slots|100.0%|✅|
|🟢|how to implement buttons|technical_question|technical_question|100.0%|✅|
|🟢|What location are you from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|stories files|technical_question|technical_question|100.0%|✅|
|🟢|Can I have a call?|contact_sales|contact_sales|100.0%|✅|
|🟢|can i talk to a sales representative|contact_sales|contact_sales|100.0%|✅|
|🟢|How small is the community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|hhola|greet|greet|100.0%|✅|
|🟢|yess|affirm|affirm|100.0%|✅|
|🟢|HEY|greet|greet|100.0%|✅|
|🟢|how to get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|ok, i know i confused you there being a human! :)|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|top|affirm|affirm|100.0%|✅|
|🟢|Heylo|greet|greet|100.0%|✅|
|🟢|implement buttons|technical_question|technical_question|100.0%|✅|
|🟢|In what manner were you formed?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|Do I have a name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|sales|contact_sales|contact_sales|100.0%|✅|
|🟢|how do i learn rasa core|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to set text slot without mentioned json|faq/slots|faq/slots|100.0%|✅|
|🟢|What is on the calendar for this month?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|Tell me all of the events you have.|ask_which_events|ask_which_events|100.0%|✅|
|🟢|How to get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|How to get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Entity recognition|nlu_info|nlu_info|100.0%|✅|
|🟢|What languages does rasa know?|faq/languages|faq/languages|100.0%|✅|
|🟢|why should i use rasa instead of IBM watson ?|why_rasa|why_rasa|100.0%|✅|
|🟢|i would like to talk to sales please|contact_sales|contact_sales|100.0%|✅|
|🟢|can rasa be used with alexa|faq/voice|faq/voice|100.0%|✅|
|🟢|Do you have rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|Whats up|greet|greet|100.0%|✅|
|🟢|Whats up?|greet|greet|100.0%|✅|
|🟢|i want to talk to a person|human_handoff|human_handoff|100.0%|✅|
|🟢|hey dude|greet|greet|100.0%|✅|
|🟢|I'm new to Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how do i build a rasa chatbot?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|what is this rasa playground thing. could you tell me more?|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|hi i'm Sandra Hernandez|greet|greet|100.0%|✅|
|🟢|I'd like to know my name|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|Does anyone know what slots are?|faq/slots|faq/slots|100.0%|✅|
|🟢|how can i use rasa with alexa|faq/voice|faq/voice|100.0%|✅|
|🟢|hi pal!|greet|greet|100.0%|✅|
|🟢|intent classification|nlu_info|nlu_info|100.0%|✅|
|🟢|Newsletter please.|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|noooooooooooooooooooooooooooooooooooooooo|deny|deny|100.0%|✅|
|🟢|subscribe to your newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|For training data, to we need to exclusively write the file in MD format?|technical_question|technical_question|100.0%|✅|
|🟢|yes i agree|affirm|affirm|100.0%|✅|
|🟢|add me to the newsletter list|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|I'm new to rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|i would love to get the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|tensorflow|technical_question|technical_question|100.0%|✅|
|🟢|where's your home town?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|Which events you got?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|tell me more about rasa nlu|faq/nlu|faq/nlu|100.0%|✅|
|🟢|i dont know the difference|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|If I use Rasa, do I also need Rasa X?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|whats the cost of rasa|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Help me to figure out the meaning of slots.|faq/slots|faq/slots|100.0%|✅|
|🟢|newsletter please my email is M_Moore@yahoo.com|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|WHAT MESSAGING PORTALS DOES RASA SUPPORT?|faq/channels|faq/channels|100.0%|✅|
|🟢|what is the variety of languages rasa uses|faq/languages|faq/languages|100.0%|✅|
|🟢|Can I have a call tomorrow at 3pm?|contact_sales|contact_sales|100.0%|✅|
|🟢|does rasa support this language?|faq/languages|faq/languages|100.0%|✅|
|🟢|hallo sara|greet|greet|100.0%|✅|
|🟢|do you have an event in Berlin|ask_which_events|ask_which_events|100.0%|✅|
|🟢|booking a sall|contact_sales|contact_sales|100.0%|✅|
|🟢|i want to speak to human|human_handoff|human_handoff|100.0%|✅|
|🟢|What makes core distinct to nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|rasa os|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|I'm a developer|enter_data|enter_data|100.0%|✅|
|🟢|What size is the Rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|tell me the slots?|faq/slots|faq/slots|100.0%|✅|
|🟢|What do people call me?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|Please elaborate on the game of slots?|faq/slots|faq/slots|100.0%|✅|
|🟢|Please tell me how to get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|let me talk to a real person|human_handoff|human_handoff|100.0%|✅|
|🟢|please subscribe me to your newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|where is the api for rasa x|technical_question|technical_question|100.0%|✅|
|🟢|wow you sound like real human|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|i want to contact sales support|contact_sales|contact_sales|100.0%|✅|
|🟢|How did they create you?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|HI|greet|greet|100.0%|✅|
|🟢|good evening|greet|greet|100.0%|✅|
|🟢|Hey Sara|greet|greet|100.0%|✅|
|🟢|help me get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|send me the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|what are the features does rasa have?    |faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|newsletter please|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|yesyesyes|affirm|affirm|100.0%|✅|
|🟢|can you add Edward@Paul.com to the newsletter list?|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|What time is it in Berlin?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|When is the next event for India?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|WHo am I|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|Who am I?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|who am i|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|I'm installing Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|🟢|how about the newsletter signup|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|nl|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|i want to be connected to your sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|When is the next user group meetup|ask_which_events|ask_which_events|100.0%|✅|
|🟢|please subscribe me to the newsletter gregory_lilley@yahoo.com|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|i want to learn more about Rasa X EE|faq/ee|faq/ee|100.0%|✅|
|🟢|i go for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|i just want to signup for our newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|how do i detect entities|technical_question|technical_question|100.0%|✅|
|🟢|what is the time in Sydney?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|cool beans|react_positive|react_positive|100.0%|✅|
|🟢|I want information about rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|tell me the difference between rasa and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|How can I determine who I am?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|How can I determine who am I?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|newsletter pls|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|what is the difference?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|add me to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|subscription newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Are you familiar with more than one language?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|Hieeeeeeeeeeeee|greet|greet|100.0%|✅|
|🟢|Is RASA NLU avaiable for German?|faq/languages|faq/languages|100.0%|✅|
|🟢|a insurance tool that consults potential customers on the best life insurance to choose.|enter_data|enter_data|100.0%|✅|
|🟢|can i subscribe to news letter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|tu pagal|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|dude, i want install rasa|install_rasa|install_rasa|100.0%|✅|
|🟢|can you help me with this problem|technical_question|technical_question|100.0%|✅|
|🟢|What are the languages that rasa supports?|faq/languages|faq/languages|100.0%|✅|
|🟢|NLW|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What even is coming up next and when is it please?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|hep me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|hey there|greet|greet|100.0%|✅|
|🟢|hey there..|greet|greet|100.0%|✅|
|🟢|Sales|contact_sales|contact_sales|100.0%|✅|
|🟢|how do I install rasa in windows|install_rasa|install_rasa|100.0%|✅|
|🟢|hello sara, can you subscribe me to the newsletter?|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|I'm going to install Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|🟢|what's the difference?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|How can i contact the team ?|contact_sales|contact_sales|100.0%|✅|
|🟢|please send me the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|what's rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|whats the diference|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|how to restart the rasa server|technical_question|technical_question|100.0%|✅|
|🟢|TypeError: 'module' object is not callable|technical_question|technical_question|100.0%|✅|
|🟢|what is rasaplayground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|Is rasa have more than 1000 members?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|where slots getting values|faq/slots|faq/slots|100.0%|✅|
|🟢|a call|contact_sales|contact_sales|100.0%|✅|
|🟢|What is your count of years being alive so far?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|doea rasa support a particular langauage?|faq/languages|faq/languages|100.0%|✅|
|🟢|what language does rasa support?|faq/languages|faq/languages|100.0%|✅|
|🟢|Could you please list the kinds of events that you have?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|how to setup rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|where can I find out what a slot is?|faq/slots|faq/slots|100.0%|✅|
|🟢|I want to talk to your sales people|contact_sales|contact_sales|100.0%|✅|
|🟢|I need to install Rasa|install_rasa|install_rasa|100.0%|✅|
|🟢|How old were you on your last birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|how old were you on your last birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|Hi sara|greet|greet|100.0%|✅|
|🟢|Hi sara..|greet|greet|100.0%|✅|
|🟢|what is custom actions|technical_question|technical_question|100.0%|✅|
|🟢|from where I should start?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|newsletter - my email is Mabel@Brown.com|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|I don’t understand entity recognition|nlu_info|nlu_info|100.0%|✅|
|🟢|could you inform me of the meaning of slots?|faq/slots|faq/slots|100.0%|✅|
|🟢|tell me your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|what is a component in rasa?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|Do I need both Rasa and Rasa X?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|recognition|nlu_info|nlu_info|100.0%|✅|
|🟢|can I run rasa on a raspberry pi|technical_question|technical_question|100.0%|✅|
|🟢|Assuming that there is an upcoming event, when is that event?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|If there is an upcoming event when is it?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|What else do people call me?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|hello there|greet|greet|100.0%|✅|
|🟢|can i please speak to a human?|human_handoff|human_handoff|100.0%|✅|
|🟢|hell yeah|affirm|affirm|100.0%|✅|
|🟢|hi hi|greet|greet|100.0%|✅|
|🟢|What state were you born in?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|Is next community event held in 2019?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|Is there a meetup|ask_which_events|ask_which_events|100.0%|✅|
|🟢|Is the Rasa Community large?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|Is the Rasa community large?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|connect me to a real person|human_handoff|human_handoff|100.0%|✅|
|🟢|rasa playground|enter_data|enter_data|100.0%|✅|
|🟢|how do i install rasa?|install_rasa|install_rasa|100.0%|✅|
|🟢|what makes core and nlu unique from each other?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|hmmm sales|contact_sales|contact_sales|100.0%|✅|
|🟢|Help me get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to train model|technical_question|technical_question|100.0%|✅|
|🟢|Im new|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to get strated|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to get strated?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Can you tell me more about NLU?|faq/nlu|faq/nlu|100.0%|✅|
|🟢|newsletter, here is my email: Marcus.Miller@yahoo.com|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Do you know who I am?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|Do you know who am I?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|how about interactive learning|technical_question|technical_question|100.0%|✅|
|🟢|Can I die|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|can i get emails from you|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|i want to chat to sales|contact_sales|contact_sales|100.0%|✅|
|🟢|I want to get in touch with your sales guys|contact_sales|contact_sales|100.0%|✅|
|🟢|book an appointment|contact_sales|contact_sales|100.0%|✅|
|🟢|McKinsey Germany|enter_data|enter_data|100.0%|✅|
|🟢|how is entity recognition managed in rasa?|nlu_info|nlu_info|100.0%|✅|
|🟢|i just want to signup for your newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Rasa provides me recall and precision?|technical_question|technical_question|100.0%|✅|
|🟢|What events are scheduled for today?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|i am qq|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|uh-huh|affirm|affirm|100.0%|✅|
|🟢|ola sara|greet|greet|100.0%|✅|
|🟢|Tell me more about Get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|is it a best practice to connect an external cms|technical_question|technical_question|100.0%|✅|
|🟢|so now what|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|i would like a call with Mr Hughes|contact_sales|contact_sales|100.0%|✅|
|🟢|how are you doing today my sweet friend|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|so what next?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|hello friend|greet|greet|100.0%|✅|
|🟢|Do you mind helping me install Rasa?|install_rasa|install_rasa|100.0%|✅|
|🟢|yes pleae|affirm|affirm|100.0%|✅|
|🟢|Voice bot|faq/voice|faq/voice|100.0%|✅|
|🟢|can I speak to a person?|human_handoff|human_handoff|100.0%|✅|
|🟢|I wanna build a bot that sends the people cute animal pictures based on their favorite color|enter_data|enter_data|100.0%|✅|
|🟢|ok i accept|affirm|affirm|100.0%|✅|
|🟢|human handoff|human_handoff|human_handoff|100.0%|✅|
|🟢|language|faq/languages|faq/languages|100.0%|✅|
|🟢|What and when is the next event?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|is Rasa works with Unity3d?|technical_question|technical_question|100.0%|✅|
|🟢|I would like to know more about your product|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|Custom Connectors|faq/channels|faq/channels|100.0%|✅|
|🟢|Hey bot|greet|greet|100.0%|✅|
|🟢|I want to talk to a human|human_handoff|human_handoff|100.0%|✅|
|🟢|you are doin great|react_positive|react_positive|100.0%|✅|
|🟢|Hey|greet|greet|100.0%|✅|
|🟢|What is up?|greet|greet|100.0%|✅|
|🟢|Are you ok?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|How you doing?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|are you ok|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how you doing|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|how you doing?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|i prefer to get the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|sign me up, my email is Elizabeth@yahoo.com|contact_sales|contact_sales|100.0%|✅|
|🟢|Tell me about rasa x ee|faq/ee|faq/ee|100.0%|✅|
|🟢|tell me about rasa x EE|faq/ee|faq/ee|100.0%|✅|
|🟢|where to intents?|nlu_info|nlu_info|100.0%|✅|
|🟢|does the community have meet ups?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|I wanna talk to your sales people.|contact_sales|contact_sales|100.0%|✅|
|🟢|Lets start with the basics|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|YES|affirm|affirm|100.0%|✅|
|🟢|how do I install rasa?|install_rasa|install_rasa|100.0%|✅|
|🟢|yup|affirm|affirm|100.0%|✅|
|🟢|HAHA|react_positive|react_positive|100.0%|✅|
|🟢|how to start|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|what is entity recognition?|nlu_info|nlu_info|100.0%|✅|
|🟢|how to subdcribe?|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|elaborate on rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|what is the language rasa supports|faq/languages|faq/languages|100.0%|✅|
|🟢|can i talk to a real person?|human_handoff|human_handoff|100.0%|✅|
|🟢|what are intents ?|nlu_info|nlu_info|100.0%|✅|
|🟢|what are intents?|nlu_info|nlu_info|100.0%|✅|
|🟢|ye|affirm|affirm|100.0%|✅|
|🟢|what is intent recognition?|nlu_info|nlu_info|100.0%|✅|
|🟢|i would love to receive the rasa newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|yes pls|affirm|affirm|100.0%|✅|
|🟢|At which date the next community event will take place?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|is this free?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|this is free?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|i want to speak to a real person|human_handoff|human_handoff|100.0%|✅|
|🟢|nah, i'm good|deny|deny|100.0%|✅|
|🟢|i want to talk to human|human_handoff|human_handoff|100.0%|✅|
|🟢|newsletter subscription|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Do you have a python sdk?|technical_question|technical_question|100.0%|✅|
|🟢|what is the difference between rasaand rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|yes go ahead|affirm|affirm|100.0%|✅|
|🟢|can i speak to a human|human_handoff|human_handoff|100.0%|✅|
|🟢|can you tell me your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|i want to call|contact_sales|contact_sales|100.0%|✅|
|🟢|just rasa nlu|enter_data|enter_data|100.0%|✅|
|🟢|newsletter registration|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|how do i get started with nlu|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to get start with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|great|affirm|affirm|100.0%|✅|
|🟢|great!|affirm|affirm|100.0%|✅|
|🟢|HI Sara|greet|greet|100.0%|✅|
|🟢|oh actually i want to get the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|let me talk sales|contact_sales|contact_sales|100.0%|✅|
|🟢|where can i find api documentation for rasa x|technical_question|technical_question|100.0%|✅|
|🟢|yow are you|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|Can I use your open source code on my website?|faq/channels|faq/channels|100.0%|✅|
|🟢|what is rasa enterprise|faq/ee|faq/ee|100.0%|✅|
|🟢|i cannot find tutorial for rasa|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|I agree|affirm|affirm|100.0%|✅|
|🟢|please give me a human|human_handoff|human_handoff|100.0%|✅|
|🟢|embeddings|technical_question|technical_question|100.0%|✅|
|🟢|so how does it all work?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|no i dont want to|deny|deny|100.0%|✅|
|🟢|gsaf|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|are there tutorials about rasa?|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|hahaha|react_positive|react_positive|100.0%|✅|
|🟢|jojojo|greet|greet|100.0%|✅|
|🟢|more info|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|Why switch to Rasa?|why_rasa|why_rasa|100.0%|✅|
|🟢|how i program the bot?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|How can I start with RASA on a legacy windows without Python?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|request call|contact_sales|contact_sales|100.0%|✅|
|🟢|ok i want to talk to your sales guys|contact_sales|contact_sales|100.0%|✅|
|🟢|Hi there, are you the bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|Can I create a chat bot and set it up on a web page?|faq/channels|faq/channels|100.0%|✅|
|🟢|yes sirfr|affirm|affirm|100.0%|✅|
|🟢|Hello Bot|greet|greet|100.0%|✅|
|🟢|yaps|affirm|affirm|100.0%|✅|
|🟢|i think I want to talk to your sales folks|contact_sales|contact_sales|100.0%|✅|
|🟢|please send newsletter to Robert@yahoo.com|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|what infrastructure is required to run a bot?|technical_question|technical_question|100.0%|✅|
|🟢|Great, is there anything else you can do, bot?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what is the difference between rasa open source and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|what version does python needs|faq/python_version|faq/python_version|100.0%|✅|
|🟢|amayzing|affirm|affirm|100.0%|✅|
|🟢|I don’t understand how you handle intent classification at Rasa|nlu_info|nlu_info|100.0%|✅|
|🟢|Guten Morgen|greet|greet|100.0%|✅|
|🟢|um what now|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|is rasa free|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|lead generation|enter_data|enter_data|100.0%|✅|
|🟢|thats great|affirm|affirm|100.0%|✅|
|🟢|I would like to book a call|contact_sales|contact_sales|100.0%|✅|
|🟢|I need help with a problem|technical_question|technical_question|100.0%|✅|
|🟢|just Rasa NLU|enter_data|enter_data|100.0%|✅|
|🟢|have a call|contact_sales|contact_sales|100.0%|✅|
|🟢|obviously talk to your awesome sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|i want to subscribe to your newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|can I develop using java|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|RASA IS SOFTWARE?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|hAHAHA|react_positive|react_positive|100.0%|✅|
|🟢|help with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Tell me about the entity recognition|nlu_info|nlu_info|100.0%|✅|
|🟢|Where are you located?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|Whats up my bot|greet|greet|100.0%|✅|
|🟢|Jane Baines|enter_data|enter_data|100.0%|✅|
|🟢|how to learn RASA|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|i agree|affirm|affirm|100.0%|✅|
|🟢|Great. Are there any tutorials?|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|how can I build a chatbot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|i want to talk to a human|human_handoff|human_handoff|100.0%|✅|
|🟢|i want to talk to a human \|human_handoff|human_handoff|100.0%|✅|
|🟢|I'm getting Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|🟢|what is the difference between the two?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|hello it is me again|greet|greet|100.0%|✅|
|🟢|I want to talk to the founders|human_handoff|human_handoff|100.0%|✅|
|🟢|can i speak to human|human_handoff|human_handoff|100.0%|✅|
|🟢|hlo|greet|greet|100.0%|✅|
|🟢|haha|react_positive|react_positive|100.0%|✅|
|🟢|i want one platform please|contact_sales|contact_sales|100.0%|✅|
|🟢|i want to signup|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Where can I find the definition of slots?|faq/slots|faq/slots|100.0%|✅|
|🟢|I'm new in Rasa, help me!|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|I'm using it|affirm|affirm|100.0%|✅|
|🟢|hi again|greet|greet|100.0%|✅|
|🟢|database rasa is using|technical_question|technical_question|100.0%|✅|
|🟢|I want to subscribe to your newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|halo sara|greet|greet|100.0%|✅|
|🟢|user can communicate with the bot in german|enter_data|enter_data|100.0%|✅|
|🟢|DOES RASA SUPPORT MESSENGER?|faq/channels|faq/channels|100.0%|✅|
|🟢|okie|affirm|affirm|100.0%|✅|
|🟢|On what day is the next event scheduled?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|let me talk to your sales people|contact_sales|contact_sales|100.0%|✅|
|🟢|let me talk to your sales people!|contact_sales|contact_sales|100.0%|✅|
|🟢|speak to a real person|human_handoff|human_handoff|100.0%|✅|
|🟢|talking to a bot is stupid|human_handoff|human_handoff|100.0%|✅|
|🟢|Can I run Rasa on a raspberry pi ?|technical_question|technical_question|100.0%|✅|
|🟢|how many ages?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|hieee|greet|greet|100.0%|✅|
|🟢|konichiwa|greet|greet|100.0%|✅|
|🟢|Give me the events you have.|ask_which_events|ask_which_events|100.0%|✅|
|🟢|what  are values of a boolean slot|technical_question|technical_question|100.0%|✅|
|🟢|Hi|greet|greet|100.0%|✅|
|🟢|Hi!|greet|greet|100.0%|✅|
|🟢|Hi'|greet|greet|100.0%|✅|
|🟢|Hi,|greet|greet|100.0%|✅|
|🟢|i want to signup for your newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|i accept|affirm|affirm|100.0%|✅|
|🟢|tell me more about rasa x EE|faq/ee|faq/ee|100.0%|✅|
|🟢|i want to book a appointment|contact_sales|contact_sales|100.0%|✅|
|🟢|Can I run rasa on a raspberry pi ?|technical_question|technical_question|100.0%|✅|
|🟢|get started pls|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|In which manner were you devised?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|slots|faq/slots|faq/slots|100.0%|✅|
|🟢|slots?|faq/slots|faq/slots|100.0%|✅|
|🟢|yessoo|affirm|affirm|100.0%|✅|
|🟢|yesyestyes|affirm|affirm|100.0%|✅|
|🟢|How were you set up?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|I dunno what a slot is|faq/slots|faq/slots|100.0%|✅|
|🟢|YUP|affirm|affirm|100.0%|✅|
|🟢|i want to be part of the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|why would you opt for rasa|why_rasa|why_rasa|100.0%|✅|
|🟢|You are great|react_positive|react_positive|100.0%|✅|
|🟢|tell me about entity recognition|nlu_info|nlu_info|100.0%|✅|
|🟢|yeah do that|affirm|affirm|100.0%|✅|
|🟢|Great|affirm|affirm|100.0%|✅|
|🟢|i would like to subscribe to your newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|ja thats great|affirm|affirm|100.0%|✅|
|🟢|How does core compare to nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|yap|affirm|affirm|100.0%|✅|
|🟢|Cool|react_positive|react_positive|100.0%|✅|
|🟢|what up|greet|greet|100.0%|✅|
|🟢|i wanna get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|yes it is|affirm|affirm|100.0%|✅|
|🟢|When do you celebrate your day of birth?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|Are you a human being?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|Just install Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|🟢|is duckling part of rasa?|nlu_info|nlu_info|100.0%|✅|
|🟢|how to add a database?|technical_question|technical_question|100.0%|✅|
|🟢|how to build rasa with different languages?|faq/languages|faq/languages|100.0%|✅|
|🟢|Hello Sara|greet|greet|100.0%|✅|
|🟢|hello robot|greet|greet|100.0%|✅|
|🟢|i am new but so how can i start|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|subcribe|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|I want to meet Rasa|ask_which_events|ask_which_events|100.0%|✅|
|🟢|sales sales sales|contact_sales|contact_sales|100.0%|✅|
|🟢|i want to subscribe to the newsletter with Joseph_Pyles@yahoo.com|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|agreed|affirm|affirm|100.0%|✅|
|🟢|how can I learn rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|x|enter_data|enter_data|100.0%|✅|
|🟢|and your REST API doesn't work|technical_question|technical_question|100.0%|✅|
|🟢|how does intent classification work?|nlu_info|nlu_info|100.0%|✅|
|🟢|Time, please!|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|how do i get started with NLU|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|wrong i want to speak to a human|human_handoff|human_handoff|100.0%|✅|
|🟢|id like to talk to a real rasa employee|human_handoff|human_handoff|100.0%|✅|
|🟢|Is the Rasa community medium?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|NO|deny|deny|100.0%|✅|
|🟢|no I dont want|deny|deny|100.0%|✅|
|🟢|name what a slot is|faq/slots|faq/slots|100.0%|✅|
|🟢|Please assist me with installing Rasa Stack.|install_rasa|install_rasa|100.0%|✅|
|🟢|can we make bot who speaks Japanese?|faq/languages|faq/languages|100.0%|✅|
|🟢|yes|affirm|affirm|100.0%|✅|
|🟢|yes ...|affirm|affirm|100.0%|✅|
|🟢|yes'|affirm|affirm|100.0%|✅|
|🟢|yes.|affirm|affirm|100.0%|✅|
|🟢|hahah|react_positive|react_positive|100.0%|✅|
|🟢|i'm a developer|enter_data|enter_data|100.0%|✅|
|🟢|i'm a developer|enter_data|enter_data|100.0%|✅|
|🟢|What is my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|what is my name|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|what is my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|do you know how old you are?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|what are the difference?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|how does rasa x stack up against rasa|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|jo|affirm|affirm|100.0%|✅|
|🟢|let me call the sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|can you tell me about rasa x ee?|faq/ee|faq/ee|100.0%|✅|
|🟢|Yes|affirm|affirm|100.0%|✅|
|🟢|Yes.|affirm|affirm|100.0%|✅|
|🟢|yes of course|affirm|affirm|100.0%|✅|
|🟢|can i took with a real person|human_handoff|human_handoff|100.0%|✅|
|🟢|What are the differences?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|what are the differences?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|Hallo|greet|greet|100.0%|✅|
|🟢|i want on that dope newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|more|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how to use rasa in salesforce|faq/channels|faq/channels|100.0%|✅|
|🟢|docs|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|What is your birthplace?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|i want to signup for the nl|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|What can you tell me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what can you tell me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|Is there a tutorial for Rasa?|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|coolio|react_positive|react_positive|100.0%|✅|
|🟢|okay|affirm|affirm|100.0%|✅|
|🟢|okay..|affirm|affirm|100.0%|✅|
|🟢|yes go for it|affirm|affirm|100.0%|✅|
|🟢|news|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|no ma'am|deny|deny|100.0%|✅|
|🟢|hello Sara|greet|greet|100.0%|✅|
|🟢|hey rasa|greet|greet|100.0%|✅|
|🟢|rasa php|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|Can I speak to a human?|human_handoff|human_handoff|100.0%|✅|
|🟢|I don’t understand intent classification|nlu_info|nlu_info|100.0%|✅|
|🟢|How to get start|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|does rasa aid other languages?|faq/languages|faq/languages|100.0%|✅|
|🟢|how to get start|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|give me your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|and what are slots|faq/slots|faq/slots|100.0%|✅|
|🟢|and what are slots?|faq/slots|faq/slots|100.0%|✅|
|🟢|sfasd|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Whats the cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|how can you tell me what a slot is ?|faq/slots|faq/slots|100.0%|✅|
|🟢|No|deny|deny|100.0%|✅|
|🟢|No.|deny|deny|100.0%|✅|
|🟢|work with buttons?|technical_question|technical_question|100.0%|✅|
|🟢|is rasa core able to run standalone?|technical_question|technical_question|100.0%|✅|
|🟢|sign me up for the newsletter - my email is Carolyn_Caskey@yahoo.com|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|When is it that the next event occurs?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|i need to speak to your sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|well yes|affirm|affirm|100.0%|✅|
|🟢|how does rasa playground relate to rasa core|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|chào|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|yes great|affirm|affirm|100.0%|✅|
|🟢|is it for free?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|I want to install Rasa Core|install_rasa|install_rasa|100.0%|✅|
|🟢|i'm migrating from LUIS|switch|switch|100.0%|✅|
|🟢|how to restart story if am drooping in between|technical_question|technical_question|100.0%|✅|
|🟢|Oh yes|affirm|affirm|100.0%|✅|
|🟢|what python version do i install|faq/python_version|faq/python_version|100.0%|✅|
|🟢|I have a problem|technical_question|technical_question|100.0%|✅|
|🟢|Will we build a snowman today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|Lol thats funny|react_positive|react_positive|100.0%|✅|
|🟢|Whatever it costs|enter_data|enter_data|100.0%|✅|
|🟢|I want to learn about entity recognition|nlu_info|nlu_info|100.0%|✅|
|🟢|yes,i am|affirm|affirm|100.0%|✅|
|🟢|What's it like out there?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|what are all the things you understand?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|you are great|react_positive|react_positive|100.0%|✅|
|🟢|tudo bom|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|What communication channels are supported by rasa?|faq/channels|faq/channels|100.0%|✅|
|🟢|Specify how you were created?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|again?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|channels supported by Rasa|faq/channels|faq/channels|100.0%|✅|
|🟢|Hi Sara|greet|greet|100.0%|✅|
|🟢|Hi Sara!|greet|greet|100.0%|✅|
|🟢|h r u ?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|yay|affirm|affirm|100.0%|✅|
|🟢|Lol|react_positive|react_positive|100.0%|✅|
|🟢|At what time is the next event scheduled?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|hello sweet boy|greet|greet|100.0%|✅|
|🟢|book a sales|contact_sales|contact_sales|100.0%|✅|
|🟢|yeeees|affirm|affirm|100.0%|✅|
|🟢|whats popping|greet|greet|100.0%|✅|
|🟢|why to use rasa|why_rasa|why_rasa|100.0%|✅|
|🟢|Hoe do I install Rasa X|install_rasa|install_rasa|100.0%|✅|
|🟢|i'd like to get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|whats the diff between rasa and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|id like a call please|contact_sales|contact_sales|100.0%|✅|
|🟢|what database rasa use|technical_question|technical_question|100.0%|✅|
|🟢|jezz|affirm|affirm|100.0%|✅|
|🟢|can you pint me to a good how-to online about Rasa|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|how to use rasa caht in react application|faq/channels|faq/channels|100.0%|✅|
|🟢|Rasa Playground|enter_data|enter_data|100.0%|✅|
|🟢|help mi with slots|faq/slots|faq/slots|100.0%|✅|
|🟢|yes please|affirm|affirm|100.0%|✅|
|🟢|yes please!|affirm|affirm|100.0%|✅|
|🟢|cool|react_positive|react_positive|100.0%|✅|
|🟢|cool :)|react_positive|react_positive|100.0%|✅|
|🟢|cool!|react_positive|react_positive|100.0%|✅|
|🟢|nah I'm good|deny|deny|100.0%|✅|
|🟢|I want to do a Rasa Stack installation|install_rasa|install_rasa|100.0%|✅|
|🟢|rasa components|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|difference between rasa core and nlu|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|hey ther|greet|greet|100.0%|✅|
|🟢|what is intent classification?|nlu_info|nlu_info|100.0%|✅|
|🟢|contact|contact_sales|contact_sales|100.0%|✅|
|🟢|oh super|affirm|affirm|100.0%|✅|
|🟢|you are awesome|react_positive|react_positive|100.0%|✅|
|🟢|yeeeeezzzzz|affirm|affirm|100.0%|✅|
|🟢|How old are you?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|how old are you|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|how old are you?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|how can i get data from a database and use them as a response to a question?|technical_question|technical_question|100.0%|✅|
|🟢|see playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|come stai?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|can someone help me with infos about rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|describe the word slot please|faq/slots|faq/slots|100.0%|✅|
|🟢|Never|deny|deny|100.0%|✅|
|🟢|I want to know how to get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Tell me about the entity extraction|nlu_info|nlu_info|100.0%|✅|
|🟢|From where did you come?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|Where did you come from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|where did you come from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|What's the size of the community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|how to install rasa on windows?|install_rasa|install_rasa|100.0%|✅|
|🟢|can i makae rest calls|technical_question|technical_question|100.0%|✅|
|🟢|get me the sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|nothing|enter_data|enter_data|100.0%|✅|
|🟢|install|install_rasa|install_rasa|100.0%|✅|
|🟢|none of them|deny|deny|100.0%|✅|
|🟢|How did they make you?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|you are funny|react_positive|react_positive|100.0%|✅|
|🟢|i want to build an insurance bot|enter_data|enter_data|100.0%|✅|
|🟢|components in rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|no sir|deny|deny|100.0%|✅|
|🟢|start|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to restart rasax|technical_question|technical_question|100.0%|✅|
|🟢|subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|php code|technical_question|technical_question|100.0%|✅|
|🟢|Hieee|greet|greet|100.0%|✅|
|🟢|Hi, how can i get started with rasa x|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how do you do?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|Where is the restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|is Rasa X separate from Rasa?|faq/rasax|faq/rasax|100.0%|✅|
|🟢|I want to use pip|enter_data|enter_data|100.0%|✅|
|🟢|you sound like a real human|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|What do you do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what do you do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what do you do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|hi how u doing|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|no|deny|deny|100.0%|✅|
|🟢|no :(|deny|deny|100.0%|✅|
|🟢|no!!!!|deny|deny|100.0%|✅|
|🟢|whats rasaplayground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|Subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|How many people are here?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|no i dont want to accept :P lol|deny|deny|100.0%|✅|
|🟢|newsletter registration first|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|In Rasa, what are slots used for?|faq/slots|faq/slots|100.0%|✅|
|🟢|go ahead|affirm|affirm|100.0%|✅|
|🟢|I'd like to perform an installation of Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|🟢|how do I start|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|why do I need rasa|why_rasa|why_rasa|100.0%|✅|
|🟢|I'm a construction worker|enter_data|enter_data|100.0%|✅|
|🟢|May i know my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|nop|deny|deny|100.0%|✅|
|🟢|tell me more about NLU|faq/nlu|faq/nlu|100.0%|✅|
|🟢|I accept|affirm|affirm|100.0%|✅|
|🟢|I accept.|affirm|affirm|100.0%|✅|
|🟢|Time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|time|enter_data|chitchat/ask_time|100.0%|❌|
|🟢|ça va ?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|🟢|Can you send messages based on events?|technical_question|technical_question|100.0%|✅|
|🟢|what's my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|OK can u brief me Abt rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|I need to install Rasa Core.|install_rasa|install_rasa|100.0%|✅|
|🟢|lets try the newsletter registration|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|show me restaurents|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|How i install|install_rasa|install_rasa|100.0%|✅|
|🟢|switching from DialogFlow|switch|switch|100.0%|✅|
|🟢|hello world|greet|greet|100.0%|✅|
|🟢|I also want to subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|What do I call myself?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|I want to subscribing to the Rasa newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|that was a great interaction|react_positive|react_positive|100.0%|✅|
|🟢|thats funny|react_positive|react_positive|100.0%|✅|
|🟢|I need Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|🟢|I need Rasa Stack.|install_rasa|install_rasa|100.0%|✅|
|🟢|No, not really.|deny|deny|100.0%|✅|
|🟢|yes that's great|affirm|affirm|100.0%|✅|
|🟢|ha ha|react_positive|react_positive|100.0%|✅|
|🟢|Is the Rasa community small?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|I'd like to know the meaning of slots|faq/slots|faq/slots|100.0%|✅|
|🟢|I am using it|affirm|affirm|100.0%|✅|
|🟢|I'd like to install Rasa Core|install_rasa|install_rasa|100.0%|✅|
|🟢|you are so smart|react_positive|react_positive|100.0%|✅|
|🟢|i am using rasa, why would i need rasa x?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|custom connection|faq/channels|faq/channels|100.0%|✅|
|🟢|I don’t understand how you handle entity recognition at Rasa|nlu_info|nlu_info|100.0%|✅|
|🟢|perfect|affirm|affirm|100.0%|✅|
|🟢|Okay|affirm|affirm|100.0%|✅|
|🟢|Okay!|affirm|affirm|100.0%|✅|
|🟢|where can i fid tutorials for rasa|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|I'd like to handle chitchat|technical_question|technical_question|100.0%|✅|
|🟢|how do I install Rasa|install_rasa|install_rasa|100.0%|✅|
|🟢|no. u r idiot|deny|deny|100.0%|✅|
|🟢|can you tell me what my identity is?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|how rasa works ?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|how works rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|call|contact_sales|contact_sales|100.0%|✅|
|🟢|What city are you in?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|si|affirm|affirm|100.0%|✅|
|🟢|Is the community large?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|do you know chinese|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|it sucks|deny|deny|100.0%|✅|
|🟢|Installing rasa|install_rasa|install_rasa|100.0%|✅|
|🟢|yes baby|affirm|affirm|100.0%|✅|
|🟢|Can we make Japanese speaking bot with Rasa?|faq/languages|faq/languages|100.0%|✅|
|🟢|the bot like you|enter_data|enter_data|100.0%|✅|
|🟢|WOW|react_positive|react_positive|100.0%|✅|
|🟢|the intent|nlu_info|nlu_info|100.0%|✅|
|🟢|can you explain what the events are?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|Yup|affirm|affirm|100.0%|✅|
|🟢|ah ok|affirm|affirm|100.0%|✅|
|🟢|your cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|Help me install Rasa|install_rasa|install_rasa|100.0%|✅|
|🟢|tell me bout rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|is rasa open source needed for rasa x?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|Did you know about Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|why use rasa|why_rasa|why_rasa|100.0%|✅|
|🟢|But I wanted a sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|Do you  help to  integrate Facebook|faq/channels|faq/channels|100.0%|✅|
|🟢|no, i hate it|deny|deny|100.0%|✅|
|🟢|i want to learn about rasa nlu|faq/nlu|faq/nlu|100.0%|✅|
|🟢|no way|deny|deny|100.0%|✅|
|🟢|tell me how old you are?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|What is my full name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|hello is anybody there|greet|greet|100.0%|✅|
|🟢|how to start with it|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Is it raining|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|Is it raining?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|how does Rasa X work?|faq/rasax|faq/rasax|100.0%|✅|
|🟢|i want a tutorial of rasa|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|I'd like to subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|LOL|react_positive|react_positive|100.0%|✅|
|🟢|gimme a proper human|human_handoff|human_handoff|100.0%|✅|
|🟢|are u human|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|how are things with you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|rasa enterprise plans|faq/ee|faq/ee|100.0%|✅|
|🟢|Say my name.|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|Neither|deny|deny|100.0%|✅|
|🟢|sign up|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|hey are you human|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|it sux|deny|deny|100.0%|✅|
|🟢|i want to subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Can Rasa be incorporated into iOS apps?|technical_question|technical_question|100.0%|✅|
|🟢|What can rasa do?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what's the purpose of Rasa Playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|where do i download rasa|install_rasa|install_rasa|100.0%|✅|
|🟢|How do I start|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|what can I do in your community's forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|a pizza bot|enter_data|enter_data|100.0%|✅|
|🟢|can you help me get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|How about hindi?|faq/languages|faq/languages|100.0%|✅|
|🟢|hell yes|affirm|affirm|100.0%|✅|
|🟢|why rasa|why_rasa|why_rasa|100.0%|✅|
|🟢|i would like more explanation on RASA Core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|in which langauges can i build a rasa bot|faq/languages|faq/languages|100.0%|✅|
|🟢|ok, well, then a sales call with the fabulous Theodora Estrada|contact_sales|contact_sales|100.0%|✅|
|🟢|that's annoying I'd like to speak to someone real|human_handoff|human_handoff|100.0%|✅|
|🟢|why to use RASA|why_rasa|why_rasa|100.0%|✅|
|🟢|can someone help me with infos about rasa x|faq/rasax|faq/rasax|100.0%|✅|
|🟢|How were you materialized?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|Hi bot|greet|greet|100.0%|✅|
|🟢|Hi, bot|greet|greet|100.0%|✅|
|🟢|Nopes|deny|deny|100.0%|✅|
|🟢|ya|affirm|affirm|100.0%|✅|
|🟢|i want on this dope newsletter - my email is R_Grove@gmail.com|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|no i can't|deny|deny|100.0%|✅|
|🟢|intent|nlu_info|nlu_info|100.0%|✅|
|🟢|you are my new bestfriend|react_positive|react_positive|100.0%|✅|
|🟢|I would like to talk to someone from your sales team|contact_sales|contact_sales|100.0%|✅|
|🟢|where do i start?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|hm intents?|nlu_info|nlu_info|100.0%|✅|
|🟢|Bom dia|greet|greet|100.0%|✅|
|🟢|can i programm a vocal assistant|faq/voice|faq/voice|100.0%|✅|
|🟢|Thank you in advance for suggesting I install Rasa NLU.|install_rasa|install_rasa|100.0%|✅|
|🟢|migration from dialogflow|switch|switch|100.0%|✅|
|🟢|tell me what my identity is?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|how do i install|install_rasa|install_rasa|100.0%|✅|
|🟢|Ok I want to talk to your sales team immediately|contact_sales|contact_sales|100.0%|✅|
|🟢|a slot is what|faq/slots|faq/slots|100.0%|✅|
|🟢|what is a slot?|faq/slots|faq/slots|100.0%|✅|
|🟢|yes i wanna know more about rasa nlu|faq/nlu|faq/nlu|100.0%|✅|
|🟢|i am feel sad|react_negative|react_negative|100.0%|✅|
|🟢|yep thats cool|affirm|affirm|100.0%|✅|
|🟢|Wow|react_positive|react_positive|100.0%|✅|
|🟢|why is Rasa useful|why_rasa|why_rasa|100.0%|✅|
|🟢|NEIN|deny|deny|100.0%|✅|
|🟢|hi mrs rasa|greet|greet|100.0%|✅|
|🟢|I need to know about slot filling|faq/slots|faq/slots|100.0%|✅|
|🟢|can I talk to human?|human_handoff|human_handoff|100.0%|✅|
|🟢|can I talk to human|human_handoff|human_handoff|100.0%|✅|
|🟢|what chat services do you support|faq/channels|faq/channels|100.0%|✅|
|🟢|Where were you born?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|Tutorials for learning rasa ?|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|I want to talk to someone about your pricing system|contact_sales|contact_sales|100.0%|✅|
|🟢|How to migrate from DialogFlwo|switch|switch|100.0%|✅|
|🟢|hello everybody|greet|greet|100.0%|✅|
|🟢|newsletter it is|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|yes I do|affirm|affirm|100.0%|✅|
|🟢|how to install on window|install_rasa|install_rasa|100.0%|✅|
|🟢|i want to learn something about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|tell me about nlu|faq/nlu|faq/nlu|100.0%|✅|
|🟢|are you bilingual?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|please compare rasa and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|yep|affirm|affirm|100.0%|✅|
|🟢|yep. :/|affirm|affirm|100.0%|✅|
|🟢|What sets nlu apart from core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|yep i want that|affirm|affirm|100.0%|✅|
|🟢|neither|deny|deny|100.0%|✅|
|🟢|hi friends|greet|greet|100.0%|✅|
|🟢|How did you come to be?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|we cant converse in french?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|hi Mister|greet|greet|100.0%|✅|
|🟢|Sign up.|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|its okay|affirm|affirm|100.0%|✅|
|🟢|How did you come into being?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|Get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|i would like to know how to get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|hello sweatheart|greet|greet|100.0%|✅|
|🟢|i need help with policies|technical_question|technical_question|100.0%|✅|
|🟢|What messaging systems are supported by rasa?|faq/channels|faq/channels|100.0%|✅|
|🟢|oh good !!|affirm|affirm|100.0%|✅|
|🟢|when is our next group event going to take place?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|Where might you be from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|Hola|greet|greet|100.0%|✅|
|🟢|I want to know about rsa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|i need a good tutorial for rasa|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|n|deny|deny|100.0%|✅|
|🟢|get me some tutorials|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|I need assistance in getting Rasa Stack.|install_rasa|install_rasa|100.0%|✅|
|🟢|how do i build a bot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how do i build a bot?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how is intent classification managed in rasa?|nlu_info|nlu_info|100.0%|✅|
|🟢|lol|react_positive|react_positive|100.0%|✅|
|🟢|im migrating from dialogflow|switch|switch|100.0%|✅|
|🟢|let me speak to a real person please|human_handoff|human_handoff|100.0%|✅|
|🟢|Can i use NLU on its own|technical_question|technical_question|100.0%|✅|
|🟢|basic tutorials|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|ja|affirm|affirm|100.0%|✅|
|🟢|ys|affirm|affirm|100.0%|✅|
|🟢|i need your data source|contact_sales|contact_sales|100.0%|✅|
|🟢|I wrote it in german|enter_data|enter_data|100.0%|✅|
|🟢|Im looking for some tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|I want to build RASA DIET in google colab|technical_question|technical_question|100.0%|✅|
|🟢|i would like to subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|What languages does rasa work with?|faq/languages|faq/languages|100.0%|✅|
|🟢|why RASA?|why_rasa|why_rasa|100.0%|✅|
|🟢|Good morning|greet|greet|100.0%|✅|
|🟢|how is it going|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|an explanation of how entity recognition work would help|nlu_info|nlu_info|100.0%|✅|
|🟢|Does Rasa have the functionality of being able to set up the bot on web pages?|faq/channels|faq/channels|100.0%|✅|
|🟢|i want to receive your nl|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|accepted|affirm|affirm|100.0%|✅|
|🟢|Where to run rasa init command ?|technical_question|technical_question|100.0%|✅|
|🟢|I still don’t get how entity recognition works|nlu_info|nlu_info|100.0%|✅|
|🟢|is there a tutorial for this?|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|subscribe my email Evan@Palmer.net to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Are you free?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|are you free ?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|how can i setup rasa in django project ?|faq/channels|faq/channels|100.0%|✅|
|🟢|definitely yes without a doubt|affirm|affirm|100.0%|✅|
|🟢|non|deny|deny|100.0%|✅|
|🟢|Rara, are you a human?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|compnnent of rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|I want Vietnamese language processing|faq/languages|faq/languages|100.0%|✅|
|🟢|Yes please|affirm|affirm|100.0%|✅|
|🟢|Yes please!|affirm|affirm|100.0%|✅|
|🟢|I have decided on Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|🟢|Yes I do|affirm|affirm|100.0%|✅|
|🟢|let me speak to a real person|human_handoff|human_handoff|100.0%|✅|
|🟢|ok friend|affirm|affirm|100.0%|✅|
|🟢|what about nlu?|faq/nlu|faq/nlu|100.0%|✅|
|🟢|now what?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|fair enough|affirm|affirm|100.0%|✅|
|🟢|I think I want to install Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|🟢|I want to build an FAQ bot|enter_data|enter_data|100.0%|✅|
|🟢|what is rasa x enterprise|faq/ee|faq/ee|100.0%|✅|
|🟢|why should i use rasa instead of google dialogflow|why_rasa|why_rasa|100.0%|✅|
|🟢|i want to know how can buld my own bot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Are u developed in rasa|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|how to use|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|sales team connection|contact_sales|contact_sales|100.0%|✅|
|🟢|sorry its ner|nlu_info|nlu_info|100.0%|✅|
|🟢|I want to install Rasa X|install_rasa|install_rasa|100.0%|✅|
|🟢|i want to run rasa x in ibm cloud|technical_question|technical_question|100.0%|✅|
|🟢|hi folks|greet|greet|100.0%|✅|
|🟢|wow|react_positive|react_positive|100.0%|✅|
|🟢|why only rasa|why_rasa|why_rasa|100.0%|✅|
|🟢|What do you know about rasa meetups?|ask_which_events|ask_which_events|100.0%|✅|
|🟢|ofcourse|affirm|affirm|100.0%|✅|
|🟢|how about nlu|faq/nlu|faq/nlu|100.0%|✅|
|🟢|Why choose rasa?|why_rasa|why_rasa|100.0%|✅|
|🟢|Ofcourse|affirm|affirm|100.0%|✅|
|🟢|nö|deny|deny|100.0%|✅|
|🟢|I checked the documentation on entity recognition but I still don’t understand it|nlu_info|nlu_info|100.0%|✅|
|🟢|Give me a description of slots.|faq/slots|faq/slots|100.0%|✅|
|🟢|what is the policy|technical_question|technical_question|100.0%|✅|
|🟢|i'd rather speak with a real rasa employee|human_handoff|human_handoff|100.0%|✅|
|🟢|I need to get Rasa Stack up and running.|install_rasa|install_rasa|100.0%|✅|
|🟢|i want to buy the rasa platform|contact_sales|contact_sales|100.0%|✅|
|🟢|can i run rasa on my computer?|install_rasa|install_rasa|100.0%|✅|
|🟢|I use DialogFlow|switch|switch|100.0%|✅|
|🟢|yes i have built a bot before|affirm|affirm|100.0%|✅|
|🟢|i decline|deny|deny|100.0%|✅|
|🟢|what sets rasa apart?|why_rasa|why_rasa|100.0%|✅|
|🟢|I want to buy the rasa platform|contact_sales|contact_sales|100.0%|✅|
|🟢|can someone call me please?|contact_sales|contact_sales|100.0%|✅|
|🟢|how to write stories to train rasa|technical_question|technical_question|100.0%|✅|
|🟢|how to get started with nlu|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how do i migrate from dialogflow|switch|switch|100.0%|✅|
|🟢|Hows it going|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|Why rasa?|why_rasa|why_rasa|100.0%|✅|
|🟢|Sure, give me the basics|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|nope|deny|deny|100.0%|✅|
|🟢|nope!|deny|deny|100.0%|✅|
|🟢|you seem pretty cool :D|react_positive|react_positive|100.0%|✅|
|🟢|i am!|affirm|affirm|100.0%|✅|
|🟢|What's rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|i am very sad|react_negative|react_negative|100.0%|✅|
|🟢|new|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how about the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|i am switching from luis|switch|switch|100.0%|✅|
|🟢|yyeeeh|affirm|affirm|100.0%|✅|
|🟢|alright, cool|affirm|affirm|100.0%|✅|
|🟢|yes I would like to subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Can I use Rasa X without using Rasa?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|So I'm here Today to ask one very simple question, what are you ?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|one which asks me loads about myself|enter_data|enter_data|100.0%|✅|
|🟢|can we use regex is rasa code|technical_question|technical_question|100.0%|✅|
|🟢|tell me more about your company|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|yes it was okay|affirm|affirm|100.0%|✅|
|🟢|I'm interested in server installation|enter_data|enter_data|100.0%|✅|
|🟢|you have speech recognition?|faq/voice|faq/voice|100.0%|✅|
|🟢|yas|affirm|affirm|100.0%|✅|
|🟢|tell me about intent classification|nlu_info|nlu_info|100.0%|✅|
|🟢|I want information about rasa x|faq/rasax|faq/rasax|100.0%|✅|
|🟢|i'd like your newspaper please|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|confirm|affirm|affirm|100.0%|✅|
|🟢|kk|affirm|affirm|100.0%|✅|
|🟢|having some problems with installation|install_rasa|install_rasa|100.0%|✅|
|🟢|migration from LUIS|switch|switch|100.0%|✅|
|🟢|how to initialize a new project?|technical_question|technical_question|100.0%|✅|
|🟢|how can i install rasa|install_rasa|install_rasa|100.0%|✅|
|🟢|I changed my mind. I want to accept it|affirm|affirm|100.0%|✅|
|🟢|What is your birthdate?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|are you human|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|Are you human?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|Are you human ?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|are you human ?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|Do you know my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|DOES RASA SUPPORT SMS?|faq/channels|faq/channels|100.0%|✅|
|🟢|no, i want to talk to human|human_handoff|human_handoff|100.0%|✅|
|🟢|how have you been built?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|how does this work?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|I want to learn about intent classification|nlu_info|nlu_info|100.0%|✅|
|🟢|how long to train|technical_question|technical_question|100.0%|✅|
|🟢|Can you help me to install Rasa?|install_rasa|install_rasa|100.0%|✅|
|🟢|What makes core and nlu incompatible?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|are you build with rasa ?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|why switch?|why_rasa|why_rasa|100.0%|✅|
|🟢|What language is the open source coding done in?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|🟢|how many people are using Rasa|faq/community_size|faq/community_size|100.0%|✅|
|🟢|how aold are you|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|does the open source version have core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|nein|deny|deny|100.0%|✅|
|🟢|why should i choose rasa|why_rasa|why_rasa|100.0%|✅|
|🟢|y|affirm|affirm|100.0%|✅|
|🟢|hi friend|greet|greet|100.0%|✅|
|🟢|I meant why you over competitors ?|why_rasa|why_rasa|100.0%|✅|
|🟢|how to build a chatbot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|greetings|greet|greet|100.0%|✅|
|🟢|does rasa support voice input|faq/voice|faq/voice|100.0%|✅|
|🟢|I need to know if I can use Rasa to build an application?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Can I talk to a human|human_handoff|human_handoff|100.0%|✅|
|🟢|rasa tutorials|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|it's not working|broken|broken|100.0%|✅|
|🟢|How can I visualise conversation flow?|technical_question|technical_question|100.0%|✅|
|🟢|are u a real person?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|kiss me|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|i would like to speak to a person|human_handoff|human_handoff|100.0%|✅|
|🟢|you are a human|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|are you a human ?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|how to install the rasa stack|install_rasa|install_rasa|100.0%|✅|
|🟢|good morning|greet|greet|100.0%|✅|
|🟢|Is rasa community big?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|i want a tutorial on rasa nlu|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|how to restart the rasa|technical_question|technical_question|100.0%|✅|
|🟢|Is it better to use rasa or luis?|why_rasa|why_rasa|100.0%|✅|
|🟢|yres|affirm|affirm|100.0%|✅|
|🟢|could you elaborate more about rasa x|faq/rasax|faq/rasax|100.0%|✅|
|🟢|Do you have friends the same age as you, if so, how old are they?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|what is action server|technical_question|technical_question|100.0%|✅|
|🟢|is everything all right|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|tell me about the nlu training data format|technical_question|technical_question|100.0%|✅|
|🟢|come back|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|why is rasa a good nlp libarary|why_rasa|why_rasa|100.0%|✅|
|🟢|What is the Similarities between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|let me talk to a human|human_handoff|human_handoff|100.0%|✅|
|🟢|what about signing up for the newsletter?|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|hi there|greet|greet|100.0%|✅|
|🟢|how to evaluate model|technical_question|technical_question|100.0%|✅|
|🟢|can i talk to human|human_handoff|human_handoff|100.0%|✅|
|🟢|where can i learn to build a chatbot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|more about NLU please|faq/nlu|faq/nlu|100.0%|✅|
|🟢|can you explain rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|such a great demo|react_positive|react_positive|100.0%|✅|
|🟢|how many forum members do you have|faq/community_size|faq/community_size|100.0%|✅|
|🟢|i need the call request|contact_sales|contact_sales|100.0%|✅|
|🟢|I need a expert opinion on slots.|faq/slots|faq/slots|100.0%|✅|
|🟢|Voice in Rasa|faq/voice|faq/voice|100.0%|✅|
|🟢|subscrime me|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|How can I assist the cause?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|what you doing?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|What does Rasa cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|no, thankyou|deny|deny|100.0%|✅|
|🟢|can i user rasa for my text classification problem?|technical_question|technical_question|100.0%|✅|
|🟢|yep that's nice|affirm|affirm|100.0%|✅|
|🟢|I don't agree|deny|deny|100.0%|✅|
|🟢|How do I download rasa ?|install_rasa|install_rasa|100.0%|✅|
|🟢|i want to learn about nlu|faq/nlu|faq/nlu|100.0%|✅|
|🟢|ya go for it|affirm|affirm|100.0%|✅|
|🟢|no sorry|deny|deny|100.0%|✅|
|🟢|what is rasa x ?|faq/rasax|faq/rasax|100.0%|✅|
|🟢|ye splease|affirm|affirm|100.0%|✅|
|🟢|what is Rasa X ?|faq/rasax|faq/rasax|100.0%|✅|
|🟢|What do you speak?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|i guess it means - no|deny|deny|100.0%|✅|
|🟢|bash: poetry: command not found|technical_question|technical_question|100.0%|✅|
|🟢|how are you Rasa|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|a little|affirm|affirm|100.0%|✅|
|🟢|of course|affirm|affirm|100.0%|✅|
|🟢|can rasa run standalone|technical_question|technical_question|100.0%|✅|
|🟢|talk with a human|human_handoff|human_handoff|100.0%|✅|
|🟢|does rasa work with duckling?|nlu_info|nlu_info|100.0%|✅|
|🟢|am struck with installation|install_rasa|install_rasa|100.0%|✅|
|🟢|how enttity extrcation works|nlu_info|nlu_info|100.0%|✅|
|🟢|How many languages does Spacy support?|technical_question|technical_question|100.0%|✅|
|🟢|Can I ask you something about weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|more about nlu|faq/nlu|faq/nlu|100.0%|✅|
|🟢|rasa bot tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|i want to know more about NLU|faq/nlu|faq/nlu|100.0%|✅|
|🟢|I want to know more about NLU|faq/nlu|faq/nlu|100.0%|✅|
|🟢|yeah sure|affirm|affirm|100.0%|✅|
|🟢|How many years have you lived?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|Subscribe to Rasa newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|yes.I.would.like.to.subscrbe|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|tell me what is rasa x|faq/rasax|faq/rasax|100.0%|✅|
|🟢|entity recognition - what is that?|nlu_info|nlu_info|100.0%|✅|
|🟢|Do you know what my name is?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|i want to know how to start with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|yeah how about the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|never|deny|deny|100.0%|✅|
|🟢|What is the rough size of the community?|faq/community_size|faq/community_size|100.0%|✅|
|🟢|when you were bon|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|What is the difference between entities and slots?|technical_question|technical_question|100.0%|✅|
|🟢|and you|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|do you use duckling|nlu_info|nlu_info|100.0%|✅|
|🟢|different parts of Rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|it is in german|enter_data|enter_data|100.0%|✅|
|🟢|i feel sad|react_negative|react_negative|100.0%|✅|
|🟢|rasa enterprise please|faq/ee|faq/ee|100.0%|✅|
|🟢|duckling|nlu_info|nlu_info|100.0%|✅|
|🟢|yes you can|affirm|affirm|100.0%|✅|
|🟢|how can create multilingual chatbor|technical_question|technical_question|100.0%|✅|
|🟢|intent please|nlu_info|nlu_info|100.0%|✅|
|🟢|How can I be more involved?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|how do I build a bot?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|I get it|affirm|affirm|100.0%|✅|
|🟢|i wanna try rasa nlu|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Yes, I want to know more about NLU|faq/nlu|faq/nlu|100.0%|✅|
|🟢|I want to integrate a database and look up values based on an entity the user gave me. How is this possible?|technical_question|technical_question|100.0%|✅|
|🟢|can we converse in french?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|what is rasa x ee?|faq/ee|faq/ee|100.0%|✅|
|🟢|does rasa works in spanish|faq/languages|faq/languages|100.0%|✅|
|🟢|I require Rasa Stack?|install_rasa|install_rasa|100.0%|✅|
|🟢|how to restart rasa|technical_question|technical_question|100.0%|✅|
|🟢|how to restart rasa?|technical_question|technical_question|100.0%|✅|
|🟢|which python is rasa using?|faq/python_version|faq/python_version|100.0%|✅|
|🟢|ok sales|contact_sales|contact_sales|100.0%|✅|
|🟢|restaurants|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|what version of python|faq/python_version|faq/python_version|100.0%|✅|
|🟢|accept|affirm|affirm|100.0%|✅|
|🟢|Good Morning|greet|greet|100.0%|✅|
|🟢|install Rasa on Mac|install_rasa|install_rasa|100.0%|✅|
|🟢|oki doki|affirm|affirm|100.0%|✅|
|🟢|which are the slots?|faq/slots|faq/slots|100.0%|✅|
|🟢|What time do we have?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|tell me about rasa enterpeise|faq/ee|faq/ee|100.0%|✅|
|🟢|yes cool|affirm|affirm|100.0%|✅|
|🟢|yes, cool|affirm|affirm|100.0%|✅|
|🟢|add me as your subscriber|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|fine|affirm|affirm|100.0%|✅|
|🟢|i want a tutorial on nlu|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|I do|affirm|affirm|100.0%|✅|
|🟢|How to migrate from DialogFlow?|switch|switch|100.0%|✅|
|🟢|switch from dilogueflow|switch|switch|100.0%|✅|
|🟢|do u know Alexa?|faq/voice|faq/voice|100.0%|✅|
|🟢|oui|affirm|affirm|100.0%|✅|
|🟢|i am very happy with your response|react_positive|react_positive|100.0%|✅|
|🟢|na|deny|deny|100.0%|✅|
|🟢|I currently use LUIS|switch|switch|100.0%|✅|
|🟢|I would like to know more about RASA NLU|faq/nlu|faq/nlu|100.0%|✅|
|🟢|What does everyone call me?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|i want subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|nlu|enter_data|enter_data|100.0%|✅|
|🟢|you are realy intelligent|react_positive|react_positive|100.0%|✅|
|🟢|DialogFlow|switch|switch|100.0%|✅|
|🟢|I'm sure I will!|affirm|affirm|100.0%|✅|
|🟢|I am trying to build a bot using rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to migrate to dialogueflow|switch|switch|100.0%|✅|
|🟢|why people go for Rasa chatbot?|why_rasa|why_rasa|100.0%|✅|
|🟢|I'm super sad|react_negative|react_negative|100.0%|✅|
|🟢|I checked the documentation on intent classification but I still don’t understand it|nlu_info|nlu_info|100.0%|✅|
|🟢|which slots are there?|faq/slots|faq/slots|100.0%|✅|
|🟢|Yeah sure|affirm|affirm|100.0%|✅|
|🟢|How do I build a bot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Can you tell me my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|can you tell me my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|Can I build a FAQ robot with Rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|How to migrate from DialogFlow to Rasa?|switch|switch|100.0%|✅|
|🟢|i would just like to have the link for the community|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|🟢|rasa core vs rasa nlu|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|I am facing some issues with LMS|technical_question|technical_question|100.0%|✅|
|🟢|fcourse|affirm|affirm|100.0%|✅|
|🟢|yes i have!|affirm|affirm|100.0%|✅|
|🟢|how can i migrate from dialogflow?|switch|switch|100.0%|✅|
|🟢|I wanna have a subscription for your product|contact_sales|contact_sales|100.0%|✅|
|🟢|why should I switch to rasa?|why_rasa|why_rasa|100.0%|✅|
|🟢|what is the difference between rasa and rasax|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|can yiu send me a tutorial?|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|this sucks|deny|deny|100.0%|✅|
|🟢|i want to buy the enterprise edition|contact_sales|contact_sales|100.0%|✅|
|🟢|im moving luis|switch|switch|100.0%|✅|
|🟢|what is the different|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|can this be integrated with mongo db|technical_question|technical_question|100.0%|✅|
|🟢|okay Rasabot, you're cool|react_positive|react_positive|100.0%|✅|
|🟢|never mind|deny|deny|100.0%|✅|
|🟢|why should I switch|why_rasa|why_rasa|100.0%|✅|
|🟢|Can you tell me about the enterprise edition?|faq/ee|faq/ee|100.0%|✅|
|🟢|i want some tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|spanish|enter_data|enter_data|100.0%|✅|
|🟢|I currently use dialog flow|switch|switch|100.0%|✅|
|🟢|I want to switch from dialog flow|switch|switch|100.0%|✅|
|🟢|Who could I be?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|any tutorials on using rasa?|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|sort of|affirm|affirm|100.0%|✅|
|🟢|tell me what's your skill|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|is it hot ?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|no thanks|deny|deny|100.0%|✅|
|🟢|no, thanks|deny|deny|100.0%|✅|
|🟢|does it support AI|technical_question|technical_question|100.0%|✅|
|🟢|i'm sad|react_negative|react_negative|100.0%|✅|
|🟢|ey boss|greet|greet|100.0%|✅|
|🟢|hi im Amanda Anderson|greet|greet|100.0%|✅|
|🟢|Nah|deny|deny|100.0%|✅|
|🟢|who may i ?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|start rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|i need to know how i can book support|contact_sales|contact_sales|100.0%|✅|
|🟢|I'm sad|react_negative|react_negative|100.0%|✅|
|🟢|Are Rasa and Rasa X the same thing?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|Well hello there ;)|greet|greet|100.0%|✅|
|🟢|download|install_rasa|install_rasa|100.0%|✅|
|🟢|why is rasa interesting|why_rasa|why_rasa|100.0%|✅|
|🟢|how do you integrate duckling|nlu_info|nlu_info|100.0%|✅|
|🟢|i am feeling happy|react_positive|react_positive|100.0%|✅|
|🟢|how to add in my website|technical_question|technical_question|100.0%|✅|
|🟢|deny|deny|deny|100.0%|✅|
|🟢|:)|react_positive|react_positive|100.0%|✅|
|🟢|adios|bye|bye|100.0%|✅|
|🟢|adios?|bye|bye|100.0%|✅|
|🟢|hèhè|react_positive|react_positive|100.0%|✅|
|🟢|getting some error|technical_question|technical_question|100.0%|✅|
|🟢|More a less|affirm|affirm|100.0%|✅|
|🟢|i'm looking for the youtube tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|How to install rasa|install_rasa|install_rasa|100.0%|✅|
|🟢|NER|nlu_info|nlu_info|100.0%|✅|
|🟢|lets do it|affirm|affirm|100.0%|✅|
|🟢|try out online|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|download the tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|How to migrate a bot from DialogFlow to Rasa?|switch|switch|100.0%|✅|
|🟢|can I migrate to rasa from another tool?|switch|switch|100.0%|✅|
|🟢|where are from|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|more about NLU|faq/nlu|faq/nlu|100.0%|✅|
|🟢|More about NLU|faq/nlu|faq/nlu|100.0%|✅|
|🟢|Could I talk to Tyrone King?|human_handoff|human_handoff|100.0%|✅|
|🟢|socket io|faq/channels|faq/channels|100.0%|✅|
|🟢|an explanation of how intent classification work would help|nlu_info|nlu_info|100.0%|✅|
|🟢|Can i talk to a human instead|human_handoff|human_handoff|100.0%|✅|
|🟢|why to use rasa over other available platform|why_rasa|why_rasa|100.0%|✅|
|🟢|heyho|greet|greet|100.0%|✅|
|🟢|pls explain how to get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|what is rasa nlu?|faq/nlu|faq/nlu|100.0%|✅|
|🟢|What does core and nlu mean?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|how to use formaction|technical_question|technical_question|100.0%|✅|
|🟢|want to build a chatbot|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|give me some information on nlu|faq/nlu|faq/nlu|100.0%|✅|
|🟢|what is rasax|faq/rasax|faq/rasax|100.0%|✅|
|🟢|I am looking for tutorial on Rasa NLU|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|okay sure|affirm|affirm|100.0%|✅|
|🟢|Can i talk to a human?|human_handoff|human_handoff|100.0%|✅|
|🟢|How do I download RASA|install_rasa|install_rasa|100.0%|✅|
|🟢|where can i find some tutorials?|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|Hello, rasa supports spanish?|faq/languages|faq/languages|100.0%|✅|
|🟢|How to build a bot in rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|python version|faq/python_version|faq/python_version|100.0%|✅|
|🟢|python version?|faq/python_version|faq/python_version|100.0%|✅|
|🟢|cr|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|Rasa X features|faq/rasax|faq/rasax|100.0%|✅|
|🟢|really|affirm|affirm|100.0%|✅|
|🟢|are there different packages customers can book?|contact_sales|contact_sales|100.0%|✅|
|🟢|I'm fine and you|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|i want to know about RASA Nlu|faq/nlu|faq/nlu|100.0%|✅|
|🟢|dialogflow and implementation from scratch|switch|switch|100.0%|✅|
|🟢|I have a few questions on my pay check|need_help_broad|need_help_broad|100.0%|✅|
|🟢|i need help setting up|install_rasa|install_rasa|100.0%|✅|
|🟢|How to get starter?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Hello, Sara. How can I configure etnity extraction for russian lnguage?|technical_question|technical_question|100.0%|✅|
|🟢|do you have a nlu tutorial i can follow|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|hello, my name is Charles Pfeffer|greet|greet|100.0%|✅|
|🟢|wit|switch|switch|100.0%|✅|
|🟢|Is rasa better than google dialogflow?|why_rasa|why_rasa|100.0%|✅|
|🟢|purchase rasa enterprise|contact_sales|contact_sales|100.0%|✅|
|🟢|nah|deny|deny|100.0%|✅|
|🟢|sorry not right now|deny|deny|100.0%|✅|
|🟢|can you tell me exactly how old you are?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|will this work on windows server|technical_question|technical_question|100.0%|✅|
|🟢|Hey is there a tutorial on how to train an intent cassification model in Python_|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|What name do I go by?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|I am super sad|react_negative|react_negative|100.0%|✅|
|🟢|what can you?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|what you can|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|book|contact_sales|contact_sales|100.0%|✅|
|🟢|custom ner|nlu_info|nlu_info|100.0%|✅|
|🟢|Not really|deny|deny|100.0%|✅|
|🟢|it would be helpful to learn more about entity recognition|nlu_info|nlu_info|100.0%|✅|
|🟢|When I use Rasa, Can I make bot speaking Japanese?|faq/languages|faq/languages|100.0%|✅|
|🟢|i am sad|react_negative|react_negative|100.0%|✅|
|🟢|how are the slots?|faq/slots|faq/slots|100.0%|✅|
|🟢|are you real human?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|how can I help improve your code|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|how can I help improve your code?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|DOES RASA SUPPORT THE WHATS APP?|faq/channels|faq/channels|100.0%|✅|
|🟢|how can I contribute?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|you are cool man|react_positive|react_positive|100.0%|✅|
|🟢|to make a subscribtion|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|ok great|affirm|affirm|100.0%|✅|
|🟢|bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|how to install rasa?|install_rasa|install_rasa|100.0%|✅|
|🟢|I am using dialogflow - how can I migrate|switch|switch|100.0%|✅|
|🟢|tell me about Rasa X please|faq/rasax|faq/rasax|100.0%|✅|
|🟢|rasa can use which different messaging channels?|faq/channels|faq/channels|100.0%|✅|
|🟢|thats fine|affirm|affirm|100.0%|✅|
|🟢|I have chosen Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|🟢|How can I add code to Rasa|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|why should I switch from luis|why_rasa|why_rasa|100.0%|✅|
|🟢|no thank s|deny|deny|100.0%|✅|
|🟢|not going well at all|deny|deny|100.0%|✅|
|🟢|how to build bot with rasa x|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|switching|switch|switch|100.0%|✅|
|🟢|what time do you have?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|i  am stuck with an erorr|need_help_broad|need_help_broad|100.0%|✅|
|🟢|Now I'm sad|react_negative|react_negative|100.0%|✅|
|🟢|whats rasax|faq/rasax|faq/rasax|100.0%|✅|
|🟢|yes subscribe me|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|more info about enterprise|faq/ee|faq/ee|100.0%|✅|
|🟢|I want to talk with sales about our project|contact_sales|contact_sales|100.0%|✅|
|🟢|what is your name|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|🟢|what is your name?|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|🟢|rasa hello|greet|greet|100.0%|✅|
|🟢|i don't have it|enter_data|enter_data|100.0%|✅|
|🟢|what is this rasa x thing. could you tell me more?|faq/rasax|faq/rasax|100.0%|✅|
|🟢|byee|bye|bye|100.0%|✅|
|🟢|LUIS|switch|switch|100.0%|✅|
|🟢|thx|thank|thank|100.0%|✅|
|🟢|How to install Rasa Core?|install_rasa|install_rasa|100.0%|✅|
|🟢|umm|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|let's make a subscribtion|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|good night|bye|bye|100.0%|✅|
|🟢|I still don’t get how intent classification works|nlu_info|nlu_info|100.0%|✅|
|🟢|are there some nlu tutorials i could look at|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|I want to know more about core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|love you|react_positive|react_positive|100.0%|✅|
|🟢|salut|greet|greet|100.0%|✅|
|🟢|hi can you help e build a chatbot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to install|install_rasa|install_rasa|100.0%|✅|
|🟢|can i migrate my luis bot to raza|switch|switch|100.0%|✅|
|🟢|how about building chatbot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|what is duckling|nlu_info|nlu_info|100.0%|✅|
|🟢|what is duckling?|nlu_info|nlu_info|100.0%|✅|
|🟢|my nlu cant detect entities|technical_question|technical_question|100.0%|✅|
|🟢|why should I use Rasa|why_rasa|why_rasa|100.0%|✅|
|🟢|but I want a sales call|contact_sales|contact_sales|100.0%|✅|
|🟢|Oh, ok|affirm|affirm|100.0%|✅|
|🟢|please can you book call for me|contact_sales|contact_sales|100.0%|✅|
|🟢|can you explain rasa x to me|faq/rasax|faq/rasax|100.0%|✅|
|🟢|How can I be a contributor?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|can you explain to me how entity recognition works?|nlu_info|nlu_info|100.0%|✅|
|🟢|No thank you|deny|deny|100.0%|✅|
|🟢|No, thank you|deny|deny|100.0%|✅|
|🟢|what are you, a bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|🟢|see u later|bye|bye|100.0%|✅|
|🟢|chatbot language ?|faq/languages|faq/languages|100.0%|✅|
|🟢|What's difference between these?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|t-mobile US|enter_data|enter_data|100.0%|✅|
|🟢|i would like to follow a nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|no go|deny|deny|100.0%|✅|
|🟢|What is the hour and minute right now?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|🟢|i need a tutorial on how to use rasa nlu|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|alright|affirm|affirm|100.0%|✅|
|🟢|NO DON"T WANT THIS!|deny|deny|100.0%|✅|
|🟢|that is funny|react_positive|react_positive|100.0%|✅|
|🟢|what is a intent?|nlu_info|nlu_info|100.0%|✅|
|🟢|rasa is not working|broken|broken|100.0%|✅|
|🟢|hm ok then i want to talk to the sales dude|contact_sales|contact_sales|100.0%|✅|
|🟢|no thank you|deny|deny|100.0%|✅|
|🟢|no, thank you|deny|deny|100.0%|✅|
|🟢|good moring|greet|greet|100.0%|✅|
|🟢|how to install rasa core?|install_rasa|install_rasa|100.0%|✅|
|🟢|why is rasa better?|why_rasa|why_rasa|100.0%|✅|
|🟢|Rasa playgrounds isn't working for me|broken|broken|100.0%|✅|
|🟢|is Rasa Playground separate from Rasa?|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|go|affirm|affirm|100.0%|✅|
|🟢|I guess so|affirm|affirm|100.0%|✅|
|🟢|let me speak with a real person please|human_handoff|human_handoff|100.0%|✅|
|🟢|please provide information on your enterprise package|faq/ee|faq/ee|100.0%|✅|
|🟢|farewell|bye|bye|100.0%|✅|
|🟢|k byyye #slay|bye|bye|100.0%|✅|
|🟢|which python do you support?|faq/python_version|faq/python_version|100.0%|✅|
|🟢|lets do this|affirm|affirm|100.0%|✅|
|🟢|Yes, I do need Rasa Stack.|install_rasa|install_rasa|100.0%|✅|
|🟢|great lets do that|affirm|affirm|100.0%|✅|
|🟢|give me a human|human_handoff|human_handoff|100.0%|✅|
|🟢|what's your name|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|🟢|it is cold|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|🟢|rasa enterprise|faq/ee|faq/ee|100.0%|✅|
|🟢|i am looking for a nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|you asked me a yes or no question, which i answered with yes|affirm|affirm|100.0%|✅|
|🟢|yesss|affirm|affirm|100.0%|✅|
|🟢|What is the name I was given?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|nehi|deny|deny|100.0%|✅|
|🟢|what is this nlu thing?|faq/nlu|faq/nlu|100.0%|✅|
|🟢|are you cool|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|intent classification - what is that?|nlu_info|nlu_info|100.0%|✅|
|🟢|tell me something about core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|i love you|react_positive|react_positive|100.0%|✅|
|🟢|hey let's talk|greet|greet|100.0%|✅|
|🟢|hey, let's talk|greet|greet|100.0%|✅|
|🟢|I am sad|react_negative|react_negative|100.0%|✅|
|🟢|i want to learn more about Rasa X|faq/rasax|faq/rasax|100.0%|✅|
|🟢|How can I try out Rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|lets get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|yep please|affirm|affirm|100.0%|✅|
|🟢|yesssss|affirm|affirm|100.0%|✅|
|🟢|nope. i am good|deny|deny|100.0%|✅|
|🟢|no i won't|deny|deny|100.0%|✅|
|🟢|how can I install RASA|install_rasa|install_rasa|100.0%|✅|
|🟢|I want to switch from dialogflow to rasa|switch|switch|100.0%|✅|
|🟢|french|enter_data|enter_data|100.0%|✅|
|🟢|nah, first time|deny|deny|100.0%|✅|
|🟢|What year were you born?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|what year were you born?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|i don't want either of those|deny|deny|100.0%|✅|
|🟢|Tell me about rasa x|faq/rasax|faq/rasax|100.0%|✅|
|🟢|Who ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|🟢|how does rasa x relate to rasa core|faq/rasax|faq/rasax|100.0%|✅|
|🟢|yes, I'd love to|affirm|affirm|100.0%|✅|
|🟢|how to use form actions|technical_question|technical_question|100.0%|✅|
|🟢|Can you built text bot with Japanese?|faq/languages|faq/languages|100.0%|✅|
|🟢|Help me to find the forum.|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|ya i want|affirm|affirm|100.0%|✅|
|🟢|hi. Sara what do you do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|rasa core is open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|what's rasa x|faq/rasax|faq/rasax|100.0%|✅|
|🟢|good bye|bye|bye|100.0%|✅|
|🟢|i want someone to call me|contact_sales|contact_sales|100.0%|✅|
|🟢|definitely not|deny|deny|100.0%|✅|
|🟢|i want to get started|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|is rasa available for node?|faq/languages|faq/languages|100.0%|✅|
|🟢|no i don't accept|deny|deny|100.0%|✅|
|🟢|explain about the rasa dialogue management|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|please give me instructions for pip|enter_data|enter_data|100.0%|✅|
|🟢|I am not able to restart action in some action|technical_question|technical_question|100.0%|✅|
|🟢|ayyyy whaddup|greet|greet|100.0%|✅|
|🟢|luis|switch|switch|100.0%|✅|
|🟢|how to export dialogflow data to rasa|switch|switch|100.0%|✅|
|🟢|How to migrate from Luis?|switch|switch|100.0%|✅|
|🟢|no bots at all|deny|deny|100.0%|✅|
|🟢|i need a rasa nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|in which rasa version google hangouts chat available|faq/channels|faq/channels|100.0%|✅|
|🟢|Thats so rude|react_negative|react_negative|100.0%|✅|
|🟢|rasa tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|ok.bye|bye|bye|100.0%|✅|
|🟢|i dont wanna talk to a bot|human_handoff|human_handoff|100.0%|✅|
|🟢|gotta go|bye|bye|100.0%|✅|
|🟢|i am angry over you|react_negative|react_negative|100.0%|✅|
|🟢|what should I do when I want to use a binary slot|technical_question|technical_question|100.0%|✅|
|🟢|goodbye|bye|bye|100.0%|✅|
|🟢|goodbye.|bye|bye|100.0%|✅|
|🟢|i am Karen Mease|greet|greet|100.0%|✅|
|🟢|why should I use rasa?|why_rasa|why_rasa|100.0%|✅|
|🟢|Can I help improve your code at all?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|boring|react_negative|react_negative|100.0%|✅|
|🟢|can you guide me know to create knowledge base chatbot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|id like to subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|i dont want to accept :P lol|deny|deny|100.0%|✅|
|🟢|Can I assist?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|i need a nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|HOW CAN i connect to rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how can I add new language to rasa core|faq/languages|faq/languages|100.0%|✅|
|🟢|Rasa Is?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|You are mad|react_negative|react_negative|100.0%|✅|
|🟢|i need to download rasa|install_rasa|install_rasa|100.0%|✅|
|🟢|How do I talk to a human|human_handoff|human_handoff|100.0%|✅|
|🟢|explain integrations|faq/channels|faq/channels|100.0%|✅|
|🟢|which user interface can I use?|faq/channels|faq/channels|100.0%|✅|
|🟢|You're cute.|react_positive|react_positive|100.0%|✅|
|🟢|Take me to the forum help section.|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|this is a really frustrating experience|react_negative|react_negative|100.0%|✅|
|🟢|There must be a way I can put forth my ideas to the situation.|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|You are rude|react_negative|react_negative|100.0%|✅|
|🟢|How to migrate to DialogFlow?|switch|switch|100.0%|✅|
|🟢|Can you tell me about rasa x?|faq/rasax|faq/rasax|100.0%|✅|
|🟢|bot framework|switch|switch|100.0%|✅|
|🟢|how do I access the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|Yeah please help me out|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|rasa core|enter_data|enter_data|100.0%|✅|
|🟢|I want an offer for your platform|contact_sales|contact_sales|100.0%|✅|
|🟢|get the latest news from Rasa|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|Rasa Stack is what I will be installing|install_rasa|install_rasa|100.0%|✅|
|🟢|can you tell me how to create a new rasa project|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|How do I find the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|ja cool|affirm|affirm|100.0%|✅|
|🟢|ofcoure i do|affirm|affirm|100.0%|✅|
|🟢|Do I have a name? What is it?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|ya thats cool|affirm|affirm|100.0%|✅|
|🟢|why not use watson?|why_rasa|why_rasa|100.0%|✅|
|🟢|Hi there|greet|greet|100.0%|✅|
|🟢|amazing, thanks|thank|thank|100.0%|✅|
|🟢|how can I leave a query in the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|How to install Rasa|install_rasa|install_rasa|100.0%|✅|
|🟢|How to install Rasa?|install_rasa|install_rasa|100.0%|✅|
|🟢|how can I improve Rasa|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|what's the best tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|please tell me more about rasa x|faq/rasax|faq/rasax|100.0%|✅|
|🟢|diffrence between rasa core and rasa nlu|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|🟢|migrate to rasa from another tool|switch|switch|100.0%|✅|
|🟢|let's start|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|i got error while installing rasa|need_help_broad|need_help_broad|100.0%|✅|
|🟢|I use luis|switch|switch|100.0%|✅|
|🟢|it won't train|broken|broken|100.0%|✅|
|🟢|Migration please|switch|switch|100.0%|✅|
|🟢|try rasa online|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|it would be helpful to learn more about intent classification|nlu_info|nlu_info|100.0%|✅|
|🟢|what are your features ?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|Channels|faq/channels|faq/channels|100.0%|✅|
|🟢|what sould i do to install rasa|install_rasa|install_rasa|100.0%|✅|
|🟢|funny bot|enter_data|enter_data|100.0%|✅|
|🟢|yes give me information|affirm|affirm|100.0%|✅|
|🟢|Yes, I have a question|need_help_broad|need_help_broad|100.0%|✅|
|🟢|what do I need to install Rasa|install_rasa|install_rasa|100.0%|✅|
|🟢|installation error|technical_question|technical_question|100.0%|✅|
|🟢|give me someone who can explain your business model|contact_sales|contact_sales|100.0%|✅|
|🟢|why is rasa good|why_rasa|why_rasa|100.0%|✅|
|🟢|What was I named?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|voice|faq/voice|faq/voice|100.0%|✅|
|🟢|yep if i have to|affirm|affirm|100.0%|✅|
|🟢|super sad|react_negative|react_negative|100.0%|✅|
|🟢|I want to ask the forum for an answer|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|hi i am not able install rasa demo in my machine|install_rasa|install_rasa|100.0%|✅|
|🟢|it's pretty cool|react_positive|react_positive|100.0%|✅|
|🟢|no you did it wrong|deny|deny|100.0%|✅|
|🟢|chatfuel|switch|switch|100.0%|✅|
|🟢|how do i train rasa nlu|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|absolutely not|deny|deny|100.0%|✅|
|🟢|how can I use transformers|technical_question|technical_question|100.0%|✅|
|🟢|I want to put some of my effort in.|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|i sad|react_negative|react_negative|100.0%|✅|
|🟢|sure|affirm|affirm|100.0%|✅|
|🟢|sure!|affirm|affirm|100.0%|✅|
|🟢|tlak to you later|bye|bye|100.0%|✅|
|🟢|ok fine|affirm|affirm|100.0%|✅|
|🟢|I want to get help in the forum|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|Where should I go for dinner?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|🟢|How to make a bot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|I want to use Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|🟢|I need a real person|human_handoff|human_handoff|100.0%|✅|
|🟢|what is the enterprise edition|faq/ee|faq/ee|100.0%|✅|
|🟢|SURE|affirm|affirm|100.0%|✅|
|🟢|how old are u|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|i can migrate microsoft luis bot to raza?|switch|switch|100.0%|✅|
|🟢|I have used it in the past|affirm|affirm|100.0%|✅|
|🟢|I will|affirm|affirm|100.0%|✅|
|🟢|sara, are you a robot or human?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|Yep that's fine|affirm|affirm|100.0%|✅|
|🟢|yes, I have a question|need_help_broad|need_help_broad|100.0%|✅|
|🟢|How do I identify myself?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|Hi the command rasa init doesn't do anything in windows|technical_question|technical_question|100.0%|✅|
|🟢|I want to change from dialogflow to rasa|switch|switch|100.0%|✅|
|🟢|how to install rasa_nlu|install_rasa|install_rasa|100.0%|✅|
|🟢|Installing Rasa Stack will be extremely helpful to me.|install_rasa|install_rasa|100.0%|✅|
|🟢|iam not feeling good|react_negative|react_negative|100.0%|✅|
|🟢|Thanks|thank|thank|100.0%|✅|
|🟢|Thanks!|thank|thank|100.0%|✅|
|🟢|why is rasa so good?|why_rasa|why_rasa|100.0%|✅|
|🟢|how to using you|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|i'm afraid not|deny|deny|100.0%|✅|
|🟢|what is rasa core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|what is rasa core?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|done|affirm|affirm|100.0%|✅|
|🟢|i am stuck with error|need_help_broad|need_help_broad|100.0%|✅|
|🟢|decline|deny|deny|100.0%|✅|
|🟢|it's not training|broken|broken|100.0%|✅|
|🟢|:D|react_positive|react_positive|100.0%|✅|
|🟢|how is rasa's NLU better than watson 's|why_rasa|why_rasa|100.0%|✅|
|🟢|ya please|affirm|affirm|100.0%|✅|
|🟢|Where do I post questions in the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|toodle-oo|bye|bye|100.0%|✅|
|🟢|what age are you|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|you are a badass bot!|react_positive|react_positive|100.0%|✅|
|🟢|Thanks for that|thank|thank|100.0%|✅|
|🟢|where to start?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|rasa nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|how to build assistant with rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|we started working with rasa but now we need support|contact_sales|contact_sales|100.0%|✅|
|🟢|Is there a way I can assist?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|thanks f|thank|thank|100.0%|✅|
|🟢|ook|affirm|affirm|100.0%|✅|
|🟢|can you explain rasa core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|great thanks|thank|thank|100.0%|✅|
|🟢|any open source GUI rasa have?|technical_question|technical_question|100.0%|✅|
|🟢|nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|thnks|thank|thank|100.0%|✅|
|🟢|no stop|deny|deny|100.0%|✅|
|🟢|testing|technical_question|technical_question|100.0%|✅|
|🟢|i am facing a particular error,could u help me?|need_help_broad|need_help_broad|100.0%|✅|
|🟢|how can i contribute to Rasa|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|your NLU understand spanish?|faq/languages|faq/languages|100.0%|✅|
|🟢|how does rasa dialogue management work?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|NLU data  generation|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|100.0%|✅|
|🟢|elaborate on rasa x|faq/rasax|faq/rasax|100.0%|✅|
|🟢|give me a human now|human_handoff|human_handoff|100.0%|✅|
|🟢|Do you have any tutorials how to migrate from dialogflow?|switch|switch|100.0%|✅|
|🟢|we built a bot with rasa x but now we're interested in the enterprise edition|faq/ee|faq/ee|100.0%|✅|
|🟢|i want to chat with human|human_handoff|human_handoff|100.0%|✅|
|🟢|What should I do fo this project?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|what about your day|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|What am I called?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|🟢|i don't think so|deny|deny|100.0%|✅|
|🟢|Accept|affirm|affirm|100.0%|✅|
|🟢|restart server|technical_question|technical_question|100.0%|✅|
|🟢|what's good|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|🟢|What is your origin?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|i want to speak to customer service|human_handoff|human_handoff|100.0%|✅|
|🟢|no and no again|deny|deny|100.0%|✅|
|🟢|Yep|affirm|affirm|100.0%|✅|
|🟢|Yep!|affirm|affirm|100.0%|✅|
|🟢|ciao|bye|bye|100.0%|✅|
|🟢|getting some errors|need_help_broad|need_help_broad|100.0%|✅|
|🟢|i want to extract predefined entity from user query|technical_question|technical_question|100.0%|✅|
|🟢|What's the name of the place you came from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|what is dialogue management|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|What is dialogue management ?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|Bye|bye|bye|100.0%|✅|
|🟢|alexa|faq/voice|faq/voice|100.0%|✅|
|🟢|php|technical_question|technical_question|100.0%|✅|
|🟢|Where from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|i'd like to talk to a sales person|contact_sales|contact_sales|100.0%|✅|
|🟢|yop|affirm|affirm|100.0%|✅|
|🟢|how to build a bot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|how to build a bot?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|I need to ask a question in the forum.|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|why should I migrate to rasa?|why_rasa|why_rasa|100.0%|✅|
|🟢|can you help me build my bot?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|hi what is your name?|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|🟢|what's rasa core?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|How can I be helpful?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|How can I help with the code?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|ok|affirm|affirm|100.0%|✅|
|🟢|ok...|affirm|affirm|100.0%|✅|
|🟢|ok..|affirm|affirm|100.0%|✅|
|🟢|I have a specific question regarding installation|install_rasa|install_rasa|100.0%|✅|
|🟢|Hey I want to ask a question in the forum|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|where can i get a tutorial on rasa|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|are you a real person|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|Are you a real person?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|are you a real person?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|🟢|What do you do as a company?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|Why should I contribute|ask_why_contribute|ask_why_contribute|100.0%|✅|
|🟢|Where can I find the forum|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|how does dialogue management work?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|badass bot tester|enter_data|enter_data|100.0%|✅|
|🟢|that ok|affirm|affirm|100.0%|✅|
|🟢|bye|bye|bye|100.0%|✅|
|🟢|bye .|bye|bye|100.0%|✅|
|🟢|bye!|bye|bye|100.0%|✅|
|🟢|recommend me some nlu tools|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|100.0%|✅|
|🟢|thanks for the help|thank|thank|100.0%|✅|
|🟢|how can i use you|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|install Rasa X|install_rasa|install_rasa|100.0%|✅|
|🟢|how do I use rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|crappy joke|react_negative|react_negative|100.0%|✅|
|🟢|what's so great about using Rasa?|why_rasa|why_rasa|100.0%|✅|
|🟢|what is the difference between slot and entity|technical_question|technical_question|100.0%|✅|
|🟢|Okay who am I?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|tutorials|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|ok thanks|thank|thank|100.0%|✅|
|🟢|ok thanks!|thank|thank|100.0%|✅|
|🟢|byr|bye|bye|100.0%|✅|
|🟢|i want to build bots|enter_data|enter_data|100.0%|✅|
|🟢|I want to ask a question in the forum|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|i need a rasa core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|🟢|Its urgent for me to install Rasa.|install_rasa|install_rasa|100.0%|✅|
|🟢|and why i should not use Tenserflow?|why_rasa|why_rasa|100.0%|✅|
|🟢|ok send me to the forum|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|you're rather dull|react_negative|react_negative|100.0%|✅|
|🟢|where to start the development of rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Bye bye|bye|bye|100.0%|✅|
|🟢|why would i use your product|why_rasa|why_rasa|100.0%|✅|
|🟢|OK|affirm|affirm|100.0%|✅|
|🟢|What area are you from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|I am stuck with fallback|need_help_broad|need_help_broad|100.0%|✅|
|🟢|i want to try it online|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|🟢|not really|deny|deny|100.0%|✅|
|🟢|tell me about dialogue management|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|where do i find instructions|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|okay cool|affirm|affirm|100.0%|✅|
|🟢|I love you|react_positive|react_positive|100.0%|✅|
|🟢|cheers bro|thank|thank|100.0%|✅|
|🟢|sadly|react_negative|react_negative|100.0%|✅|
|🟢|no, my frst time|deny|deny|100.0%|✅|
|🟢|install Rasa NLU|install_rasa|install_rasa|100.0%|✅|
|🟢|why not use ibm watson|why_rasa|why_rasa|100.0%|✅|
|🟢|You are quite bad|react_negative|react_negative|100.0%|✅|
|🟢|what rasa_nlu|faq/nlu|faq/nlu|100.0%|✅|
|🟢|How can one contribute?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|i want to use pip to install sara|install_rasa|install_rasa|100.0%|✅|
|🟢|Hi rasa|greet|greet|100.0%|✅|
|🟢|please explain what is dialogue management|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|i will!|affirm|affirm|100.0%|✅|
|🟢|give me a reason to switch to Rasa from luis|why_rasa|why_rasa|100.0%|✅|
|🟢|can I use Rasa with my Raspberry Pi|technical_question|technical_question|100.0%|✅|
|🟢|i want human :(|human_handoff|human_handoff|100.0%|✅|
|🟢|can you show me a nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|tell me about core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|you know French|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|🟢|how come?|explain|explain|100.0%|✅|
|🟢|considering|affirm|affirm|100.0%|✅|
|🟢|what's rasa nlu|faq/nlu|faq/nlu|100.0%|✅|
|🟢|thanks for forum link, I'll check it out|thank|thank|100.0%|✅|
|🟢|oh cool|affirm|affirm|100.0%|✅|
|🟢|from which tools can I migrate to rasa?|switch|switch|100.0%|✅|
|🟢|what is nlu|faq/nlu|faq/nlu|100.0%|✅|
|🟢|In what ways can I help?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|can you help me to build a bot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|need more data for nlu|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|100.0%|✅|
|🟢|Nevermind|deny|deny|100.0%|✅|
|🟢|tell me about Rasa Core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|4 + 2 = ?|out_of_scope/other|enter_data|100.0%|❌|
|🟢|what is the difference between you and LUIS|technical_question|technical_question|100.0%|✅|
|🟢|my bot can be in italian?|faq/languages|faq/languages|100.0%|✅|
|🟢|i am stuck|need_help_broad|need_help_broad|100.0%|✅|
|🟢|What is the benefit of contributing to your code|ask_why_contribute|ask_why_contribute|100.0%|✅|
|🟢|how much is it|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|lots of errors|need_help_broad|need_help_broad|100.0%|✅|
|🟢|I want to build a chatbot|how_to_get_started|faq/rasa_components|100.0%|❌|
|🟢|what is you name and where are you from|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|🟢|thank u|thank|thank|100.0%|✅|
|🟢|take care|bye|bye|100.0%|✅|
|🟢|How can I develop a bot?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|thanks|thank|thank|100.0%|✅|
|🟢|thanks!|thank|thank|100.0%|✅|
|🟢|I am stuck and I need help|need_help_broad|need_help_broad|100.0%|✅|
|🟢|Where is the forum|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|i have to less nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|100.0%|✅|
|🟢|I do not know yet|enter_data|enter_data|100.0%|✅|
|🟢|what is it for?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|Great, thanks|thank|thank|100.0%|✅|
|🟢|what components of Rasa are open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|🟢|I have an inquiry for the forum|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|i want to learn about rasa core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|rasa core agent information|technical_question|technical_question|100.0%|✅|
|🟢|Ok|affirm|affirm|100.0%|✅|
|🟢|Ok.|affirm|affirm|100.0%|✅|
|🟢|join that newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|🟢|an ice cream bot|enter_data|enter_data|100.0%|✅|
|🟢|ok i guess you can't help me|canthelp|canthelp|100.0%|✅|
|🟢|help me build a bot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|im stuck|need_help_broad|need_help_broad|100.0%|✅|
|🟢|I need to ask something of the forum|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|Thank's!|thank|thank|100.0%|✅|
|🟢|i would like rasa enterprise|contact_sales|contact_sales|100.0%|✅|
|🟢|nah not for me|deny|deny|100.0%|✅|
|🟢|i guess you can't help me then|canthelp|canthelp|100.0%|✅|
|🟢|thank you anyways|thank|thank|100.0%|✅|
|🟢|it's broken|broken|broken|100.0%|✅|
|🟢|Where can I post on the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|actions on rasa|technical_question|technical_question|100.0%|✅|
|🟢|how to improve Rasa|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|it is showing error while installing|need_help_broad|need_help_broad|100.0%|✅|
|🟢|do you support french ?|faq/languages|faq/languages|100.0%|✅|
|🟢|How can one contribute to this cause?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|help me wih the installation|install_rasa|install_rasa|100.0%|✅|
|🟢|I get errors while installation|need_help_broad|need_help_broad|100.0%|✅|
|🟢|i require more nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|100.0%|✅|
|🟢|i dont want to|deny|deny|100.0%|✅|
|🟢|I want to know if rasa works with duckling|nlu_info|nlu_info|100.0%|✅|
|🟢|I want know about Rasa Core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|do you know how to set up a chatbot?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|I want to make a forum post.|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|whats rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|give me more details|explain|explain|100.0%|✅|
|🟢|I am searching the changlog|technical_question|technical_question|100.0%|✅|
|🟢|what's the rasa x enterprise edition|faq/ee|faq/ee|100.0%|✅|
|🟢|cya|bye|bye|100.0%|✅|
|🟢|i have errors in installaition|need_help_broad|need_help_broad|100.0%|✅|
|🟢|yes, give me information, please|affirm|affirm|100.0%|✅|
|🟢|give me a reason to use Rasa|why_rasa|why_rasa|100.0%|✅|
|🟢|I want to create chatbot using Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|amazing!|affirm|affirm|100.0%|✅|
|🟢|what is ur name|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|🟢|I dont want to tell|deny|deny|100.0%|✅|
|🟢|could I program spanish speaking bots?|faq/languages|faq/languages|100.0%|✅|
|🟢|danke|thank|thank|100.0%|✅|
|🟢|I have a few questions|need_help_broad|need_help_broad|100.0%|✅|
|🟢|bye bye|bye|bye|100.0%|✅|
|🟢|I want information about the enterprise edition|faq/ee|faq/ee|100.0%|✅|
|🟢|please show me a nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|what can I do with Rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|what can i do with rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|🟢|see you . bye|bye|bye|100.0%|✅|
|🟢|How d I use a boolean slot|technical_question|technical_question|100.0%|✅|
|🟢|thanks a lot|thank|thank|100.0%|✅|
|🟢|do you have tutorials about nlu|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|🟢|catch you later|bye|bye|100.0%|✅|
|🟢|Lets go to the forum so I can ask my question.|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|how do you switch from dialogflow|switch|switch|100.0%|✅|
|🟢|Do you have a user group|ask_which_events|ask_which_events|100.0%|✅|
|🟢|tell me about core please|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|what's my identity?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|🟢|k|affirm|affirm|100.0%|✅|
|🟢|Nice|affirm|affirm|100.0%|✅|
|🟢|you make me sad|react_negative|react_negative|100.0%|✅|
|🟢|i want to know more about nlu and why is it better than watson or luis|why_rasa|why_rasa|100.0%|✅|
|🟢|good.|affirm|affirm|100.0%|✅|
|🟢|Where should I ask my question on the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|enterprise features|faq/ee|faq/ee|100.0%|✅|
|🟢|Surely you're not so smart lik i thought|react_negative|react_negative|100.0%|✅|
|🟢|yes what if i have to code open end responses into some categories|technical_question|technical_question|100.0%|✅|
|🟢|sad|react_negative|react_negative|100.0%|✅|
|🟢|i need more nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|100.0%|✅|
|🟢|ok then you cant help me|canthelp|canthelp|100.0%|✅|
|🟢|ok thanks sara|thank|thank|100.0%|✅|
|🟢|can you tell me how to build a bot?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|Playground is broken|broken|broken|100.0%|✅|
|🟢|what's pip|technical_question|technical_question|100.0%|✅|
|🟢|source code|source_code|source_code|100.0%|✅|
|🟢|can you help with some documentation|technical_question|technical_question|100.0%|✅|
|🟢|it is going pretty badly|deny|deny|100.0%|✅|
|🟢|how old?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|Where to get Rasa Stack?|install_rasa|install_rasa|100.0%|✅|
|🟢|why migrate?|why_rasa|why_rasa|100.0%|✅|
|🟢|its an german bot|enter_data|enter_data|100.0%|✅|
|🟢|Can you get me Rasa Core?|install_rasa|install_rasa|100.0%|✅|
|🟢|cool story bro|affirm|affirm|100.0%|✅|
|🟢|ok Bye|bye|bye|100.0%|✅|
|🟢|cheers|thank|thank|100.0%|✅|
|🟢|what is X ?|faq/rasax|faq/rasax|100.0%|✅|
|🟢|ok bye|bye|bye|100.0%|✅|
|🟢|ok, bye|bye|bye|100.0%|✅|
|🟢|Sure|affirm|affirm|100.0%|✅|
|🟢|bye was nice talking to you|bye|bye|100.0%|✅|
|🟢|is there a tutorial?|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|I need someone in the forum to help me|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|how can I get help in the forum|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|the bot won't train|broken|broken|100.0%|✅|
|🟢|I was looking for Duckling integration|nlu_info|nlu_info|100.0%|✅|
|🟢|what is this bot for|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|you are bad bot|react_negative|react_negative|100.0%|✅|
|🟢|thanks a bunch for everything|thank|thank|100.0%|✅|
|🟢|rasa core quickstart|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|in what ways can I help out?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|that sounds fine|affirm|affirm|100.0%|✅|
|🟢|What is your root?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|🟢|ok, but that doesnt help me|canthelp|canthelp|100.0%|✅|
|🟢|I am seeing an error|need_help_broad|need_help_broad|100.0%|✅|
|🟢|language = german|enter_data|enter_data|100.0%|✅|
|🟢|language: german|enter_data|enter_data|100.0%|✅|
|🟢|I don't want to say|deny|deny|100.0%|✅|
|🟢|For some reason, Rasa X never loads and I don't know why|broken|broken|100.0%|✅|
|🟢|i am looking for a core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|🟢|a bot|enter_data|enter_data|100.0%|✅|
|🟢|Is the forum the right place to ask questions?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|am struck with installation of rasa nlu and core in my mac book|install_rasa|install_rasa|100.0%|✅|
|🟢|i don't care!!!!|react_negative|react_negative|100.0%|✅|
|🟢|help me can you fix it|broken|broken|100.0%|✅|
|🟢|absolutely|affirm|affirm|100.0%|✅|
|🟢|i need smalltalk.md file|source_code|source_code|100.0%|✅|
|🟢|i would like to follow a core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|🟢|thank you|thank|thank|100.0%|✅|
|🟢|tell me the difference between rasa and x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|🟢|rasa core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|🟢|can you help me build a chatbot|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|What can I bring to help your code|ask_why_contribute|ask_why_contribute|100.0%|✅|
|🟢|see ya|bye|bye|100.0%|✅|
|🟢|what can i build with rasa core?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|how to build assistant?|how_to_get_started|how_to_get_started|100.0%|✅|
|🟢|hello I have a question|need_help_broad|need_help_broad|100.0%|✅|
|🟢|I need to ask the forum something|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|can you hand a conversation over to a human?|human_handoff|human_handoff|100.0%|✅|
|🟢|How do I use ngrok with rasa x?|technical_question|technical_question|100.0%|✅|
|🟢|can you help me with the rasa core ?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|🟢|driver|enter_data|enter_data|100.0%|✅|
|🟢|what ui can I use|faq/channels|faq/channels|100.0%|✅|
|🟢|How do I create a thread on the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|do you have a rasa tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|🟢|what is your birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|🟢|very very sad|react_negative|react_negative|100.0%|✅|
|🟢|i am sad about that|react_negative|react_negative|100.0%|✅|
|🟢|what are the benefits of helping|ask_why_contribute|ask_why_contribute|100.0%|✅|
|🟢|parts of rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|🟢|what technologies did u use to create more mature chatbot?|technical_question|technical_question|100.0%|✅|
|🟢|what are you doing|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|🟢|i need information from posters in the forum|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|cool thanks|thank|thank|100.0%|✅|
|🟢|cool, thanks|thank|thank|100.0%|✅|
|🟢|Looks nice|react_positive|react_positive|100.0%|✅|
|🟢|How can be of assistance?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|🟢|I need to know about Rasa X|faq/rasax|faq/rasax|100.0%|✅|
|🟢|Is it possible to integrate Rasa with Android to run on mobile devices|technical_question|technical_question|100.0%|✅|
|🟢|I have a question about the functioning of the device|need_help_broad|need_help_broad|100.0%|✅|
|🟢|please explain|explain|explain|100.0%|✅|
|🟢|i wanna build all the bots|enter_data|enter_data|100.0%|✅|
|🟢|how to integrate RASA with customer data?|technical_question|technical_question|100.0%|✅|
|🟢|thats not helping, can i talk to human?|human_handoff|human_handoff|100.0%|✅|
|🟢|still dont want to tell|deny|deny|100.0%|✅|
|🟢|happy|react_positive|react_positive|100.0%|✅|
|🟢|what are you made of|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|🟢|i need a tutorial on how to use rasa core|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|🟢|how can I get nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|100.0%|✅|
|🟢|docker is restarting|technical_question|technical_question|100.0%|✅|
|🟢|How do I ask a question on the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|🟢|thankyou|thank|thank|100.0%|✅|
|🟢|I don't wanna talk to a bot|human_handoff|human_handoff|100.0%|✅|
|🟢|are there also humans working for your company?|human_handoff|human_handoff|100.0%|✅|
|🟢|testing chatbot|technical_question|technical_question|100.0%|✅|
|🟢|i need a core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|99.9%|✅|
|🟢|yes thanks|thank|thank|99.9%|✅|
|🟢|so sad|react_negative|react_negative|99.9%|✅|
|🟢|so sad :(|react_negative|react_negative|99.9%|✅|
|🟢|I want to help the cause.|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|where can i get data for the nlu|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.9%|✅|
|🟢|i don't want to|deny|deny|99.9%|✅|
|🟢|can someone help me with infos about the enterprise edition|faq/ee|faq/ee|99.9%|✅|
|🟢|how do I contribute?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|how do i train rasa core|how_to_get_started|how_to_get_started|99.9%|✅|
|🟢|is rasa core paid?|faq/opensource_cost|faq/opensource_cost|99.9%|✅|
|🟢|what are the channels Rasa NLU supports|faq/channels|faq/channels|99.9%|✅|
|🟢|Why do I want to help with your code|ask_why_contribute|ask_why_contribute|99.9%|✅|
|🟢|Why should I contribute to your code?|ask_why_contribute|ask_why_contribute|99.9%|✅|
|🟢|very much|affirm|affirm|99.9%|✅|
|🟢|how have you been|chitchat/ask_howdoing|chitchat/ask_howdoing|99.9%|✅|
|🟢|are there tools to create nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.9%|✅|
|🟢|bad boy|react_negative|react_negative|99.9%|✅|
|🟢|i don't want to run rasa, i want to restart it|technical_question|technical_question|99.9%|✅|
|🟢|buy rasa enterprise|contact_sales|contact_sales|99.9%|✅|
|🟢|can you point me to a good manual about Rasa|faq/tutorials|faq/tutorials|99.9%|✅|
|🟢|what's the purpose of Rasa X|faq/rasax|faq/rasax|99.9%|✅|
|🟢|why switch from dialogflow?|why_rasa|why_rasa|99.9%|✅|
|🟢|I have a question|need_help_broad|need_help_broad|99.9%|✅|
|🟢|I have a question.|need_help_broad|need_help_broad|99.9%|✅|
|🟢|I have a question?|need_help_broad|need_help_broad|99.9%|✅|
|🟢|Yes I want to switch from LUIS to rasa|switch|switch|99.9%|✅|
|🟢|Where can I ask a question on the forum?|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|🟢|How do I post my question on the forum?|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|🟢|what is a custom action?|technical_question|technical_question|99.9%|✅|
|🟢|I am stuck with action|need_help_broad|need_help_broad|99.9%|✅|
|🟢|you cannot help me with what I want|canthelp|canthelp|99.9%|✅|
|🟢|i want to talk to someone else|human_handoff|human_handoff|99.9%|✅|
|🟢|stop it, i do not care!!!|deny|deny|99.9%|✅|
|🟢|i m stuck while importing data|need_help_broad|need_help_broad|99.9%|✅|
|🟢|what dialects does rasa support|faq/languages|faq/languages|99.9%|✅|
|🟢|I need to install Rasa NLU.|install_rasa|install_rasa|99.9%|✅|
|🟢|how can I help?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|why should I switch to rasa from dialogflow|why_rasa|why_rasa|99.9%|✅|
|🟢|Help me install rasa x|install_rasa|install_rasa|99.9%|✅|
|🟢|sounds good!|affirm|affirm|99.9%|✅|
|🟢|You're nice.|react_positive|react_positive|99.9%|✅|
|🟢|demo bot source code|source_code|source_code|99.9%|✅|
|🟢|Good|affirm|affirm|99.9%|✅|
|🟢|i got some error during installation|need_help_broad|need_help_broad|99.9%|✅|
|🟢|i need more info for rasa core|faq/dialogue_management|faq/dialogue_management|99.9%|✅|
|🟢|can i speak to your human|human_handoff|human_handoff|99.9%|✅|
|🟢|can you forward me to your team|human_handoff|human_handoff|99.9%|✅|
|🟢|bye udo|bye|bye|99.9%|✅|
|🟢|how to setup rasax on slack|faq/channels|faq/channels|99.9%|✅|
|🟢|how to you exit the server|technical_question|technical_question|99.9%|✅|
|🟢|where to train intents in rasa?|nlu_info|nlu_info|99.9%|✅|
|🟢|I'd like to install Rasa NLU|install_rasa|install_rasa|99.9%|✅|
|🟢|how do you build a bot|how_to_get_started|how_to_get_started|99.9%|✅|
|🟢|what will i get for the contribution?|ask_why_contribute|ask_why_contribute|99.9%|✅|
|🟢|thanks you|thank|thank|99.9%|✅|
|🟢|can i install on may mac|technical_question|technical_question|99.9%|✅|
|🟢|you are bot or human?|chitchat/ask_ishuman|chitchat/ask_ishuman|99.9%|✅|
|🟢|you are human or bot|chitchat/ask_ishuman|chitchat/ask_ishuman|99.9%|✅|
|🟢|how can i contribute to it|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|Why should I contribute to Rasa|ask_why_contribute|ask_why_contribute|99.9%|✅|
|🟢|i don not like this|deny|deny|99.9%|✅|
|🟢|i want to switch from luis to rasa|switch|switch|99.9%|✅|
|🟢|I think it's broken|broken|broken|99.9%|✅|
|🟢|ARE YOU SPANISH|chitchat/ask_languagesbot|chitchat/ask_languagesbot|99.9%|✅|
|🟢|can you put me in touch with a human?|human_handoff|human_handoff|99.9%|✅|
|🟢|core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|99.9%|✅|
|🟢|hi there it's me|greet|greet|99.9%|✅|
|🟢|which python?|faq/python_version|faq/python_version|99.9%|✅|
|🟢|Okay cool|affirm|affirm|99.9%|✅|
|🟢|that was shit, you're not helping|canthelp|canthelp|99.9%|✅|
|🟢|see you|bye|bye|99.9%|✅|
|🟢|goodnight|bye|bye|99.9%|✅|
|🟢|hm, i'd like that|affirm|affirm|99.9%|✅|
|🟢|are there ways I can contribute?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|Thanks bot|thank|thank|99.9%|✅|
|🟢|I dont like to talk to a machine|human_handoff|human_handoff|99.9%|✅|
|🟢|how ?|chitchat/ask_howdoing|chitchat/ask_howdoing|99.9%|✅|
|🟢|how|out_of_scope/other|chitchat/ask_howdoing|99.9%|❌|
|🟢|today was a nice day|react_positive|react_positive|99.9%|✅|
|🟢|why is that necessary|explain|explain|99.9%|✅|
|🟢|i want that|affirm|affirm|99.9%|✅|
|🟢|ok good|affirm|affirm|99.9%|✅|
|🟢|service agent|human_handoff|human_handoff|99.9%|✅|
|🟢|how to install rasa in my system|install_rasa|install_rasa|99.9%|✅|
|🟢|what is EE?|faq/ee|faq/ee|99.9%|✅|
|🟢|are you real person or chat bot?|chitchat/ask_ishuman|chitchat/ask_ishuman|99.9%|✅|
|🟢|help me please it's not working|broken|broken|99.9%|✅|
|🟢|can i switch from luis to rasa?|switch|switch|99.9%|✅|
|🟢|pipeline recommendation|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|🟢|hi sara, i get the following error when trying to install rasa on my macbook|need_help_broad|need_help_broad|99.9%|✅|
|🟢|i'm not sure|deny|deny|99.9%|✅|
|🟢|Do you have a great day?|chitchat/ask_howdoing|chitchat/ask_howdoing|99.9%|✅|
|🟢|rasa is awesome|react_positive|react_positive|99.9%|✅|
|🟢|Is there some way I can help?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|How do I post on the forum?|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|🟢|how to build a pipelin|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|🟢|let me have the call|contact_sales|contact_sales|99.9%|✅|
|🟢|are there some core tutorials i could look at|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|99.9%|✅|
|🟢|I'm not giving you my email address|deny|deny|99.9%|✅|
|🟢|ok sara|affirm|affirm|99.9%|✅|
|🟢|I want to help improve Rasa|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|Where are you?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|99.9%|✅|
|🟢|Can you tell me what I am called?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|99.9%|✅|
|🟢|Did you have an tutorial.|faq/tutorials|faq/tutorials|99.9%|✅|
|🟢|thanks for your information|thank|thank|99.9%|✅|
|🟢|what is different|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|99.9%|✅|
|🟢|greet|greet|greet|99.9%|✅|
|🟢|TUTORIAL !!!!!!!!!!|faq/tutorials|faq/tutorials|99.9%|✅|
|🟢|tutorial|faq/tutorials|faq/tutorials|99.9%|✅|
|🟢|tutorial?|faq/tutorials|faq/tutorials|99.9%|✅|
|🟢|migrate to rasa|switch|switch|99.9%|✅|
|🟢|Thank you|thank|thank|99.9%|✅|
|🟢|Hi man|greet|greet|99.9%|✅|
|🟢|i am happy|react_positive|react_positive|99.9%|✅|
|🟢|what I a good pipeline to start with?|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|🟢|what is knowledge base|technical_question|technical_question|99.9%|✅|
|🟢|how do I install it?|install_rasa|install_rasa|99.9%|✅|
|🟢|I think you cant help me|canthelp|canthelp|99.9%|✅|
|🟢|How to I post a question on the forum?|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|🟢|how can I post a question in the forum?|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|🟢|that does not help|canthelp|canthelp|99.9%|✅|
|🟢|bye bye bot|bye|bye|99.9%|✅|
|🟢|who are u|chitchat/ask_whoisit|chitchat/ask_whoisit|99.9%|✅|
|🟢|what does rasa dialogue management do?|faq/dialogue_management|faq/dialogue_management|99.9%|✅|
|🟢|sure thing|affirm|affirm|99.9%|✅|
|🟢|i want to develop a chatbot|how_to_get_started|how_to_get_started|99.9%|✅|
|🟢|perfect thank you|thank|thank|99.9%|✅|
|🟢|go for it|affirm|affirm|99.9%|✅|
|🟢|What can I do to help?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|Rasa X isn't working for me|broken|broken|99.9%|✅|
|🟢|in what year were you born?|chitchat/ask_howold|chitchat/ask_howold|99.9%|✅|
|🟢|i want a tutorial on rasa core|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|99.9%|✅|
|🟢|What should I work on?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|what pipeline should I start with?|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|🟢|going super well|affirm|affirm|99.9%|✅|
|🟢|Is there some way I can help improve your code?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|Sure. I have a question for you|need_help_broad|need_help_broad|99.9%|✅|
|🟢|About Core|faq/dialogue_management|faq/dialogue_management|99.9%|✅|
|🟢|so, how do I use rasa?|how_to_get_started|how_to_get_started|99.9%|✅|
|🟢|can you explain to me how intent classification works?|nlu_info|nlu_info|99.9%|✅|
|🟢|How does one go about making their contribution?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|Why should I add to your code|ask_why_contribute|ask_why_contribute|99.9%|✅|
|🟢|why offer my assistance?|ask_why_contribute|ask_why_contribute|99.9%|✅|
|🟢|how do I run rasa on windows|install_rasa|install_rasa|99.9%|✅|
|🟢|I am getting some error|technical_question|technical_question|99.9%|✅|
|🟢|who r u|chitchat/ask_whoisit|chitchat/ask_whoisit|99.9%|✅|
|🟢|How do I get yes / no answer buttons|technical_question|technical_question|99.9%|✅|
|🟢|which tools can I use to create nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.9%|✅|
|🟢|I have a name, what is it?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|99.9%|✅|
|🟢|I got stuck with the installation|need_help_broad|need_help_broad|99.9%|✅|
|🟢|are there some tutorials i could look at|faq/tutorials|faq/tutorials|99.9%|✅|
|🟢|what pipeline should i use?|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|🟢|Tell me how I can contribute|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|what is core|faq/dialogue_management|faq/dialogue_management|99.9%|✅|
|🟢|That tool here isnt good|react_negative|react_negative|99.9%|✅|
|🟢|can i try it out|how_to_get_started|how_to_get_started|99.9%|✅|
|🟢|WHAT IS IT|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|99.9%|✅|
|🟢|pipeline|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|🟢|ok restart please|restart|restart|99.9%|✅|
|🟢|Rasa bot|enter_data|enter_data|99.9%|✅|
|🟢|can someone show me the forum?|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|🟢|recommend pipeline|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|🟢|can you help me with installation|install_rasa|install_rasa|99.9%|✅|
|🟢|i will leave|react_negative|react_negative|99.9%|✅|
|🟢|Can i use rasa without rasa x?|faq/differencerasarasax|faq/differencerasarasax|99.9%|✅|
|🟢|Why should I devote time to your code|ask_why_contribute|ask_why_contribute|99.9%|✅|
|🟢|ok, I understood|affirm|affirm|99.9%|✅|
|🟢|explain it to me|explain|explain|99.9%|✅|
|🟢|oh awesome!|affirm|affirm|99.9%|✅|
|🟢|I'm not going to give it to you|deny|deny|99.9%|✅|
|🟢|what is you name|chitchat/ask_whoisit|chitchat/ask_whoisit|99.9%|✅|
|🟢|bye :P|bye|bye|99.9%|✅|
|🟢|where is your source code|source_code|source_code|99.9%|✅|
|🟢|What could I do to be helpful?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|Why help Rasa's organization?|ask_why_contribute|ask_why_contribute|99.9%|✅|
|🟢|luis bot can migrate to raza bot ?|switch|switch|99.9%|✅|
|🟢|what is the right pipeline to choose?|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|🟢|stop this conversation|canthelp|canthelp|99.9%|✅|
|🟢|you are cool|react_positive|react_positive|99.9%|✅|
|🟢|That's awesome.|react_positive|react_positive|99.9%|✅|
|🟢|i get error when initializing a project|need_help_broad|need_help_broad|99.9%|✅|
|🟢|I need to get information from the forum|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|🟢|I mean to say that I liked the explanation|react_positive|react_positive|99.9%|✅|
|🟢|any other tools to create chatbots?|technical_question|technical_question|99.9%|✅|
|🟢|it is ok|affirm|affirm|99.9%|✅|
|🟢|Can you get a human to assist me?|human_handoff|human_handoff|99.9%|✅|
|🟢|How can I help you?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|ok, Sara|affirm|affirm|99.9%|✅|
|🟢|switch to rasa|switch|switch|99.9%|✅|
|🟢|then bye|bye|bye|99.9%|✅|
|🟢|how this Rasa works|how_to_get_started|how_to_get_started|99.9%|✅|
|🟢|I'm ready to contribute.|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|Can we stop at the forum so I can ask a question|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|🟢|Please, I need Rasa Core.|install_rasa|install_rasa|99.9%|✅|
|🟢|does rasa support python|faq/is_programming_required|faq/is_programming_required|99.9%|✅|
|🟢|I would like to contribute.|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|you good|react_positive|react_positive|99.9%|✅|
|🟢|can you explain me what intents are ?|nlu_info|nlu_info|99.9%|✅|
|🟢|Which other tools can be used to create chatbots?|technical_question|technical_question|99.9%|✅|
|🟢|Super! I love Rasa|react_positive|react_positive|99.9%|✅|
|🟢|ya cool|affirm|affirm|99.9%|✅|
|🟢|bots are bad|react_negative|react_negative|99.9%|✅|
|🟢|id like to talk to someone who can explain me what i can do with rasa|contact_sales|contact_sales|99.9%|✅|
|🟢|How to install rasa X?|install_rasa|install_rasa|99.9%|✅|
|🟢|how can I install rasa open source?|install_rasa|install_rasa|99.9%|✅|
|🟢|Where do I post my question?|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|🟢|how to build a pipeline for the bot|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|🟢|I am feeling bad|react_negative|react_negative|99.9%|✅|
|🟢|i need nlu.md file|source_code|source_code|99.9%|✅|
|🟢|you are bad|react_negative|react_negative|99.9%|✅|
|🟢|what you do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|99.9%|✅|
|🟢|I want to convert my dialog flow bot to rasa|switch|switch|99.9%|✅|
|🟢|there is an issue during installation|need_help_broad|need_help_broad|99.9%|✅|
|🟢|should I better start with the tensorflow pipeline or spacy?|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|🟢|That would be great|affirm|affirm|99.9%|✅|
|🟢|no I haven't decided yet if I want to sign up|deny|deny|99.9%|✅|
|🟢|Hello Rasa|greet|greet|99.9%|✅|
|🟢|How to download?|how_to_get_started|how_to_get_started|99.9%|✅|
|🟢|How do i write a forum question?|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|🟢|nlu pipeline|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|🟢|How to download rasa|install_rasa|install_rasa|99.9%|✅|
|🟢|i want a tutorial on core|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|99.9%|✅|
|🟢|I have error during the installation|need_help_broad|need_help_broad|99.9%|✅|
|🟢|Rasa X|enter_data|enter_data|99.9%|✅|
|🟢|are you real|chitchat/ask_isbot|chitchat/ask_isbot|99.9%|✅|
|🟢|can you help me with the pipeline?|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|🟢|please show me a core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|99.9%|✅|
|🟢|I want to offer assistance|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|u broke my heart|react_negative|react_negative|99.9%|✅|
|🟢|Help me get Rasa Core.|install_rasa|install_rasa|99.9%|✅|
|🟢|nothing else?|canthelp|canthelp|99.9%|✅|
|🟢|error message when installing rasa|need_help_broad|need_help_broad|99.9%|✅|
|🟢|How can I contribute to your code|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|like u|react_positive|react_positive|99.9%|✅|
|🟢|This is bad|react_negative|react_negative|99.9%|✅|
|🟢|Thank you so much|thank|thank|99.9%|✅|
|🟢|rasa is bad|react_negative|react_negative|99.9%|✅|
|🟢|How to generate NLU using frontend.|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.9%|✅|
|🟢|Close this talk|bye|bye|99.9%|✅|
|🟢|bye bot|bye|bye|99.9%|✅|
|🟢|In what manner can one contribute?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|Can I speak to anyone who can really help me?|human_handoff|human_handoff|99.9%|✅|
|🟢|I don't want to|deny|deny|99.9%|✅|
|🟢|I wonder if the forum can answer my question.|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|🟢|i am so worry|react_negative|react_negative|99.9%|✅|
|🟢|Although I understand your still in development, I feel a little bit disappointed.|react_negative|react_negative|99.9%|✅|
|🟢|you cant help me|canthelp|canthelp|99.9%|✅|
|🟢|i dont like bots|react_negative|react_negative|99.9%|✅|
|🟢|yes that's what i want|affirm|affirm|99.9%|✅|
|🟢|thats good|affirm|affirm|99.9%|✅|
|🟢|rasa init error|need_help_broad|need_help_broad|99.9%|✅|
|🟢|need to understand dialogue management|faq/dialogue_management|faq/dialogue_management|99.9%|✅|
|🟢|How is Rasa X different from Rasa?|faq/differencerasarasax|faq/differencerasarasax|99.9%|✅|
|🟢|ok, I behave now|affirm|affirm|99.9%|✅|
|🟢|Is there any way I can contribute?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|🟢|i want a recommendation for an nlu data generation tool|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.8%|✅|
|🟢|what are you good at?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|99.8%|✅|
|🟢|I don't wanna tell the name of my company|deny|deny|99.8%|✅|
|🟢|do u give me the code|source_code|source_code|99.8%|✅|
|🟢|I have a question about Rasa NLU|need_help_broad|need_help_broad|99.8%|✅|
|🟢|to the forum|ask_question_in_forum|ask_question_in_forum|99.8%|✅|
|🟢|when were you born?|chitchat/ask_howold|chitchat/ask_howold|99.8%|✅|
|🟢|I have a question for you|need_help_broad|need_help_broad|99.8%|✅|
|🟢|what do I get if I contribute|ask_why_contribute|ask_why_contribute|99.8%|✅|
|🟢|I don’t know which pipeline to use|pipeline_recommendation|pipeline_recommendation|99.8%|✅|
|🟢|where is the source code?|source_code|source_code|99.8%|✅|
|🟢|I'm ready to help.|ask_how_contribute|ask_how_contribute|99.8%|✅|
|🟢|I want to build a cool bot|enter_data|enter_data|99.8%|✅|
|🟢|Where can I find your source code?|source_code|source_code|99.8%|✅|
|🟢|is your code available?|source_code|source_code|99.8%|✅|
|🟢|You're really cool|react_positive|react_positive|99.8%|✅|
|🟢|can you show me a core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|99.8%|✅|
|🟢|I do not need help installing|deny|deny|99.8%|✅|
|🟢|Rasa core|enter_data|enter_data|99.8%|✅|
|🟢|exit now|canthelp|canthelp|99.8%|✅|
|🟢|i want to use nlu|how_to_get_started|how_to_get_started|99.8%|✅|
|🟢|what is pip?|technical_question|technical_question|99.8%|✅|
|🟢|switch to rasa from another platform|switch|switch|99.8%|✅|
|🟢|how contribute to Rasa|ask_how_contribute|ask_how_contribute|99.8%|✅|
|🟢|you can't help me|canthelp|canthelp|99.8%|✅|
|🟢|who are you|chitchat/ask_whoisit|chitchat/ask_whoisit|99.8%|✅|
|🟢|who are you?|chitchat/ask_whoisit|chitchat/ask_whoisit|99.8%|✅|
|🟢|not right now|deny|deny|99.8%|✅|
|🟢|Why should I devote effort to working on your code|ask_why_contribute|ask_why_contribute|99.8%|✅|
|🟢|Cool. Thanks|thank|thank|99.8%|✅|
|🟢|who the hell are you?|chitchat/ask_whoisit|chitchat/ask_whoisit|99.8%|✅|
|🟢|your code please|source_code|source_code|99.8%|✅|
|🟢|i need the source code to this bot|source_code|source_code|99.8%|✅|
|🟢|hey, i said restart|restart|restart|99.8%|✅|
|🟢|Rasa Open Source is not training at all|broken|broken|99.8%|✅|
|🟢|explain that|explain|explain|99.8%|✅|
|🟢|the playground is not training|broken|broken|99.8%|✅|
|🟢|good bye rasa bot!|bye|bye|99.8%|✅|
|🟢|thanks this is great news|thank|thank|99.8%|✅|
|🟢|someone from customer care|human_handoff|human_handoff|99.8%|✅|
|🟢|your name?|chitchat/ask_whoisit|chitchat/ask_whoisit|99.8%|✅|
|🟢|install Rasa on Linux|install_rasa|install_rasa|99.8%|✅|
|🟢|that's not what i want|canthelp|canthelp|99.8%|✅|
|🟢|I am happy|react_positive|react_positive|99.8%|✅|
|🟢|can you please connect me to a real rasa employee?|human_handoff|human_handoff|99.8%|✅|
|🟢|this conversation is not really helpful|canthelp|canthelp|99.8%|✅|
|🟢|In what way can I contribute.|ask_how_contribute|ask_how_contribute|99.8%|✅|
|🟢|yeah, why not|affirm|affirm|99.8%|✅|
|🟢|can i just test features without having to deal with your predefined conversation|how_to_get_started|how_to_get_started|99.8%|✅|
|🟢|are there simpler ways to create nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.8%|✅|
|🟢|Where can i find the source code|source_code|source_code|99.8%|✅|
|🟢|how to migrate my bot to rasa|switch|switch|99.8%|✅|
|🟢|and you call yourself bot company? pff|canthelp|canthelp|99.8%|✅|
|🟢|can you tell me what I am?|chitchat/ask_whoami|chitchat/ask_whoami|99.8%|✅|
|🟢|Why should I help to improve Rasa|ask_why_contribute|ask_why_contribute|99.8%|✅|
|🟢|what is the best place to get started?|how_to_get_started|how_to_get_started|99.8%|✅|
|🟢|what nlu pipeline would you recommend?|pipeline_recommendation|pipeline_recommendation|99.8%|✅|
|🟢|do you have a core tutorial i can follow|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|99.8%|✅|
|🟢|bad|react_negative|react_negative|99.8%|✅|
|🟢|i need source code|source_code|source_code|99.8%|✅|
|🟢|Great information|react_positive|react_positive|99.8%|✅|
|🟢|that's great|affirm|affirm|99.8%|✅|
|🟢|restart ps|restart|restart|99.8%|✅|
|🟢|can you explain how can i make chatbot like you|how_to_get_started|how_to_get_started|99.8%|✅|
|🟢|i want to built a chatbot please help me|how_to_get_started|how_to_get_started|99.8%|✅|
|🟢|what I can call you|chitchat/ask_whoisit|chitchat/ask_whoisit|99.8%|✅|
|🟢|I want to move from [LUIS.ai](current_api) to Rasa|switch|switch|99.8%|✅|
|🟢|add me to the subscription list|signup_newsletter|signup_newsletter|99.8%|✅|
|🟢|what does NLU server do?|nlu_info|nlu_info|99.8%|✅|
|🟢|tell me your name|chitchat/ask_whoisit|chitchat/ask_whoisit|99.8%|✅|
|🟢|Please restart this chat/|restart|restart|99.8%|✅|
|🟢|hm i don't think you can do what i want|canthelp|canthelp|99.8%|✅|
|🟢|nevermind.... you're not human ... I need to talk to a live person|human_handoff|human_handoff|99.8%|✅|
|🟢|spacy or tensorflow, what is better to start?|pipeline_recommendation|pipeline_recommendation|99.8%|✅|
|🟢|Will the forum take my question?|ask_question_in_forum|ask_question_in_forum|99.7%|✅|
|🟢|I'm getting an error while installing Rasa|need_help_broad|need_help_broad|99.7%|✅|
|🟢|what is your source code|source_code|source_code|99.7%|✅|
|🟢|What ways can one make a contribution?|ask_how_contribute|ask_how_contribute|99.7%|✅|
|🟢|not yet|deny|deny|99.7%|✅|
|🟢|bye for now|bye|bye|99.7%|✅|
|🟢|how can i restart conversation on chatbot|technical_question|technical_question|99.7%|✅|
|🟢|Why be a part of your mission?|ask_why_contribute|ask_why_contribute|99.7%|✅|
|🟢|Why aid your opportunity?|ask_why_contribute|ask_why_contribute|99.7%|✅|
|🟢|NLU|enter_data|enter_data|99.7%|✅|
|🟢|what pipeline is better?|pipeline_recommendation|pipeline_recommendation|99.7%|✅|
|🟢|hey, you promised to contact me, but nobody did, I really need to finish that car insurance bot!!!!|canthelp|canthelp|99.7%|✅|
|🟢|your code|source_code|source_code|99.7%|✅|
|🟢|do you have tutorials about core|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|99.7%|✅|
|🟢|how do I get rasa core|install_rasa|install_rasa|99.7%|✅|
|🟢|this is leading to nothing|canthelp|canthelp|99.7%|✅|
|🟢|which pipeline is better?|pipeline_recommendation|pipeline_recommendation|99.7%|✅|
|🟢|Got it|react_positive|react_positive|99.7%|✅|
|🟢|you can't help me with what i need|canthelp|canthelp|99.7%|✅|
|🟢|i want more information|explain|explain|99.7%|✅|
|🟢|why should I help?|ask_why_contribute|ask_why_contribute|99.7%|✅|
|🟢|Thank you Sara|thank|thank|99.7%|✅|
|🟢|how can i install python|install_rasa|install_rasa|99.7%|✅|
|🟢|I want to make Rasa better|ask_how_contribute|ask_how_contribute|99.7%|✅|
|🟢|restart this conversation|restart|restart|99.7%|✅|
|🟢|stop go back|canthelp|canthelp|99.7%|✅|
|🟢|I like Rasa|react_positive|react_positive|99.7%|✅|
|🟢|i want to restart|restart|restart|99.7%|✅|
|🟢|Where should I eat?|chitchat/ask_restaurant|chitchat/ask_restaurant|99.7%|✅|
|🟢|what's your source code?|source_code|source_code|99.7%|✅|
|🟢|installation steps of rasa|install_rasa|install_rasa|99.7%|✅|
|🟢|please restart the bot|restart|restart|99.7%|✅|
|🟢|how it works?|source_code|source_code|99.7%|✅|
|🟢|I like you|react_positive|react_positive|99.7%|✅|
|🟢|no i get a error while installing|need_help_broad|need_help_broad|99.7%|✅|
|🟢|stop|canthelp|canthelp|99.7%|✅|
|🟢|i want to know restart action|technical_question|technical_question|99.6%|✅|
|🟢|how do i get rasa core|install_rasa|install_rasa|99.6%|✅|
|🟢|tell me who you are|chitchat/ask_whoisit|chitchat/ask_whoisit|99.6%|✅|
|🟢|do we need to write training data nlu.md|technical_question|technical_question|99.6%|✅|
|🟢|cool thank you|thank|thank|99.6%|✅|
|🟢|restart session pls|restart|restart|99.6%|✅|
|🟢|how to work with nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.6%|✅|
|🟢|what does nlu stands for|nlu_info|nlu_info|99.6%|✅|
|🟢|can i look at your source code|source_code|source_code|99.6%|✅|
|🟢|how nice!|affirm|affirm|99.6%|✅|
|🟢|who is this|chitchat/ask_whoisit|chitchat/ask_whoisit|99.6%|✅|
|🟢|why help out?|ask_why_contribute|ask_why_contribute|99.6%|✅|
|🟢|Rasa Core|enter_data|enter_data|99.6%|✅|
|🟢|give me a recommendation|pipeline_recommendation|pipeline_recommendation|99.6%|✅|
|🟢|and rasa nlu?|enter_data|enter_data|99.6%|✅|
|🟢|how does your pricing work?|contact_sales|contact_sales|99.6%|✅|
|🟢|i would like to know why you need that|explain|explain|99.6%|✅|
|🟢|Where can I get the source code of Rasa?|technical_question|technical_question|99.6%|✅|
|🟢|i want to speak to a manager|human_handoff|human_handoff|99.6%|✅|
|🟢|need help on chatbot|need_help_broad|need_help_broad|99.6%|✅|
|🟢|and that's it?|canthelp|canthelp|99.6%|✅|
|🟢|you got me, I accept, if you want me to|affirm|affirm|99.5%|✅|
|🟢|Why contribute to Rasa?|ask_why_contribute|ask_why_contribute|99.5%|✅|
|🟢|that is cool|affirm|affirm|99.5%|✅|
|🟢|I want info on installing Rasa|install_rasa|install_rasa|99.5%|✅|
|🟢|Is there a live demo of rasa somewhere ?|book_demo|book_demo|99.5%|✅|
|🟢|thanks but no thanks|deny|deny|99.5%|✅|
|🟢|ok cool|affirm|affirm|99.5%|✅|
|🟢|yep, will do thank you|affirm|affirm|99.5%|✅|
|🟢|What ways are there to contribute?|ask_how_contribute|ask_how_contribute|99.5%|✅|
|🟢|Rasa installation error|need_help_broad|need_help_broad|99.5%|✅|
|🟢|deploy rasa chat bot in flask|technical_question|technical_question|99.5%|✅|
|🟢|Why add to your business?|ask_why_contribute|ask_why_contribute|99.5%|✅|
|🟢|Where do I ask questions?|ask_question_in_forum|ask_question_in_forum|99.5%|✅|
|🟢|what pipeline is better for what i want?|pipeline_recommendation|pipeline_recommendation|99.5%|✅|
|🟢|awesome|affirm|affirm|99.5%|✅|
|🟢|awesome!|affirm|affirm|99.5%|✅|
|🟢|i want to install|install_rasa|install_rasa|99.5%|✅|
|🟢|hey can you provide me the code of yours|source_code|source_code|99.4%|✅|
|🟢|yep you can restart|restart|restart|99.4%|✅|
|🟢|I don't want to give it to you|deny|deny|99.4%|✅|
|🟢|quit|canthelp|canthelp|99.4%|✅|
|🟢|i want to talk to someone who is smarter than you|human_handoff|human_handoff|99.4%|✅|
|🟢|do you have human support ?|human_handoff|human_handoff|99.4%|✅|
|🟢|how help Rasa|ask_how_contribute|ask_how_contribute|99.4%|✅|
|🟢|Can you shw me some information about intallation?|install_rasa|install_rasa|99.4%|✅|
|🟢|what do you mean|explain|explain|99.4%|✅|
|🟢|can i know your source code ?|source_code|source_code|99.4%|✅|
|🟢|github link?|source_code|source_code|99.4%|✅|
|🟢|Can u tell where is ur code|source_code|source_code|99.4%|✅|
|🟢|what does that mean|explain|explain|99.3%|✅|
|🟢|can you help me with installation of rasa nlu and train my first bot|install_rasa|install_rasa|99.3%|✅|
|🟢|I have something to ask about at the forum.|ask_question_in_forum|ask_question_in_forum|99.3%|✅|
|🟢|show me a tutorial?|faq/tutorials|faq/tutorials|99.3%|✅|
|🟢|how can I train data|technical_question|technical_question|99.3%|✅|
|🟢|yes with your source code|source_code|source_code|99.3%|✅|
|🟢|[luis.ai](current_api)|switch|switch|99.3%|✅|
|🟢|not good|react_negative|react_negative|99.3%|✅|
|🟢|documentation of rasa is very bad|react_negative|react_negative|99.3%|✅|
|🟢|how to install sara in my server|install_rasa|install_rasa|99.3%|✅|
|🟢|i want to use your source code|source_code|source_code|99.2%|✅|
|🟢|not bad|affirm|affirm|99.2%|✅|
|🟢|please elaborate|explain|explain|99.2%|✅|
|🟢|we want to have full code of rasa chatbot|source_code|source_code|99.2%|✅|
|🟢|chatbot|enter_data|enter_data|99.2%|✅|
|🟢|Can i have a deno|book_demo|book_demo|99.2%|✅|
|🟢|rasa nlu|enter_data|enter_data|99.2%|✅|
|🟢|where can I download the source code?|source_code|source_code|99.1%|✅|
|🟢|how do i get rasa nlu|install_rasa|install_rasa|99.1%|✅|
|🟢|i wanna build a bot|how_to_get_started|how_to_get_started|99.1%|✅|
|🟢|where can I find the rasa source code?|source_code|source_code|99.1%|✅|
|🟢|why don't you restart????|restart|restart|99.1%|✅|
|🟢|Ok let's start|affirm|affirm|99.1%|✅|
|🟢|what is your github link|source_code|source_code|99.0%|✅|
|🟢|exit|canthelp|canthelp|98.9%|✅|
|🟢|how to get the source code|source_code|source_code|98.9%|✅|
|🟢|can I install this on a mac?|technical_question|technical_question|98.8%|✅|
|🟢|i have an error on install|need_help_broad|need_help_broad|98.8%|✅|
|🟢|Awesome!|affirm|affirm|98.8%|✅|
|🟢|i want to talk to someone at rasa|human_handoff|human_handoff|98.8%|✅|
|🟢|not sure yet|enter_data|enter_data|98.7%|✅|
|🟢|how do u work?|source_code|source_code|98.7%|✅|
|🟢|i am happy today|react_positive|react_positive|98.6%|✅|
|🟢|do you get anything?|canthelp|canthelp|98.6%|✅|
|🟢|What could I do to contribute?|ask_how_contribute|ask_how_contribute|98.6%|✅|
|🟢|bookin|book_demo|book_demo|98.6%|✅|
|🟢|Is there a way to contribute?|ask_how_contribute|ask_how_contribute|98.5%|✅|
|🟢|could you explain why you need that|explain|explain|98.4%|✅|
|🟢|I would like to have a demo scheduled|book_demo|book_demo|98.3%|✅|
|🟢|I'd absolutely love that|affirm|affirm|98.2%|✅|
|🟢|I want to learn more about your pricing|contact_sales|contact_sales|98.2%|✅|
|🟢|i want to build a bot about me|enter_data|enter_data|98.2%|✅|
|🟢|where can i find this code|source_code|source_code|98.1%|✅|
|🟢|RASA NLU|enter_data|enter_data|98.1%|✅|
|🟢|who are I ?|chitchat/ask_whoami|chitchat/ask_whoami|97.8%|✅|
|🟢|I want to see a demonstration of rasa enterprise|book_demo|book_demo|97.7%|✅|
|🟢|i want to use rasa to build my chatbot|how_to_get_started|how_to_get_started|97.5%|✅|
|🟢|please tell steps for installing chatbot|install_rasa|install_rasa|97.2%|✅|
|🟢|source|source_code|source_code|97.1%|✅|
|🟢|could you tell me more|explain|explain|97.1%|✅|
|🟢|please|affirm|affirm|97.0%|✅|
|🟢|sweet|react_positive|react_positive|96.9%|✅|
|🟢|very bad|deny|deny|96.9%|✅|
|🟢|tell me more about how to use rasa|how_to_get_started|how_to_get_started|96.7%|✅|
|🟢|Exit|bye|canthelp|96.6%|❌|
|🟢|can i see your code|source_code|source_code|96.6%|✅|
|🟢|PLEASE|affirm|affirm|96.6%|✅|
|🟢|I wanted to build a bot my product customer support|how_to_get_started|how_to_get_started|96.6%|✅|
|🟢|I like to build a bot|how_to_get_started|how_to_get_started|96.5%|✅|
|🟢|hi can you speak ?|greet|greet|96.4%|✅|
|🟢|why|explain|explain|96.2%|✅|
|🟢|get a subscription|signup_newsletter|signup_newsletter|96.2%|✅|
|🟢|tensorflow 1.10.0 has requirement numpy<=1.14.5,>=1.13.3, but you'll have numpy 1.16.0 which is incompatible.|technical_question|technical_question|95.8%|✅|
|🟢|What languages can a program like rasa handle?|faq/languages|faq/languages|95.2%|✅|
|🟢|what can I do?|ask_how_contribute|ask_how_contribute|94.6%|✅|
|🟢|Sweet|affirm|react_positive|94.0%|❌|
|🟢|I use [wit.ai](current_api)|switch|switch|93.5%|✅|
|🟢|r u real?|chitchat/ask_ishuman|chitchat/ask_ishuman|93.4%|✅|
|🟢|what are you?|chitchat/ask_whoisit|chitchat/ask_whoisit|93.1%|✅|
|🟢|how can i deploy my server on production?|technical_question|technical_question|93.1%|✅|
|🟢|why do I get errors using rasa?|technical_question|technical_question|92.2%|✅|
|🟢|Rasa NLU|enter_data|enter_data|91.2%|✅|
|🟢|why do you need to know that|explain|explain|90.9%|✅|
|🟢|can you elaborate|explain|explain|90.8%|✅|
|🟢|Deploy to a Server|technical_question|technical_question|90.8%|✅|
|🟡|how i deploy my bot on production server?|technical_question|technical_question|88.3%|✅|
|🟡|got it|enter_data|enter_data|88.2%|✅|
|🟡|how can i get the code for the demo bot?|source_code|source_code|86.6%|✅|
|🟡|What can I do?|chitchat/ask_whatspossible|ask_how_contribute|83.8%|❌|
|🟡|How can I try out rasa enterprise|book_demo|book_demo|81.7%|✅|
|🟡|I want to build a bot|how_to_get_started|how_to_get_started|78.5%|✅|
|🟡|i want to build a bot|enter_data|enter_data|70.7%|✅|
|🟠|i don't want to give you my email|deny|out_of_scope|68.3%|❌|
|🟠|what does the nlu pipeline do|technical_question|technical_question|68.0%|❌|
|🟠|what can I do here|chitchat/ask_whatspossible|chitchat|67.8%|❌|
|🟠|What does the NLU pipeline do|technical_question|technical_question|65.3%|❌|
|🟠|rasa|enter_data|enter_data|60.9%|❌|
|🟠|RASA?|chitchat/ask_whatisrasa|chitchat|60.0%|❌|
|🟠|Rasa NLu|nlu_info|enter_data|55.4%|❌|
|🟠|Which languages can you do?|faq/languages|faq|53.8%|❌|
|🟠|Rasa|enter_data|enter_data|52.1%|❌|

### Sentences with problems
Table with the sentences that were not understood correctly by the model.

||Text|Intent|Predicted intent|Confidence|Understood|
|-|-|-|-|-|-|
|🟢|german|enter_data|out_of_scope/other|100.0%|❌|
|🟢|time|enter_data|chitchat/ask_time|100.0%|❌|
|🟢|4 + 2 = ?|out_of_scope/other|enter_data|100.0%|❌|
|🟢|I want to build a chatbot|how_to_get_started|faq/rasa_components|100.0%|❌|
|🟢|how|out_of_scope/other|chitchat/ask_howdoing|99.9%|❌|
|🟢|Exit|bye|canthelp|96.6%|❌|
|🟢|Sweet|affirm|react_positive|94.0%|❌|
|🟡|What can I do?|chitchat/ask_whatspossible|ask_how_contribute|83.8%|❌|
|🟠|i don't want to give you my email|deny|out_of_scope|68.3%|❌|
|🟠|what does the nlu pipeline do|technical_question|technical_question|68.0%|❌|
|🟠|what can I do here|chitchat/ask_whatspossible|chitchat|67.8%|❌|
|🟠|What does the NLU pipeline do|technical_question|technical_question|65.3%|❌|
|🟠|rasa|enter_data|enter_data|60.9%|❌|
|🟠|RASA?|chitchat/ask_whatisrasa|chitchat|60.0%|❌|
|🟠|Rasa NLu|nlu_info|enter_data|55.4%|❌|
|🟠|Which languages can you do?|faq/languages|faq|53.8%|❌|
|🟠|Rasa|enter_data|enter_data|52.1%|❌|

## Core <a name='core'></a>
Section that discusses metrics about bot responses and actions.

### Metrics
Table with bot core metrics.

||Response|Precision|Recall|F1 Score|Number of occurrences|
|-|-|-|-|-|-|
|🟢|utter_getstarted_new|100.0%|100.0%|100.0%|1|
|🟢|utter_why_rasa_compliant|100.0%|100.0%|100.0%|1|
|🟢|utter_thumbsup|100.0%|100.0%|100.0%|3|
|🟢|utter_ask_continue_sales|100.0%|100.0%|100.0%|1|
|🟢|utter_rasa_components_details|100.0%|100.0%|100.0%|2|
|🟢|utter_ask_playground_install_info|100.0%|100.0%|100.0%|7|
|🟢|action_submit_subscribe_newsletter_form|100.0%|100.0%|100.0%|2|
|🟢|utter_explain_rasa_components|100.0%|100.0%|100.0%|2|
|🟢|utter_explain_nlu|100.0%|100.0%|100.0%|5|
|🟢|utter_why_rasa|100.0%|100.0%|100.0%|1|
|🟢|utter_anything_else|100.0%|100.0%|100.0%|3|
|🟢|utter_installation_command|100.0%|100.0%|100.0%|1|
|🟢|utter_having_trouble_installing|100.0%|100.0%|100.0%|1|
|🟢|utter_run_rasa_init|100.0%|100.0%|100.0%|1|
|🟢|utter_ask_migration|100.0%|100.0%|100.0%|1|
|🟢|action_greet_user|100.0%|100.0%|100.0%|4|
|🟢|utter_link_to_forum|100.0%|100.0%|100.0%|1|
|🟢|utter_contact_email|100.0%|100.0%|100.0%|1|
|🟢|utter_out_of_scope|100.0%|100.0%|100.0%|1|
|🟢|action_store_problem_description|100.0%|100.0%|100.0%|1|
|🟢|utter_explain_core|100.0%|100.0%|100.0%|5|
|🟢|action_set_onboarding|100.0%|100.0%|100.0%|6|
|🟢|action_trigger_response_selector|100.0%|100.0%|100.0%|5|
|🟢|action_submit_sales_form|100.0%|100.0%|100.0%|1|
|🟢|utter_ask_playground_help|100.0%|100.0%|100.0%|1|
|🟢|action_explain_faq|100.0%|100.0%|100.0%|1|
|🟢|utter_why_rasa_os|100.0%|100.0%|100.0%|1|
|🟢|utter_chitchat|100.0%|100.0%|100.0%|4|
|🟢|utter_possibilities_to_contribute|100.0%|100.0%|100.0%|1|
|🟢|utter_faq|100.0%|100.0%|100.0%|5|
|🟢|action_get_community_events|100.0%|100.0%|100.0%|1|
|🟢|utter_built_bot_before|100.0%|100.0%|100.0%|2|
|🟢|utter_ask_x_local_server|100.0%|100.0%|100.0%|2|
|🟢|utter_why_rasa_nlu|100.0%|100.0%|100.0%|1|
|🟢|utter_explain_x|100.0%|100.0%|100.0%|2|
|🟢|utter_ask_ready_to_build|100.0%|100.0%|100.0%|1|
|🟢|utter_ask_explain_nlucorex|100.0%|100.0%|100.0%|2|
|🟢|utter_playground_intro|100.0%|100.0%|100.0%|1|
|🟢|utter_can_do|100.0%|100.0%|100.0%|2|
|🟢|utter_first_bot_with_rasa|100.0%|100.0%|100.0%|5|
|🟢|utter_direct_to_forum_for_help|100.0%|100.0%|100.0%|1|
|🟢|utter_possibilities|100.0%|100.0%|100.0%|1|
|🟢|utter_great|100.0%|100.0%|100.0%|2|
|🟢|utter_greet|100.0%|100.0%|100.0%|2|
|🟢|action_two_stage_fallback|100.0%|100.0%|100.0%|3|
|🟢|utter_ask_more|100.0%|100.0%|100.0%|1|
|🟢|utter_why_rasa_dialogue|100.0%|100.0%|100.0%|1|
|🟢|utter_ask_feedback|100.0%|100.0%|100.0%|3|
|🟢|utter_ask_which_product|100.0%|100.0%|100.0%|6|
|🟢|action_restart_with_button|100.0%|100.0%|100.0%|1|
|🟢|utter_also_explain_nlucore|100.0%|100.0%|100.0%|2|
|🟢|action_listen|100.0%|100.0%|100.0%|71|
|🟢|action_set_faq_slot|100.0%|100.0%|100.0%|5|
|🟢|utter_docu|100.0%|100.0%|100.0%|3|
|🟢|utter_moreinformation|100.0%|100.0%|100.0%|1|
|🟢|utter_rasa_x_local_installation|100.0%|100.0%|100.0%|2|
|🟢|utter_ask_continue_newsletter|100.0%|100.0%|100.0%|1|
|🟢|utter_reasons_to_contribute|100.0%|100.0%|100.0%|1|
|🟢|utter_why_rasa_research|100.0%|100.0%|100.0%|1|
### Confusion Matrix
![Confusion Matrix](https://raw.githubusercontent.com/brunohjs/rasa-model-report/main/docs/image/another_sample_story_confusion_matrix.png 'Confusion Matrix')

## E2E Coverage <a name='e2e'></a>
Section that shows data from intents, entities and responses that aren't covered by end-to-end tests.

### Not covered elements
List with not covered elements by end-to-end tests.

#### Intents
 - ask_when_next_event
 - book_demo
 - broken
 - bye
 - canthelp
 - feedback
 - need_help_broad
 - next_step
 - nlu_generation_tool_recommendation
 - nlu_info
 - pipeline_recommendation
 - react_negative
 - react_positive
 - restart
 - source_code
 - suggestion
 - switch
 - technical_question
 - thank
 - trigger_rephrase

#### Entities
 - amount-of-money
 - company
 - current_api
 - email
 - entity
 - feedback_value
 - job_function
 - language
 - location
 - name
 - nlu_part
 - number
 - retrieval_intent

#### Actions
 - utter_already_subscribed
 - utter_also_explain_core
 - utter_also_explain_nlu
 - utter_awesome
 - utter_bye
 - utter_canthelp
 - utter_cantsignup
 - utter_change_mind
 - utter_chatbot_tutorial
 - utter_confirm_salesrequest
 - utter_confirmationemail
 - utter_could_not_subscribe
 - utter_crf
 - utter_default
 - utter_dont_know_nlu_part
 - utter_duckling
 - utter_duckling_info
 - utter_encourage_building_bot
 - utter_explain_budget
 - utter_explain_business_email
 - utter_explain_company
 - utter_explain_job_function
 - utter_explain_person_name
 - utter_explain_use_case
 - utter_faq_channels_more
 - utter_faq_languages_more
 - utter_faq_ee_more
 - utter_faq_slots_more
 - utter_faq_voice_more
 - utter_tutorialnlu
 - utter_getstarted
 - utter_have_you_used_rasa_before
 - utter_installation_command_followup
 - utter_interested_in_starter_packs
 - utter_interested_in_installation
 - utter_installation_instructions
 - utter_must_accept
 - utter_nlu_entity_tutorial
 - utter_nlu_intent_tutorial
 - utter_nlu_tools
 - utter_no_email
 - utter_no_guide_for_switch
 - utter_no_more_steps
 - utter_no_speak
 - utter_nohelp
 - utter_not_sure
 - utter_noworries
 - utter_offer_recommendation
 - utter_rasa_x_server_installation
 - utter_react_negative
 - utter_react_positive
 - utter_recommend_forum
 - utter_response_why_email
 - utter_restart
 - utter_restart_with_button
 - utter_sales_contact
 - utter_salesrequest_failed
 - utter_search_bar
 - utter_source_code
 - utter_starter_pack_info
 - utter_pipeline_english
 - utter_spacy
 - utter_pipeline_nonenglish_spacy
 - utter_schedule_enterprise_demo
 - utter_suggestion
 - utter_switch_dialogflow
 - utter_switch_luis
 - utter_pipeline_nonenglish_nospacy
 - utter_thank_suggestion
 - utter_what_help
 - utter_what_language
 - utter_x_tutorial
 - utter_no_further_info
 - action_default_ask_affirmation
 - action_default_fallback
 - action_docs_search
 - action_explain_sales_form
 - action_forum_search
 - action_pause
 - action_store_bot_language
 - action_store_entity_extractor
 - action_store_unknown_nlu_part
 - action_store_unknown_product
 - action_tag_docs_search
 - action_tag_feedback
 - action_submit_suggestion_form

Total number of elements: 186

Total number of not covered elements: 119

Coverage rate: 36.0% (🔴)


##### Generated by rasa-model-report, collaborative open-source project for Rasa projects. Github repository at this [link](https://github.com/brunohjs/rasa-model-report).
