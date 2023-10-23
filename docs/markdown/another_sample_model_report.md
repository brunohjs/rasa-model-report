
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
|Bot Name|Rasa Version|Creation date|Updated date|
|:-:|:-:|:-:|:-:|
|<span style='font-size:16px'>Sara - The Rasa Demo Bot</span>|<span style='font-size:16px'>2.8.28</span>|<span style='font-size:16px'>25/02/23 23:54:27</span>|<span style='font-size:16px'>23/10/23 19:02:45</span>|


### Score
|Intent|Entity|NLU|Core|E2E Coverage|<span style='font-size:20px'>Overall</span>|
|:-:|:-:|:-:|:-:|:-:|:-:|
|9.97            |9.97            |9.96            |9.63            |5.23            |<span style='font-size:20px'>**5.74**</span>|
🟢            |🟢            |🟢            |🟢            |🟠            |<span style='font-size:20px'>🟠</span>|
### Element count
Describe the number of elements in the chatbot.

|Element type|Total|
|:-:|:-:|
|Intents|42|
|Entities|16|
|Actions and Utters|165|
|Stories|276|
|Rules|53|



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
|#||intent|Precision|Recall|F1 Score|Examples|
|:-:|-|-|-|-|-|-|
|1|🟢|source_code|100.0%|100.0%|100.0%|34|
|2|🟢|ask_why_contribute|100.0%|100.0%|100.0%|21|
|3|🟢|need_help_broad|100.0%|100.0%|100.0%|41|
|4|🟢|pipeline_recommendation|100.0%|100.0%|100.0%|19|
|5|🟢|book_demo|100.0%|100.0%|100.0%|6|
|6|🟢|signup_newsletter|100.0%|100.0%|100.0%|141|
|7|🟢|canthelp|100.0%|100.0%|100.0%|26|
|8|🟢|restart|100.0%|100.0%|100.0%|10|
|9|🟢|bye|100.0%|100.0%|100.0%|42|
|10|🟢|deny|100.0%|100.0%|100.0%|100|
|11|🟢|greet|100.0%|100.0%|100.0%|147|
|12|🟢|faq|100.0%|100.0%|100.0%|880|
|13|🟢|react_negative|100.0%|100.0%|100.0%|47|
|14|🟢|ask_question_in_forum|100.0%|100.0%|100.0%|42|
|15|🟢|nlu_generation_tool_recommendation|100.0%|100.0%|100.0%|14|
|16|🟢|technical_question|100.0%|100.0%|100.0%|221|
|17|🟢|switch|100.0%|100.0%|100.0%|54|
|18|🟢|human_handoff|100.0%|100.0%|100.0%|69|
|19|🟢|contact_sales|100.0%|100.0%|100.0%|155|
|20|🟢|ask_which_events|100.0%|100.0%|100.0%|107|
|21|🟢|thank|100.0%|100.0%|100.0%|39|
|22|🟢|why_rasa|100.0%|100.0%|100.0%|45|
|23|🟢|broken|100.0%|100.0%|100.0%|15|
|24|🟢|chitchat|99.8%|99.8%|99.8%|812|
|25|🟢|enter_data|99.7%|99.5%|99.6%|759|
|26|🟢|affirm|99.6%|99.6%|99.6%|224|
|27|🟢|out_of_scope|99.0%|99.8%|99.4%|410|
|28|🟢|react_positive|98.5%|100.0%|99.2%|65|
|29|🟢|nlu_info|100.0%|98.4%|99.2%|62|
|30|🟢|how_to_get_started|98.1%|99.5%|98.8%|211|
|31|🟢|install_rasa|100.0%|97.2%|98.6%|108|
|32|🟢|ask_how_contribute|98.1%|98.1%|98.1%|53|
|33|🟢|explain|100.0%|93.8%|96.8%|16|

### Confused intentions
Where all the confusing or wrong sentences of the model are listed.
|#|Text|Intent|Predicted Intent|Confidence|
|:-:|-|-|-|-|
|1|Sweet|affirm|react_positive|99.5%|
|2|There must be a way I can put forth my ideas to the situation.|ask_how_contribute|chitchat|98.5%|
|3|What can I do?|chitchat|ask_how_contribute|98.1%|
|4|german|enter_data|out_of_scope|91.3%|
|5|how do i get rasa nlu|install_rasa|how_to_get_started|87.5%|
|6|time|enter_data|chitchat|85.9%|
|7|how do i get rasa core|install_rasa|how_to_get_started|80.6%|
|8|why is that necessary|explain|out_of_scope|77.7%|
|9|Rasa NLu|nlu_info|enter_data|73.6%|
|10|4 + 2 = ?|out_of_scope|enter_data|71.2%|
|11|how do I get rasa core|install_rasa|how_to_get_started|70.6%|
|12|let's start|how_to_get_started|affirm|60.8%|
|13|customer service|enter_data|out_of_scope|60.6%|
|14|i want to build a bot|enter_data|how_to_get_started|57.9%|
|15|how ?|chitchat|out_of_scope|54.3%|
### Histogram
![Histogram](results/intent_histogram.png 'Histogram')
### Confusion Matrix
![Confusion Matrix](results/intent_confusion_matrix.png 'Confusion Matrix')

## Entities <a name='entities'></a>
Section that discusses metrics about the model entities.

### Metrics
Table with entity metrics.

|#||Entity|Precision|Recall|F1 Score|Examples|
|:-:|-|-|-|-|-|-|
|1|🟢|language|100.0%|100.0%|100.0%|297|
|2|🟢|entity|100.0%|100.0%|100.0%|16|
|3|🟢|location|100.0%|100.0%|100.0%|42|
|4|🟢|name|100.0%|100.0%|100.0%|155|
|5|🟢|nlu_part|100.0%|100.0%|100.0%|94|
|6|🟢|user_type|100.0%|100.0%|100.0%|19|
|7|🟢|install_type|100.0%|100.0%|100.0%|13|
|8|🟢|current_api|100.0%|100.0%|100.0%|64|
|9|🟢|product|99.5%|100.0%|99.7%|554|
|10|🟢|job_function|97.6%|100.0%|98.8%|160|
|11|🟢|company|97.8%|98.9%|98.3%|88|

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
                    <td>RASA?</td>
                    <td>
                        -
                    </td>
                    <td>
                        <details>
                            <summary>product</summary>
                            <pre>start: 0
                            <br>end: 4
                            <br>value: rasa
                            </pre>
                        </details>
                    </td>
                </tr>
                <tr>
                    <td>explain about the rasa dialogue management</td>
                    <td>
                        <details>
                            <summary>product</summary>
                            <pre>start: 23
                            <br>end: 42
                            <br>value: dialogue management
                            </pre>
                        </details>
                    </td>
                    <td>
                        <details>
                            <summary>product</summary>
                            <pre>start: 18
                            <br>end: 22
                            <br>value: rasa
                            </pre>
                        </details>
							<details>
                            <summary>product</summary>
                            <pre>start: 23
                            <br>end: 42
                            <br>value: core
                            </pre>
                        </details>
                    </td>
                </tr>
                <tr>
                    <td>how does rasa dialogue management work?</td>
                    <td>
                        <details>
                            <summary>product</summary>
                            <pre>start: 14
                            <br>end: 33
                            <br>value: dialogue management
                            </pre>
                        </details>
                    </td>
                    <td>
                        <details>
                            <summary>product</summary>
                            <pre>start: 9
                            <br>end: 13
                            <br>value: rasa
                            </pre>
                        </details>
							<details>
                            <summary>product</summary>
                            <pre>start: 14
                            <br>end: 33
                            <br>value: core
                            </pre>
                        </details>
                    </td>
                </tr>
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
                    <td>No job</td>
                    <td>
                        -
                    </td>
                    <td>
                        <details>
                            <summary>job_function</summary>
                            <pre>start: 3
                            <br>end: 6
                            <br>value: job
                            </pre>
                        </details>
                    </td>
                </tr>
                <tr>
                    <td>SCALABLE MINDS</td>
                    <td>
                        -
                    </td>
                    <td>
                        <details>
                            <summary>company</summary>
                            <pre>start: 0
                            <br>end: 14
                            <br>value: SCALABLE MINDS
                            </pre>
                        </details>
                    </td>
                </tr>
                <tr>
                    <td>I am a freelancer</td>
                    <td>
                        <details>
                            <summary>company</summary>
                            <pre>start: 0
                            <br>end: 17
                            <br>value: I am a freelancer
                            </pre>
                        </details>
                    </td>
                    <td>
                        <details>
                            <summary>company</summary>
                            <pre>start: 0
                            <br>end: 6
                            <br>value: I am a
                            </pre>
                        </details>
							<details>
                            <summary>job_function</summary>
                            <pre>start: 7
                            <br>end: 17
                            <br>value: freelancer
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
            </tbody>
        </table>

### Histogram
![Histogram](results/DIETClassifier_histogram.png 'Histogram')
### Confusion Matrix
![Confusion Matrix](results/DIETClassifier_confusion_matrix.png 'Confusion Matrix')

## NLU <a name='nlu'></a>
Section that discusses metrics about NLU and its example phrases.

### Sentences
Table with metrics for bot training phrases.

|#||Text|Intent|Predicted intent|Confidence|Understood|
|:-:|-|-|-|-|-|-|
|1|🟢|Can you say how you were constructed?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2|🟢|How's it going|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|3|🟢|Is everything ok?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|4|🟢|are you alright|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|5|🟢|how are things going|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|6|🟢|how are things with you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|7|🟢|how are you doing this morning|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|8|🟢|how are you doing today?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|9|🟢|how is your day going|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|10|🟢|how's it going?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|11|🟢|how's your day going|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|12|🟢|is everything all right|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|13|🟢|okay hi how are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|14|🟢|Hey Sara, how's it going|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|15|🟢|How many years have you been alive?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|16|🟢|How old will you be on your next birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|17|🟢|What will be your age on your next birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|18|🟢|and you are how many years old?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|19|🟢|how many years old are you?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|20|🟢|how old were you when you celebrated your last birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|21|🟢|how old will you be this year?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|22|🟢|Do you speak any other languages?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|23|🟢|How many languages can you speak?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|24|🟢|In which languages can you speak?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|25|🟢|What are the languages you can speak?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|26|🟢|What languages can you converse in?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|27|🟢|What languages do you speak?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|28|🟢|Which languages are you familiar with?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|29|🟢|Which languages do you speak?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|30|🟢|can you speak Spanish?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|31|🟢|do you speak any other languages?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|32|🟢|what languages are you familiar with?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|33|🟢|what languages do you speak|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|34|🟢|what languages you can speak ?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|35|🟢|you speak french ?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|36|🟢|Could you find me a restaurant to eat at?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|37|🟢|Find a restaurant for me to eat at.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|38|🟢|Find a restaurant for me where I can eat.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|39|🟢|Find me a fast food restaurant.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|40|🟢|Find me a restaurant where I can eat.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|41|🟢|Would you find a restaurant for me?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|42|🟢|Could you tell me what time is it?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|43|🟢|What time is it right now?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|44|🟢|Would you tell me what time it is?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|45|🟢|that's true. do you know what time it is?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|46|🟢|How is the weather today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|47|🟢|Is it hot or cold?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|48|🟢|What is the temperature today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|49|🟢|What is the weather for tomorrow?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|50|🟢|What is the weather in newyork?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|51|🟢|What's the weather forecast?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|52|🟢|What's the weather like over there?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|53|🟢|What's the weather like?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|54|🟢|hows the weather today in berlin?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|55|🟢|the weather today|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|56|🟢|what is the weather like?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|57|🟢|what's the weather like|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|58|🟢|what's the weather like in LA|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|59|🟢|what's the weather like?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|60|🟢|what's the weather today|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|61|🟢|what's the weather today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|62|🟢|whats the weather like tomorrow?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|63|🟢|Can you help me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|64|🟢|How can you help me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|65|🟢|What can you do for me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|66|🟢|can you help me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|67|🟢|can you help me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|68|🟢|hello what can you do for me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|69|🟢|how can you help me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|70|🟢|how can you help me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|71|🟢|how u can help me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|72|🟢|so what can you help me with?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|73|🟢|what are the options?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|74|🟢|what can you do for me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|75|🟢|what can you offer me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|76|🟢|what else can you help with?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|77|🟢|what you can do for me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|78|🟢|you can hep me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|79|🟢|Around where are you from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|80|🟢|where are your parents from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|81|🟢|Wie fange ich mit Rasa an?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|82|🟢|hilf mir beim start|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|83|🟢|de que lugar eres?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|84|🟢|kalhmera sara ti kaneis|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|85|🟢|kannst du auch deutsch?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|86|🟢|kannst du dies auch auf deutsch?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|87|🟢|oui je besoine de l'aide|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|88|🟢|tu parles francais?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|89|🟢|kannst du mir helfen|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|90|🟢|日本語分かる？|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|91|🟢|I'm speaking a non-english language.|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|92|🟢|你懂中文吗？|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|93|🟢|kya hindi me bat kar sakate ho|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|94|🟢|αστεία λές|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|95|🟢|rasa codigo abierto|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|96|🟢|I am asking you an out of scope question|out_of_scope/other|out_of_scope/other|100.0%|✅|
|97|🟢|After registration I see that I have an available balance of 0.00000000. What does this balance represent?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|98|🟢|Are you ready?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|99|🟢|But you're an english site :(|out_of_scope/other|out_of_scope/other|100.0%|✅|
|100|🟢|Can I ask you questions first?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|101|🟢|Can I get a hamburger?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|102|🟢|Can YouTube talk?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|103|🟢|Can you call me back ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|104|🟢|Can you give me your datacenter's password|out_of_scope/other|out_of_scope/other|100.0%|✅|
|105|🟢|Can you give me your datacenter's password?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|106|🟢|Can you make sandwiches?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|107|🟢|Can you please send me an uber|out_of_scope/other|out_of_scope/other|100.0%|✅|
|108|🟢|Do I have to accept?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|109|🟢|Do you know Kevin Pelton|out_of_scope/other|out_of_scope/other|100.0%|✅|
|110|🟢|Find nearest pizzahut|out_of_scope/other|out_of_scope/other|100.0%|✅|
|111|🟢|Have we met before?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|112|🟢|HomeBase is advertised as a community. Is there a way to interact with other members of the community?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|113|🟢|How long does it take to set up a Rasa bot?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|114|🟢|I already told you! I'm a shitmuncher|out_of_scope/other|out_of_scope/other|100.0%|✅|
|115|🟢|I am User|out_of_scope/other|out_of_scope/other|100.0%|✅|
|116|🟢|I am an opioid addic|out_of_scope/other|out_of_scope/other|100.0%|✅|
|117|🟢|I am an opioid addict|out_of_scope/other|out_of_scope/other|100.0%|✅|
|118|🟢|I am hungry|out_of_scope/other|out_of_scope/other|100.0%|✅|
|119|🟢|I am trying to build one, and did some research before, but I have not do hand-on work yet|out_of_scope/other|out_of_scope/other|100.0%|✅|
|120|🟢|I can barely see this white text on light gray background ...|out_of_scope/other|out_of_scope/other|100.0%|✅|
|121|🟢|I changed my mind|out_of_scope/other|out_of_scope/other|100.0%|✅|
|122|🟢|I have installed it|out_of_scope/other|out_of_scope/other|100.0%|✅|
|123|🟢|I ned a GP in 94301|out_of_scope/other|out_of_scope/other|100.0%|✅|
|124|🟢|I need a GP in 94301|out_of_scope/other|out_of_scope/other|100.0%|✅|
|125|🟢|I need a girl friend!|out_of_scope/other|out_of_scope/other|100.0%|✅|
|126|🟢|I need to eat cake|out_of_scope/other|out_of_scope/other|100.0%|✅|
|127|🟢|I wan to buy a plane|out_of_scope/other|out_of_scope/other|100.0%|✅|
|128|🟢|I wanna marry you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|129|🟢|I want a new laptop|out_of_scope/other|out_of_scope/other|100.0%|✅|
|130|🟢|I want book a hotel|out_of_scope/other|out_of_scope/other|100.0%|✅|
|131|🟢|I want french cuisine|out_of_scope/other|out_of_scope/other|100.0%|✅|
|132|🟢|I want pizza|out_of_scope/other|out_of_scope/other|100.0%|✅|
|133|🟢|I want to die|out_of_scope/other|out_of_scope/other|100.0%|✅|
|134|🟢|I want to order pizza|out_of_scope/other|out_of_scope/other|100.0%|✅|
|135|🟢|I want to use pipe|out_of_scope/other|out_of_scope/other|100.0%|✅|
|136|🟢|I will check|out_of_scope/other|out_of_scope/other|100.0%|✅|
|137|🟢|I'm a shitmuncher|out_of_scope/other|out_of_scope/other|100.0%|✅|
|138|🟢|Is Rasa really smart?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|139|🟢|Is this Goal-Oriented Chatbot?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|140|🟢|Is today saturday?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|141|🟢|Mail me the guide|out_of_scope/other|out_of_scope/other|100.0%|✅|
|142|🟢|Make me a sandwich|out_of_scope/other|out_of_scope/other|100.0%|✅|
|143|🟢|Pizza bot|out_of_scope/other|out_of_scope/other|100.0%|✅|
|144|🟢|SEL ME SOMETHING|out_of_scope/other|out_of_scope/other|100.0%|✅|
|145|🟢|The Try it out is not working|out_of_scope/other|out_of_scope/other|100.0%|✅|
|146|🟢|The weather is good|out_of_scope/other|out_of_scope/other|100.0%|✅|
|147|🟢|Try it out broken|out_of_scope/other|out_of_scope/other|100.0%|✅|
|148|🟢|What day is it today?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|149|🟢|What did you eat yesterday?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|150|🟢|What do you prefer?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|151|🟢|What is todays date|out_of_scope/other|out_of_scope/other|100.0%|✅|
|152|🟢|What is your hobbies?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|153|🟢|What makes you better than a human?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|154|🟢|What's 1 + 1?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|155|🟢|What's do YouTube do|out_of_scope/other|out_of_scope/other|100.0%|✅|
|156|🟢|What's your backend system?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|157|🟢|Where am I right now?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|158|🟢|Where am I?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|159|🟢|Who are your customers|out_of_scope/other|out_of_scope/other|100.0%|✅|
|160|🟢|Why don’t you answer?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|161|🟢|Why is my TRUST score set to 50 after I completed the registration process?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|162|🟢|Won't you ask me how I am?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|163|🟢|You'r blue.|out_of_scope/other|out_of_scope/other|100.0%|✅|
|164|🟢|Kristin, I want to marry you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|165|🟢|a tamed mouse will arrive at your doorstep in the next couple of days|out_of_scope/other|out_of_scope/other|100.0%|✅|
|166|🟢|aRE YOU SINGLE|out_of_scope/other|out_of_scope/other|100.0%|✅|
|167|🟢|alexa, order 5 tons of natrium chloride|out_of_scope/other|out_of_scope/other|100.0%|✅|
|168|🟢|and make chicken noises into the phone|out_of_scope/other|out_of_scope/other|100.0%|✅|
|169|🟢|are the newsletter worth the subscription?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|170|🟢|are u facebook|out_of_scope/other|out_of_scope/other|100.0%|✅|
|171|🟢|are u, facebook?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|172|🟢|are you single?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|173|🟢|are you dev?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|174|🟢|are you russian?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|175|🟢|are you sick|out_of_scope/other|out_of_scope/other|100.0%|✅|
|176|🟢|are you vegan|out_of_scope/other|out_of_scope/other|100.0%|✅|
|177|🟢|better than you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|178|🟢|book a ticket|out_of_scope/other|out_of_scope/other|100.0%|✅|
|179|🟢|but I just told you that :(|out_of_scope/other|out_of_scope/other|100.0%|✅|
|180|🟢|but if rasa is open source why do you have a sales team|out_of_scope/other|out_of_scope/other|100.0%|✅|
|181|🟢|buy one please|out_of_scope/other|out_of_scope/other|100.0%|✅|
|182|🟢|buy groceries|out_of_scope/other|out_of_scope/other|100.0%|✅|
|183|🟢|call me father|out_of_scope/other|out_of_scope/other|100.0%|✅|
|184|🟢|can we keep chatting?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|185|🟢|can you book dinner|out_of_scope/other|out_of_scope/other|100.0%|✅|
|186|🟢|can you cheer me up|out_of_scope/other|out_of_scope/other|100.0%|✅|
|187|🟢|can you cook dinner|out_of_scope/other|out_of_scope/other|100.0%|✅|
|188|🟢|can you give me a cup of coffee|out_of_scope/other|out_of_scope/other|100.0%|✅|
|189|🟢|can you help me with the docs?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|190|🟢|can you help me with your docs|out_of_scope/other|out_of_scope/other|100.0%|✅|
|191|🟢|can you help me with your docs?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|192|🟢|can you learn from our conversation?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|193|🟢|can you speak about politic ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|194|🟢|can you understand ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|195|🟢|cannot see|out_of_scope/other|out_of_scope/other|100.0%|✅|
|196|🟢|chinese ok?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|197|🟢|common, just try|out_of_scope/other|out_of_scope/other|100.0%|✅|
|198|🟢|connect to alexa|out_of_scope/other|out_of_scope/other|100.0%|✅|
|199|🟢|custom service|out_of_scope/other|out_of_scope/other|100.0%|✅|
|200|🟢|did i break you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|201|🟢|do you believe in god?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|202|🟢|do you have a phone number?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|203|🟢|do you have your photo?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|204|🟢|do you know me|out_of_scope/other|out_of_scope/other|100.0%|✅|
|205|🟢|do you know ras|out_of_scope/other|out_of_scope/other|100.0%|✅|
|206|🟢|do you liek cheese?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|207|🟢|do you like football|out_of_scope/other|out_of_scope/other|100.0%|✅|
|208|🟢|do you like movies|out_of_scope/other|out_of_scope/other|100.0%|✅|
|209|🟢|do you sell vacuum robots?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|210|🟢|do you want to marry me?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|211|🟢|everything|out_of_scope/other|out_of_scope/other|100.0%|✅|
|212|🟢|example of a chatbot|out_of_scope/other|out_of_scope/other|100.0%|✅|
|213|🟢|genocide|out_of_scope/other|out_of_scope/other|100.0%|✅|
|214|🟢|get me a club mate|out_of_scope/other|out_of_scope/other|100.0%|✅|
|215|🟢|give me a girl friend|out_of_scope/other|out_of_scope/other|100.0%|✅|
|216|🟢|give me food|out_of_scope/other|out_of_scope/other|100.0%|✅|
|217|🟢|great, I'd like to buy a house|out_of_scope/other|out_of_scope/other|100.0%|✅|
|218|🟢|hang on let me find it|out_of_scope/other|out_of_scope/other|100.0%|✅|
|219|🟢|have you ever seen Keith Reilly?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|220|🟢|help with Alma Abrams|out_of_scope/other|out_of_scope/other|100.0%|✅|
|221|🟢|help with my life|out_of_scope/other|out_of_scope/other|100.0%|✅|
|222|🟢|hey little mama let em whisper in your ear|out_of_scope/other|out_of_scope/other|100.0%|✅|
|223|🟢|hey, I contacted you a couple of days ago but didn't get any response, any news?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|224|🟢|how about NYC|out_of_scope/other|out_of_scope/other|100.0%|✅|
|225|🟢|how are Alicia Jackson's cats doing?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|226|🟢|how are the kids|out_of_scope/other|out_of_scope/other|100.0%|✅|
|227|🟢|how can i get them?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|228|🟢|how can i test this|out_of_scope/other|out_of_scope/other|100.0%|✅|
|229|🟢|how come you say ok ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|230|🟢|how do you learn|out_of_scope/other|out_of_scope/other|100.0%|✅|
|231|🟢|how good is Rasa|out_of_scope/other|out_of_scope/other|100.0%|✅|
|232|🟢|how it compares to alexa|out_of_scope/other|out_of_scope/other|100.0%|✅|
|233|🟢|how long have you been online?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|234|🟢|how long will the next version will launch?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|235|🟢|how many lines of codes|out_of_scope/other|out_of_scope/other|100.0%|✅|
|236|🟢|how much is 10 + 89 ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|237|🟢|how much is 10 + 89|out_of_scope/other|out_of_scope/other|100.0%|✅|
|238|🟢|how to get rasa studio|out_of_scope/other|out_of_scope/other|100.0%|✅|
|239|🟢|how to go to newyork ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|240|🟢|i am hungry|out_of_scope/other|out_of_scope/other|100.0%|✅|
|241|🟢|i am hungry, what should i do?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|242|🟢|i am not a developer but need this for business|out_of_scope/other|out_of_scope/other|100.0%|✅|
|243|🟢|i can't deal with _your_ request|out_of_scope/other|out_of_scope/other|100.0%|✅|
|244|🟢|i do not care how are you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|245|🟢|i hope you will be better|out_of_scope/other|out_of_scope/other|100.0%|✅|
|246|🟢|i immediately need help with implementing the coolest bot you can imagine|out_of_scope/other|out_of_scope/other|100.0%|✅|
|247|🟢|i m looking for job|out_of_scope/other|out_of_scope/other|100.0%|✅|
|248|🟢|i told you already|out_of_scope/other|out_of_scope/other|100.0%|✅|
|249|🟢|i wanna party|out_of_scope/other|out_of_scope/other|100.0%|✅|
|250|🟢|i want a non dripping ice cream|out_of_scope/other|out_of_scope/other|100.0%|✅|
|251|🟢|i want caffe|out_of_scope/other|out_of_scope/other|100.0%|✅|
|252|🟢|i want food|out_of_scope/other|out_of_scope/other|100.0%|✅|
|253|🟢|i want good flycam|out_of_scope/other|out_of_scope/other|100.0%|✅|
|254|🟢|i want more of you in my life!|out_of_scope/other|out_of_scope/other|100.0%|✅|
|255|🟢|i want pizza|out_of_scope/other|out_of_scope/other|100.0%|✅|
|256|🟢|i want pizza!!|out_of_scope/other|out_of_scope/other|100.0%|✅|
|257|🟢|i want to book a hotel|out_of_scope/other|out_of_scope/other|100.0%|✅|
|258|🟢|i want to buy a roomba for my grandson|out_of_scope/other|out_of_scope/other|100.0%|✅|
|259|🟢|i want to eat|out_of_scope/other|out_of_scope/other|100.0%|✅|
|260|🟢|i want to find new friends|out_of_scope/other|out_of_scope/other|100.0%|✅|
|261|🟢|i want to find out what you can build with rasa|out_of_scope/other|out_of_scope/other|100.0%|✅|
|262|🟢|i want to fly|out_of_scope/other|out_of_scope/other|100.0%|✅|
|263|🟢|i want to grab lunch|out_of_scope/other|out_of_scope/other|100.0%|✅|
|264|🟢|i want to know current situtation in pakistan|out_of_scope/other|out_of_scope/other|100.0%|✅|
|265|🟢|i want to order a pizza|out_of_scope/other|out_of_scope/other|100.0%|✅|
|266|🟢|i want to see your happy customers|out_of_scope/other|out_of_scope/other|100.0%|✅|
|267|🟢|i will tame a mouse for you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|268|🟢|is John Lewis still married to you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|269|🟢|is it a wasteland full of broken robot parts?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|270|🟢|is it allow to|out_of_scope/other|out_of_scope/other|100.0%|✅|
|271|🟢|is rasa any good|out_of_scope/other|out_of_scope/other|100.0%|✅|
|272|🟢|is that any of your business|out_of_scope/other|out_of_scope/other|100.0%|✅|
|273|🟢|isn't the newsletter just spam?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|274|🟢|it's a pity|out_of_scope/other|out_of_scope/other|100.0%|✅|
|275|🟢|i´m hungry|out_of_scope/other|out_of_scope/other|100.0%|✅|
|276|🟢|machine learning|out_of_scope/other|out_of_scope/other|100.0%|✅|
|277|🟢|mail me the steps|out_of_scope/other|out_of_scope/other|100.0%|✅|
|278|🟢|mascot means?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|279|🟢|mountain|out_of_scope/other|out_of_scope/other|100.0%|✅|
|280|🟢|my name k|out_of_scope/other|out_of_scope/other|100.0%|✅|
|281|🟢|no wait go back i want a dripping ice cream but a cone that catches it so you can drink the ice cream later|out_of_scope/other|out_of_scope/other|100.0%|✅|
|282|🟢|offer me lunch|out_of_scope/other|out_of_scope/other|100.0%|✅|
|283|🟢|oh my god, not again!|out_of_scope/other|out_of_scope/other|100.0%|✅|
|284|🟢|oh wait i gave you my work email address can i change it?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|285|🟢|ok one then|out_of_scope/other|out_of_scope/other|100.0%|✅|
|286|🟢|on wiche nlp based system are you build?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|287|🟢|only that?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|288|🟢|order good|out_of_scope/other|out_of_scope/other|100.0%|✅|
|289|🟢|order pizza|out_of_scope/other|out_of_scope/other|100.0%|✅|
|290|🟢|personal or work?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|291|🟢|pizza|out_of_scope/other|out_of_scope/other|100.0%|✅|
|292|🟢|please help with my ice cream it's dripping|out_of_scope/other|out_of_scope/other|100.0%|✅|
|293|🟢|please hjave lunchj|out_of_scope/other|out_of_scope/other|100.0%|✅|
|294|🟢|please hurry, i have deadline in two weeks to deliver the bot it is for very big company|out_of_scope/other|out_of_scope/other|100.0%|✅|
|295|🟢|please play music|out_of_scope/other|out_of_scope/other|100.0%|✅|
|296|🟢|really? you're so touchy?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|297|🟢|region with no. of records|out_of_scope/other|out_of_scope/other|100.0%|✅|
|298|🟢|remember my name|out_of_scope/other|out_of_scope/other|100.0%|✅|
|299|🟢|search wikipedia|out_of_scope/other|out_of_scope/other|100.0%|✅|
|300|🟢|shitmuncher|out_of_scope/other|out_of_scope/other|100.0%|✅|
|301|🟢|show me a picture of a chicken|out_of_scope/other|out_of_scope/other|100.0%|✅|
|302|🟢|silly bot|out_of_scope/other|out_of_scope/other|100.0%|✅|
|303|🟢|so, I'm helping right now to training you?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|304|🟢|some thing else|out_of_scope/other|out_of_scope/other|100.0%|✅|
|305|🟢|someone call the police i think the bot died|out_of_scope/other|out_of_scope/other|100.0%|✅|
|306|🟢|sorry, i cannot rephrase|out_of_scope/other|out_of_scope/other|100.0%|✅|
|307|🟢|sudo make me a sandwich|out_of_scope/other|out_of_scope/other|100.0%|✅|
|308|🟢|tell me about yourself|out_of_scope/other|out_of_scope/other|100.0%|✅|
|309|🟢|tell me more about next best action|out_of_scope/other|out_of_scope/other|100.0%|✅|
|310|🟢|that doesn't sound like a joke|out_of_scope/other|out_of_scope/other|100.0%|✅|
|311|🟢|that link doesn't work!|out_of_scope/other|out_of_scope/other|100.0%|✅|
|312|🟢|the one that is better than you|out_of_scope/other|out_of_scope/other|100.0%|✅|
|313|🟢|tricked  ya|out_of_scope/other|out_of_scope/other|100.0%|✅|
|314|🟢|turn off my stove|out_of_scope/other|out_of_scope/other|100.0%|✅|
|315|🟢|wait a bit i am still reading|out_of_scope/other|out_of_scope/other|100.0%|✅|
|316|🟢|what about wheather|out_of_scope/other|out_of_scope/other|100.0%|✅|
|317|🟢|what are contextual AI assistants and how different are they from chatbots?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|318|🟢|what are you doing now?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|319|🟢|what are your uses for universities|out_of_scope/other|out_of_scope/other|100.0%|✅|
|320|🟢|what did you eat for lunch?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|321|🟢|what do oyu think about siri?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|322|🟢|what do you think abou siri?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|323|🟢|what do you think about Stanley Ramirez?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|324|🟢|what do you think of alexa|out_of_scope/other|out_of_scope/other|100.0%|✅|
|325|🟢|what does your soul feel my friend|out_of_scope/other|out_of_scope/other|100.0%|✅|
|326|🟢|what doing|out_of_scope/other|out_of_scope/other|100.0%|✅|
|327|🟢|what else?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|328|🟢|what films do you like|out_of_scope/other|out_of_scope/other|100.0%|✅|
|329|🟢|what i do after cd starter-pack-rasa-stack?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|330|🟢|what is a discourse?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|331|🟢|what is a mascot|out_of_scope/other|out_of_scope/other|100.0%|✅|
|332|🟢|what is adlingo|out_of_scope/other|out_of_scope/other|100.0%|✅|
|333|🟢|what is differance between bot and mascot?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|334|🟢|what is evolution ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|335|🟢|what is google rcs|out_of_scope/other|out_of_scope/other|100.0%|✅|
|336|🟢|what is machine learning|out_of_scope/other|out_of_scope/other|100.0%|✅|
|337|🟢|what is nice?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|338|🟢|what is the capital of delhi|out_of_scope/other|out_of_scope/other|100.0%|✅|
|339|🟢|what is the capital of india|out_of_scope/other|out_of_scope/other|100.0%|✅|
|340|🟢|what is the current petrol price|out_of_scope/other|out_of_scope/other|100.0%|✅|
|341|🟢|what is the day ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|342|🟢|what is the real use case where we can use this one|out_of_scope/other|out_of_scope/other|100.0%|✅|
|343|🟢|what is your address?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|344|🟢|what is your purpose|out_of_scope/other|out_of_scope/other|100.0%|✅|
|345|🟢|what lnu mean?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|346|🟢|what the latest news ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|347|🟢|what you ate today?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|348|🟢|what's 5 + 5|out_of_scope/other|out_of_scope/other|100.0%|✅|
|349|🟢|what's a newsletter?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|350|🟢|what's gingerale|out_of_scope/other|out_of_scope/other|100.0%|✅|
|351|🟢|what's your wife doing this weekend|out_of_scope/other|out_of_scope/other|100.0%|✅|
|352|🟢|whats that|out_of_scope/other|out_of_scope/other|100.0%|✅|
|353|🟢|whats the sign|out_of_scope/other|out_of_scope/other|100.0%|✅|
|354|🟢|when is the next train is coming?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|355|🟢|where do i get install files for mac?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|356|🟢|where is Oslo?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|357|🟢|where is mexico?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|358|🟢|wheres the party?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|359|🟢|which city are you talking about?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|360|🟢|which email|out_of_scope/other|out_of_scope/other|100.0%|✅|
|361|🟢|which email should i send to ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|362|🟢|which file is created first while developing chat bot|out_of_scope/other|out_of_scope/other|100.0%|✅|
|363|🟢|which is the LNU asynchronism ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|364|🟢|which kind|out_of_scope/other|out_of_scope/other|100.0%|✅|
|365|🟢|who are the engineers at rasa?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|366|🟢|who are they?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|367|🟢|who is Sharon Zeches|out_of_scope/other|out_of_scope/other|100.0%|✅|
|368|🟢|who is the MD of samsung bangalore ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|369|🟢|who is the president of india ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|370|🟢|who is your favourite robot?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|371|🟢|who let the dog out|out_of_scope/other|out_of_scope/other|100.0%|✅|
|372|🟢|who was hitler|out_of_scope/other|out_of_scope/other|100.0%|✅|
|373|🟢|who will anser my email?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|374|🟢|who's Bill Gates?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|375|🟢|whta you think about gdpr?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|376|🟢|why do you need that?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|377|🟢|why its called rasa ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|378|🟢|will u kill me|out_of_scope/other|out_of_scope/other|100.0%|✅|
|379|🟢|will u kill me?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|380|🟢|winter is already leaving|out_of_scope/other|out_of_scope/other|100.0%|✅|
|381|🟢|with you recommend me?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|382|🟢|would you like some water|out_of_scope/other|out_of_scope/other|100.0%|✅|
|383|🟢|yeah, my dog was drinking a couple of litres of water per day and tried drinking the swimming pool|out_of_scope/other|out_of_scope/other|100.0%|✅|
|384|🟢|you already have that|out_of_scope/other|out_of_scope/other|100.0%|✅|
|385|🟢|you can learn how to make a coffe|out_of_scope/other|out_of_scope/other|100.0%|✅|
|386|🟢|you have children?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|387|🟢|you have job opening|out_of_scope/other|out_of_scope/other|100.0%|✅|
|388|🟢|you lock sweety|out_of_scope/other|out_of_scope/other|100.0%|✅|
|389|🟢|you should learn to count|out_of_scope/other|out_of_scope/other|100.0%|✅|
|390|🟢|you will know it from the single red rose it carries between its teeth|out_of_scope/other|out_of_scope/other|100.0%|✅|
|391|🟢|you're a woman|out_of_scope/other|out_of_scope/other|100.0%|✅|
|392|🟢|ı am learning python|out_of_scope/other|out_of_scope/other|100.0%|✅|
|393|🟢|CALL THE POLICE|out_of_scope/other|out_of_scope/other|100.0%|✅|
|394|🟢|tertyryutyi|out_of_scope/other|out_of_scope/other|100.0%|✅|
|395|🟢|wsdrcftvgybhnj|out_of_scope/other|out_of_scope/other|100.0%|✅|
|396|🟢|why sky is blue?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|397|🟢|what kind of bird are you?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|398|🟢|talk to me about voulette|out_of_scope/other|out_of_scope/other|100.0%|✅|
|399|🟢|voulette voulette|out_of_scope/other|out_of_scope/other|100.0%|✅|
|400|🟢|Do you have a demo?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|401|🟢|please voulette|out_of_scope/other|out_of_scope/other|100.0%|✅|
|402|🟢|Out of scope question.|out_of_scope/other|out_of_scope/other|100.0%|✅|
|403|🟢|i need money|out_of_scope/other|out_of_scope/other|100.0%|✅|
|404|🟢|no, i need cash, money! Do you have it ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|405|🟢|Hi i want to go palghar|out_of_scope/other|out_of_scope/other|100.0%|✅|
|406|🟢|I want to go palghar|out_of_scope/other|out_of_scope/other|100.0%|✅|
|407|🟢|your contry name|out_of_scope/other|out_of_scope/other|100.0%|✅|
|408|🟢|you girl|out_of_scope/other|out_of_scope/other|100.0%|✅|
|409|🟢|expert of rasa|out_of_scope/other|out_of_scope/other|100.0%|✅|
|410|🟢|i want play ball|out_of_scope/other|out_of_scope/other|100.0%|✅|
|411|🟢|flight catch up|out_of_scope/other|out_of_scope/other|100.0%|✅|
|412|🟢|how do you like your coffee|out_of_scope/other|out_of_scope/other|100.0%|✅|
|413|🟢|Can you get analytics on who I'm chatting with when I use Rasa|out_of_scope/other|out_of_scope/other|100.0%|✅|
|414|🟢|coronavirus|out_of_scope/other|out_of_scope/other|100.0%|✅|
|415|🟢|have you heard of corona?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|416|🟢|where do i type in commandy|out_of_scope/other|out_of_scope/other|100.0%|✅|
|417|🟢|where to type in commands|out_of_scope/other|out_of_scope/other|100.0%|✅|
|418|🟢|you have to|out_of_scope/other|out_of_scope/other|100.0%|✅|
|419|🟢|what type of bot?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|420|🟢|asdkjasdhjkasd|out_of_scope/other|out_of_scope/other|100.0%|✅|
|421|🟢|j  bhbhj|out_of_scope/other|out_of_scope/other|100.0%|✅|
|422|🟢|eshdtjfjfyk|out_of_scope/other|out_of_scope/other|100.0%|✅|
|423|🟢|drhdtjfjfyj|out_of_scope/other|out_of_scope/other|100.0%|✅|
|424|🟢|sudo reboot|out_of_scope/other|out_of_scope/other|100.0%|✅|
|425|🟢|asdfgasd|out_of_scope/other|out_of_scope/other|100.0%|✅|
|426|🟢|asdfgasdas|out_of_scope/other|out_of_scope/other|100.0%|✅|
|427|🟢|Do you know which messaging channels rasa supports?|faq/channels|faq/channels|100.0%|✅|
|428|🟢|Any integrations with WhatsApp and Facebook?|faq/channels|faq/channels|100.0%|✅|
|429|🟢|How large roughly speaking is the Rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|430|🟢|How many members in the community?|faq/community_size|faq/community_size|100.0%|✅|
|431|🟢|How many people are in the Rasa Community?|faq/community_size|faq/community_size|100.0%|✅|
|432|🟢|Do you know the difference between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|433|🟢|Is Core different than NLU?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|434|🟢|What is the difference between NLU and Core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|435|🟢|What makes core and nlu different?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|436|🟢|What makes core different from nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|437|🟢|what are the difference between NLU and core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|438|🟢|what differences are there between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|439|🟢|what is different about core compared to nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|440|🟢|what is the difference between core and nlu|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|441|🟢|what is the difference between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|442|🟢|what is the difference between nlu and core|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|443|🟢|what is the difference between nlu and core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|444|🟢|what makes core different from nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|445|🟢|what's the difference between NLU and Core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|446|🟢|what's the difference between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|447|🟢|whats the difference between core and nlu|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|448|🟢|we built a bot with rasa x but now we're interested in the enterprise edition|faq/ee|faq/ee|100.0%|✅|
|449|🟢|what programming language do i need?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|450|🟢|what programming language does rasa use|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|451|🟢|But what kind of programming language is the code written in?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|452|🟢|I would like to know about using Java as a programming language with Rasa|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|453|🟢|Any languages that rasa supports?|faq/languages|faq/languages|100.0%|✅|
|454|🟢|Can rasa support any language?|faq/languages|faq/languages|100.0%|✅|
|455|🟢|Can we make Japanese speaking bot with Rasa?|faq/languages|faq/languages|100.0%|✅|
|456|🟢|Can you use other language than English?|faq/languages|faq/languages|100.0%|✅|
|457|🟢|I want to add Romanian language support|faq/languages|faq/languages|100.0%|✅|
|458|🟢|What all languages does rasa support for us?|faq/languages|faq/languages|100.0%|✅|
|459|🟢|What language u support?|faq/languages|faq/languages|100.0%|✅|
|460|🟢|What language you support?|faq/languages|faq/languages|100.0%|✅|
|461|🟢|What languages can rasa be relied upon to support?|faq/languages|faq/languages|100.0%|✅|
|462|🟢|What languages can rasa handle?|faq/languages|faq/languages|100.0%|✅|
|463|🟢|What languages can rasa support?|faq/languages|faq/languages|100.0%|✅|
|464|🟢|What languages does rasa work for?|faq/languages|faq/languages|100.0%|✅|
|465|🟢|What languages will the utility rasa support?|faq/languages|faq/languages|100.0%|✅|
|466|🟢|Which specific languages does rasa support?|faq/languages|faq/languages|100.0%|✅|
|467|🟢|can rasa speak portuguese?|faq/languages|faq/languages|100.0%|✅|
|468|🟢|can rasa support this language?|faq/languages|faq/languages|100.0%|✅|
|469|🟢|can you tell me what languages rasa supports|faq/languages|faq/languages|100.0%|✅|
|470|🟢|doea rasa support a particular langauage?|faq/languages|faq/languages|100.0%|✅|
|471|🟢|does Rasa support other languages like spanish?|faq/languages|faq/languages|100.0%|✅|
|472|🟢|does rasa works in spanish|faq/languages|faq/languages|100.0%|✅|
|473|🟢|hich languages supports rasa|faq/languages|faq/languages|100.0%|✅|
|474|🟢|how can I add new language to rasa|faq/languages|faq/languages|100.0%|✅|
|475|🟢|how many natural language that rasa supported?|faq/languages|faq/languages|100.0%|✅|
|476|🟢|is it available in Spanish?|faq/languages|faq/languages|100.0%|✅|
|477|🟢|is support for rasa in this language?|faq/languages|faq/languages|100.0%|✅|
|478|🟢|language support|faq/languages|faq/languages|100.0%|✅|
|479|🟢|languages supported|faq/languages|faq/languages|100.0%|✅|
|480|🟢|support for serbian language|faq/languages|faq/languages|100.0%|✅|
|481|🟢|what about languages supported in rasa?|faq/languages|faq/languages|100.0%|✅|
|482|🟢|what language supported by rasa?|faq/languages|faq/languages|100.0%|✅|
|483|🟢|what languages are available?|faq/languages|faq/languages|100.0%|✅|
|484|🟢|what languages can be supported by rasa?|faq/languages|faq/languages|100.0%|✅|
|485|🟢|what languages do you support|faq/languages|faq/languages|100.0%|✅|
|486|🟢|what languages does rasa support?|faq/languages|faq/languages|100.0%|✅|
|487|🟢|which language supports rasa|faq/languages|faq/languages|100.0%|✅|
|488|🟢|which languages does rasa support|faq/languages|faq/languages|100.0%|✅|
|489|🟢|which languages supports rasa|faq/languages|faq/languages|100.0%|✅|
|490|🟢|does rasa support other language beside english?|faq/languages|faq/languages|100.0%|✅|
|491|🟢|even non latin based languages?|faq/languages|faq/languages|100.0%|✅|
|492|🟢|How much do you cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|493|🟢|How much does it cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|494|🟢|How much does rasa cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|495|🟢|How much it costs|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|496|🟢|how much do you cost|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|497|🟢|how much does Rasa cost|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|498|🟢|how much does RASA cost ?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|499|🟢|how much does it cost|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|500|🟢|how much does it cost normally?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|501|🟢|how much does it cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|502|🟢|how much does rasa cost|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|503|🟢|how much does rasa cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|504|🟢|how much it costs?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|505|🟢|is rasa free of cost|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|506|🟢|is rasa stack free|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|507|🟢|what is the enterprise pricing schedule?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|508|🟢|Are you open-source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|509|🟢|Is the rasa software open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|510|🟢|Is your software open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|511|🟢|The rasa software, is that open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|512|🟢|is it open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|513|🟢|is it open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|514|🟢|is rasa Open-Source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|515|🟢|is rasa a type of open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|516|🟢|is rasa an open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|517|🟢|is rasa considered open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|518|🟢|is rasa is open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|519|🟢|is rasa like an open source software|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|520|🟢|is rasa software that is classified as open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|521|🟢|is the software rasa open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|522|🟢|is this open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|523|🟢|is this open source license|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|524|🟢|is your product open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|525|🟢|ist es freie open source software|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|526|🟢|would people consider rasa an open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|527|🟢|would you consider rasa open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|528|🟢|How is it opensource|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|529|🟢|How can I use to rasa to build a voice bot?|faq/voice|faq/voice|100.0%|✅|
|530|🟢|How to use rasa to build a voice bot.|faq/voice|faq/voice|100.0%|✅|
|531|🟢|I could build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|532|🟢|do you have voice recognition|faq/voice|faq/voice|100.0%|✅|
|533|🟢|do you support alexa voice?|faq/voice|faq/voice|100.0%|✅|
|534|🟢|why is that necessary|explain|out_of_scope/other|100.0%|❌|
|535|🟢|Able to integrate with paypal, wordpress, facebook andd twilio|enter_data|enter_data|100.0%|✅|
|536|🟢|I work for Stanford University|enter_data|enter_data|100.0%|✅|
|537|🟢|I'm the lead engineer|enter_data|enter_data|100.0%|✅|
|538|🟢|I’ve trained it in english|enter_data|enter_data|100.0%|✅|
|539|🟢|ACME Mops|enter_data|enter_data|100.0%|✅|
|540|🟢|Al Capone|enter_data|enter_data|100.0%|✅|
|541|🟢|Allianz|enter_data|enter_data|100.0%|✅|
|542|🟢|BCG brazil|enter_data|enter_data|100.0%|✅|
|543|🟢|BCG digital ventures|enter_data|enter_data|100.0%|✅|
|544|🟢|William Zelkind|enter_data|enter_data|100.0%|✅|
|545|🟢|Zendesk|enter_data|enter_data|100.0%|✅|
|546|🟢|allianz|enter_data|enter_data|100.0%|✅|
|547|🟢|assistant to the CEO|enter_data|enter_data|100.0%|✅|
|548|🟢|dutch|enter_data|enter_data|100.0%|✅|
|549|🟢|growth manager|enter_data|enter_data|100.0%|✅|
|550|🟢|klara health|enter_data|enter_data|100.0%|✅|
|551|🟢|ubisoft|enter_data|enter_data|100.0%|✅|
|552|🟢|conversational|enter_data|enter_data|100.0%|✅|
|553|🟢|email = Patti.Salazar@gmail.com|enter_data|enter_data|100.0%|✅|
|554|🟢|i work in biz dev|enter_data|enter_data|100.0%|✅|
|555|🟢|it’s trained in dutch|enter_data|enter_data|100.0%|✅|
|556|🟢|it’s trained in english|enter_data|enter_data|100.0%|✅|
|557|🟢|it’s trained in french|enter_data|enter_data|100.0%|✅|
|558|🟢|it’s trained in italian|enter_data|enter_data|100.0%|✅|
|559|🟢|it’s trained only in dutch|enter_data|enter_data|100.0%|✅|
|560|🟢|it’s trained only in english|enter_data|enter_data|100.0%|✅|
|561|🟢|it’s trained only in french|enter_data|enter_data|100.0%|✅|
|562|🟢|it’s trained only in italian|enter_data|enter_data|100.0%|✅|
|563|🟢|it’s trained only in mandarin|enter_data|enter_data|100.0%|✅|
|564|🟢|it’s trained only in portuguese|enter_data|enter_data|100.0%|✅|
|565|🟢|it’s trained only in spanish|enter_data|enter_data|100.0%|✅|
|566|🟢|the New York Times|enter_data|enter_data|100.0%|✅|
|567|🟢|the ice cream factory is the company|enter_data|enter_data|100.0%|✅|
|568|🟢|the assistant is in dutch|enter_data|enter_data|100.0%|✅|
|569|🟢|the assistant is in english|enter_data|enter_data|100.0%|✅|
|570|🟢|wordpress|enter_data|enter_data|100.0%|✅|
|571|🟢|How's life treating you friend?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|572|🟢|what age were you when you celebrated your last birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|573|🟢|are you a real bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|574|🟢|Any good restaurants nearby?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|575|🟢|hows the weather in bot world|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|576|🟢|well, if you wish: what about the weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|577|🟢|Recharge|out_of_scope/other|out_of_scope/other|100.0%|✅|
|578|🟢|doctor|out_of_scope/other|out_of_scope/other|100.0%|✅|
|579|🟢|Can I use rasa to build a voice bot?|faq/voice|faq/voice|100.0%|✅|
|580|🟢|Will it be correct if I said I can build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|581|🟢|I wanna build a bot that sends the people cute animal pictures based on their favorite color|enter_data|enter_data|100.0%|✅|
|582|🟢|I work for Bayer|enter_data|enter_data|100.0%|✅|
|583|🟢|I'm Harvey Cordano|enter_data|enter_data|100.0%|✅|
|584|🟢|I'm Jeanine Hwang|enter_data|enter_data|100.0%|✅|
|585|🟢|I'm a conversation designer|enter_data|enter_data|100.0%|✅|
|586|🟢|I’ve trained it in dutch|enter_data|enter_data|100.0%|✅|
|587|🟢|I’ve trained it in french|enter_data|enter_data|100.0%|✅|
|588|🟢|I’ve trained it in mandarin|enter_data|enter_data|100.0%|✅|
|589|🟢|No job|enter_data|enter_data|100.0%|✅|
|590|🟢|This is Kim Vanderveen|enter_data|enter_data|100.0%|✅|
|591|🟢|BCBSM|enter_data|enter_data|100.0%|✅|
|592|🟢|BigBotsInc|enter_data|enter_data|100.0%|✅|
|593|🟢|J_Herrera@gmail.com|enter_data|enter_data|100.0%|✅|
|594|🟢|Linda Mchone|enter_data|enter_data|100.0%|✅|
|595|🟢|McKinsey Germany|enter_data|enter_data|100.0%|✅|
|596|🟢|Scalable Minds|enter_data|enter_data|100.0%|✅|
|597|🟢|bayer|enter_data|enter_data|100.0%|✅|
|598|🟢|no job|enter_data|enter_data|100.0%|✅|
|599|🟢|none i will build it from scraps|enter_data|enter_data|100.0%|✅|
|600|🟢|one billion|enter_data|enter_data|100.0%|✅|
|601|🟢|t-mobile US|enter_data|enter_data|100.0%|✅|
|602|🟢|vodafone|enter_data|enter_data|100.0%|✅|
|603|🟢|wurst co kg|enter_data|enter_data|100.0%|✅|
|604|🟢|xyz|enter_data|enter_data|100.0%|✅|
|605|🟢|it’s an dutch bot|enter_data|enter_data|100.0%|✅|
|606|🟢|it’s in dutch|enter_data|enter_data|100.0%|✅|
|607|🟢|it’s only in english but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|608|🟢|it’s trained in mandarin|enter_data|enter_data|100.0%|✅|
|609|🟢|it’s trained in portuguese|enter_data|enter_data|100.0%|✅|
|610|🟢|it’s trained in spanish|enter_data|enter_data|100.0%|✅|
|611|🟢|it’s trained only in chinese|enter_data|enter_data|100.0%|✅|
|612|🟢|my name is Monica Ser|enter_data|enter_data|100.0%|✅|
|613|🟢|one trillion dollar|enter_data|enter_data|100.0%|✅|
|614|🟢|so far it only speaks dutch|enter_data|enter_data|100.0%|✅|
|615|🟢|so far it only speaks english|enter_data|enter_data|100.0%|✅|
|616|🟢|the assistant is in french|enter_data|enter_data|100.0%|✅|
|617|🟢|the assistant is in mandarin|enter_data|enter_data|100.0%|✅|
|618|🟢|the assistant speaks english|enter_data|enter_data|100.0%|✅|
|619|🟢|the language of the ai assistant is dutch|enter_data|enter_data|100.0%|✅|
|620|🟢|the language of the ai assistant is english|enter_data|enter_data|100.0%|✅|
|621|🟢|the people speak dutch|enter_data|enter_data|100.0%|✅|
|622|🟢|local machine|enter_data|enter_data|100.0%|✅|
|623|🟢|Can you give me an idea as to how you were created?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|624|🟢|How were you constructed?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|625|🟢|How are you today?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|626|🟢|how are you feeling|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|627|🟢|how are you today|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|628|🟢|how is your evening|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|629|🟢|nah, I'm good - how are you doing?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|630|🟢|Could you find a restaurant for me?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|631|🟢|Could you find me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|632|🟢|Find a restaurant for me?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|633|🟢|Would you find me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|634|🟢|Do you know what time it is?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|635|🟢|What is the current time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|636|🟢|What's the time right now?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|637|🟢|what is the current time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|638|🟢|How is the weather?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|639|🟢|What's the weather like where I am right now?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|640|🟢|Will we build a snowman today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|641|🟢|how is the weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|642|🟢|how is the weather ?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|643|🟢|how is the weather in berlin?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|644|🟢|how is the weather?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|645|🟢|what is the weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|646|🟢|what is the weather in Berlin|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|647|🟢|what is the weather in zurich?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|648|🟢|what is the weather like where you are?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|649|🟢|What did my parents name me?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|650|🟢|what cn u do for me ?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|651|🟢|what do you know except this?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|652|🟢|tschüssikowski|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|653|🟢|epdi iruka|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|654|🟢|tu kaisi he|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|655|🟢|chgfhgh|out_of_scope/other|out_of_scope/other|100.0%|✅|
|656|🟢|license|out_of_scope/other|out_of_scope/other|100.0%|✅|
|657|🟢|sing me a song|out_of_scope/other|out_of_scope/other|100.0%|✅|
|658|🟢|what?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|659|🟢|the beatles|out_of_scope/other|out_of_scope/other|100.0%|✅|
|660|🟢|Do you know how many people are in the Rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|661|🟢|Is nlu different to core and, if so, how?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|662|🟢|What are some ways that nlu is different from core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|663|🟢|what differences exist between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|664|🟢|what is the main difference between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|665|🟢|what programming language is rasa written in?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|666|🟢|what programming languages does Rasa support?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|667|🟢|what programming language do you recommend|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|668|🟢|programming language|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|669|🟢|Hello, rasa supports spanish?|faq/languages|faq/languages|100.0%|✅|
|670|🟢|What are the languages that rasa supports?|faq/languages|faq/languages|100.0%|✅|
|671|🟢|What are the specific languages that rasa is intended to work with?|faq/languages|faq/languages|100.0%|✅|
|672|🟢|Which languages are supported by rasa?|faq/languages|faq/languages|100.0%|✅|
|673|🟢|are there any languages that rasa supports?|faq/languages|faq/languages|100.0%|✅|
|674|🟢|can rasa understand this language?|faq/languages|faq/languages|100.0%|✅|
|675|🟢|what languages are supported by rasa?|faq/languages|faq/languages|100.0%|✅|
|676|🟢|which languages are supported?|faq/languages|faq/languages|100.0%|✅|
|677|🟢|are you full open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|678|🟢|would you call rasa open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|679|🟢|Great. Are there any tutorials?|faq/tutorials|faq/tutorials|100.0%|✅|
|680|🟢|Could I build a rasa voice bot?|faq/voice|faq/voice|100.0%|✅|
|681|🟢|Do you know how to build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|682|🟢|How can I build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|683|🟢|How could I construct a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|684|🟢|How to build a voice bot using rasa?|faq/voice|faq/voice|100.0%|✅|
|685|🟢|How to build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|686|🟢|I'd like to use rasa to build a voice bot.|faq/voice|faq/voice|100.0%|✅|
|687|🟢|Is it possible to use rasa to build a voice bot?|faq/voice|faq/voice|100.0%|✅|
|688|🟢|how do i build a voice bot?|faq/voice|faq/voice|100.0%|✅|
|689|🟢|how to add voice assitant to chat bot|faq/voice|faq/voice|100.0%|✅|
|690|🟢|what do people do in the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|691|🟢|ACME brands|enter_data|enter_data|100.0%|✅|
|692|🟢|Flexible, but looking for low-cost alternative to proof of concept|enter_data|enter_data|100.0%|✅|
|693|🟢|I wrote it in dutch|enter_data|enter_data|100.0%|✅|
|694|🟢|I'm Gladys Bynum|enter_data|enter_data|100.0%|✅|
|695|🟢|I'm the boss|enter_data|enter_data|100.0%|✅|
|696|🟢|I’ve trained it in italian|enter_data|enter_data|100.0%|✅|
|697|🟢|I’ve trained it in spanish|enter_data|enter_data|100.0%|✅|
|698|🟢|SCALABLE MINDS|enter_data|enter_data|100.0%|✅|
|699|🟢|BigBots|enter_data|enter_data|100.0%|✅|
|700|🟢|Developer Advocate|enter_data|enter_data|100.0%|✅|
|701|🟢|Ebony@gmail.com|enter_data|enter_data|100.0%|✅|
|702|🟢|Full Stack|enter_data|enter_data|100.0%|✅|
|703|🟢|Full stack.|enter_data|enter_data|100.0%|✅|
|704|🟢|Helvetia|enter_data|enter_data|100.0%|✅|
|705|🟢|Im Phyllis Howard|enter_data|enter_data|100.0%|✅|
|706|🟢|Jane Baines|enter_data|enter_data|100.0%|✅|
|707|🟢|John Strickland|enter_data|enter_data|100.0%|✅|
|708|🟢|Kristin@yahoo.com|enter_data|enter_data|100.0%|✅|
|709|🟢|SAP|enter_data|enter_data|100.0%|✅|
|710|🟢|a@b.com|enter_data|enter_data|100.0%|✅|
|711|🟢|arabic|enter_data|enter_data|100.0%|✅|
|712|🟢|developer|enter_data|enter_data|100.0%|✅|
|713|🟢|dutch is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|714|🟢|full stack|enter_data|enter_data|100.0%|✅|
|715|🟢|marketing|enter_data|enter_data|100.0%|✅|
|716|🟢|project manager|enter_data|enter_data|100.0%|✅|
|717|🟢|a bot which sends cute shiba pictures|enter_data|enter_data|100.0%|✅|
|718|🟢|all the training data was in dutch|enter_data|enter_data|100.0%|✅|
|719|🟢|all the training data was in english|enter_data|enter_data|100.0%|✅|
|720|🟢|i'm head of sales|enter_data|enter_data|100.0%|✅|
|721|🟢|it is in dutch|enter_data|enter_data|100.0%|✅|
|722|🟢|it's R_Iuliucci@yahoo.com|enter_data|enter_data|100.0%|✅|
|723|🟢|it's the moabit yoga studio|enter_data|enter_data|100.0%|✅|
|724|🟢|it’s only in dutch but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|725|🟢|it’s only in french but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|726|🟢|my business mail is s_Dibenedetto@Simpson.net|enter_data|enter_data|100.0%|✅|
|727|🟢|my email is K_Spivey@yahoo.com|enter_data|enter_data|100.0%|✅|
|728|🟢|my emayl is V_Comley@Nelson.com|enter_data|enter_data|100.0%|✅|
|729|🟢|my name is betty mclendon|enter_data|enter_data|100.0%|✅|
|730|🟢|my name is Frances Kunkle|enter_data|enter_data|100.0%|✅|
|731|🟢|my name is Nigel Partida|enter_data|enter_data|100.0%|✅|
|732|🟢|my name is Staci Simpson|enter_data|enter_data|100.0%|✅|
|733|🟢|my name is susan crandall|enter_data|enter_data|100.0%|✅|
|734|🟢|so far it only speaks mandarin|enter_data|enter_data|100.0%|✅|
|735|🟢|the assistant is in italian|enter_data|enter_data|100.0%|✅|
|736|🟢|the assistant speaks dutch|enter_data|enter_data|100.0%|✅|
|737|🟢|the bot speaks dutch|enter_data|enter_data|100.0%|✅|
|738|🟢|the bot speaks english|enter_data|enter_data|100.0%|✅|
|739|🟢|the language is dutch|enter_data|enter_data|100.0%|✅|
|740|🟢|the language is english|enter_data|enter_data|100.0%|✅|
|741|🟢|the language of the ai assistant is french|enter_data|enter_data|100.0%|✅|
|742|🟢|the language of the ai assistant is mandarin|enter_data|enter_data|100.0%|✅|
|743|🟢|until now it’s only in dutch|enter_data|enter_data|100.0%|✅|
|744|🟢|until now it’s only in english|enter_data|enter_data|100.0%|✅|
|745|🟢|until now it’s only in mandarin|enter_data|enter_data|100.0%|✅|
|746|🟢|we're building a conversational assistant for our employees to book meeting rooms.|enter_data|enter_data|100.0%|✅|
|747|🟢|botonic|enter_data|enter_data|100.0%|✅|
|748|🟢|botpress|enter_data|enter_data|100.0%|✅|
|749|🟢|local|enter_data|enter_data|100.0%|✅|
|750|🟢|What process was used to build you?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|751|🟢|is everything okay|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|752|🟢|What is your count of years being alive so far?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|753|🟢|Can you tell me what time it is?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|754|🟢|what about the weather in [Lüneburg](location)|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|755|🟢|what can we talk about?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|756|🟢|what programming language is used by rasa|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|757|🟢|does rasa support any languages?|faq/languages|faq/languages|100.0%|✅|
|758|🟢|what language does rasa support?|faq/languages|faq/languages|100.0%|✅|
|759|🟢|I can build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|760|🟢|can i build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|761|🟢|rasa can't be used to build a voice bot, can it?|faq/voice|faq/voice|100.0%|✅|
|762|🟢|with rasa can I build a voice bot?|faq/voice|faq/voice|100.0%|✅|
|763|🟢|what can a person in Rasa do at the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|764|🟢|who is the forum for?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|765|🟢|100000k|enter_data|enter_data|100.0%|✅|
|766|🟢|I work for the New York Times|enter_data|enter_data|100.0%|✅|
|767|🟢|I wrote it in french|enter_data|enter_data|100.0%|✅|
|768|🟢|I'm Virginia Mason|enter_data|enter_data|100.0%|✅|
|769|🟢|I'm an engineer|enter_data|enter_data|100.0%|✅|
|770|🟢|300k|enter_data|enter_data|100.0%|✅|
|771|🟢|[Mr. Sweney](name)|enter_data|enter_data|100.0%|✅|
|772|🟢|N26|enter_data|enter_data|100.0%|✅|
|773|🟢|Product Manager|enter_data|enter_data|100.0%|✅|
|774|🟢|developer advocate|enter_data|enter_data|100.0%|✅|
|775|🟢|english is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|776|🟢|fullstack|enter_data|enter_data|100.0%|✅|
|777|🟢|mandarin is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|778|🟢|ml researcher|enter_data|enter_data|100.0%|✅|
|779|🟢|sales manager|enter_data|enter_data|100.0%|✅|
|780|🟢|i'm in marketing|enter_data|enter_data|100.0%|✅|
|781|🟢|it’s an english bot|enter_data|enter_data|100.0%|✅|
|782|🟢|it’s trained in chinese|enter_data|enter_data|100.0%|✅|
|783|🟢|it’s trained only in german|enter_data|enter_data|100.0%|✅|
|784|🟢|my bot is in dutch|enter_data|enter_data|100.0%|✅|
|785|🟢|my email is Mia_Gainey@gmail.com|enter_data|enter_data|100.0%|✅|
|786|🟢|the assistant is in portuguese|enter_data|enter_data|100.0%|✅|
|787|🟢|the assistant speaks french|enter_data|enter_data|100.0%|✅|
|788|🟢|the language is mandarin|enter_data|enter_data|100.0%|✅|
|789|🟢|Rasa provides me recall and precision?|technical_question|technical_question|100.0%|✅|
|790|🟢|How were you made into who you are?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|791|🟢|how are you doing|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|792|🟢|how are you doing?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|793|🟢|How old were you on your last birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|794|🟢|What was your age on your last birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|795|🟢|how old were you on your last birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|796|🟢|Can you speak more than one language?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|797|🟢|I'm looking for a Spanish restaurant.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|798|🟢|Suggest me a good restaurant around|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|799|🟢|Will you find me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|800|🟢|I want to find some restauant nearby|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|801|🟢|what is time is USA ?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|802|🟢|How is weather today|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|803|🟢|Is it humid out there today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|804|🟢|What is the weather at your place?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|805|🟢|what the wheather like?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|806|🟢|what"s the weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|807|🟢|what's the weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|808|🟢|que puedes hacer?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|809|🟢|你叫什么名字|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|810|🟢|google?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|811|🟢|rasa topics|out_of_scope/other|out_of_scope/other|100.0%|✅|
|812|🟢|contextua|out_of_scope/other|out_of_scope/other|100.0%|✅|
|813|🟢|How to connect messaging channels to rasa?|faq/channels|faq/channels|100.0%|✅|
|814|🟢|rasa supports which messaging channels?|faq/channels|faq/channels|100.0%|✅|
|815|🟢|which messaging channels can I use with rasa?|faq/channels|faq/channels|100.0%|✅|
|816|🟢|which messaging channels does rasa support?|faq/channels|faq/channels|100.0%|✅|
|817|🟢|How large is the Rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|818|🟢|DIFFERENCES BETWEEN CORE AND NLU|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|819|🟢|How does core differ to nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|820|🟢|What does core offer that nlu does not?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|821|🟢|what would you say the difference is between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|822|🟢|Do I need programming skills to develop a chatbot in rasa|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|823|🟢|what is the your programming language|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|824|🟢|What languages can be used with rasa?|faq/languages|faq/languages|100.0%|✅|
|825|🟢|can I use rasa also for another laguage?|faq/languages|faq/languages|100.0%|✅|
|826|🟢|do you have a list of languages rasa supports|faq/languages|faq/languages|100.0%|✅|
|827|🟢|what is the language rasa supports|faq/languages|faq/languages|100.0%|✅|
|828|🟢|which languages do you support|faq/languages|faq/languages|100.0%|✅|
|829|🟢|could I program spanish speaking bots?|faq/languages|faq/languages|100.0%|✅|
|830|🟢|what lanquages do you support|faq/languages|faq/languages|100.0%|✅|
|831|🟢|how much costs the rasa platform|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|832|🟢|is this opensource?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|833|🟢|Can I use my voice to speak to these bots?|faq/voice|faq/voice|100.0%|✅|
|834|🟢|Do you know if I can build a voice bot using rasa?|faq/voice|faq/voice|100.0%|✅|
|835|🟢|I'd like to build a voice bot with rasa.|faq/voice|faq/voice|100.0%|✅|
|836|🟢|Is it possible to build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|837|🟢|It is possible to build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|838|🟢|can I create a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|839|🟢|can rasa be used to build a voice bot?|faq/voice|faq/voice|100.0%|✅|
|840|🟢|What are the rules of the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|841|🟢|What can a person do in the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|842|🟢|What do people do in the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|843|🟢|What is the advantage of rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|844|🟢|10000k|enter_data|enter_data|100.0%|✅|
|845|🟢|240k/year|enter_data|enter_data|100.0%|✅|
|846|🟢|75000-150000 euro|enter_data|enter_data|100.0%|✅|
|847|🟢|I wrote it in english|enter_data|enter_data|100.0%|✅|
|848|🟢|I wrote it in italian|enter_data|enter_data|100.0%|✅|
|849|🟢|I’ve trained it in portuguese|enter_data|enter_data|100.0%|✅|
|850|🟢|My name is Ashleigh Mees|enter_data|enter_data|100.0%|✅|
|851|🟢|My name is Lee George|enter_data|enter_data|100.0%|✅|
|852|🟢|My name si tom Harbin|enter_data|enter_data|100.0%|✅|
|853|🟢|AI engieer|enter_data|enter_data|100.0%|✅|
|854|🟢|AI researcher|enter_data|enter_data|100.0%|✅|
|855|🟢|Club Mate|enter_data|enter_data|100.0%|✅|
|856|🟢|David Carter|enter_data|enter_data|100.0%|✅|
|857|🟢|Developer|enter_data|enter_data|100.0%|✅|
|858|🟢|Ten|enter_data|enter_data|100.0%|✅|
|859|🟢|dutch is the language of my bot|enter_data|enter_data|100.0%|✅|
|860|🟢|english is the language of my bot|enter_data|enter_data|100.0%|✅|
|861|🟢|french is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|862|🟢|italina|enter_data|enter_data|100.0%|✅|
|863|🟢|numbers|enter_data|enter_data|100.0%|✅|
|864|🟢|product manager|enter_data|enter_data|100.0%|✅|
|865|🟢|a health bot|enter_data|enter_data|100.0%|✅|
|866|🟢|all the training data was in french|enter_data|enter_data|100.0%|✅|
|867|🟢|chief nerd at rasa technologies|enter_data|enter_data|100.0%|✅|
|868|🟢|it speaks dutch|enter_data|enter_data|100.0%|✅|
|869|🟢|it’s an portuguese bot|enter_data|enter_data|100.0%|✅|
|870|🟢|it’s available in dutch|enter_data|enter_data|100.0%|✅|
|871|🟢|it’s only in italian but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|872|🟢|it’s only in mandarin but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|873|🟢|my name is Greg King|enter_data|enter_data|100.0%|✅|
|874|🟢|so far it only speaks french|enter_data|enter_data|100.0%|✅|
|875|🟢|the language of the ai assistant is italian|enter_data|enter_data|100.0%|✅|
|876|🟢|£50k|enter_data|enter_data|100.0%|✅|
|877|🟢|websocket|technical_question|technical_question|100.0%|✅|
|878|🟢|What are all of the different languages you can speak?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|879|🟢|What restaurant would you recommend for dinner?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|880|🟢|what is time is US ?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|881|🟢|whats the weather in berlin?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|882|🟢|programming language use|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|883|🟢|do you know of the languages rasa supports|faq/languages|faq/languages|100.0%|✅|
|884|🟢|I need to study RASA step by step, which is the best site to study?|faq/tutorials|faq/tutorials|100.0%|✅|
|885|🟢|5 mln|enter_data|enter_data|100.0%|✅|
|886|🟢|I am Christina Sullivan|enter_data|enter_data|100.0%|✅|
|887|🟢|I spend money|enter_data|enter_data|100.0%|✅|
|888|🟢|I want a bot that sales my product that Catherine Rodriguez finally can focus on important stuff|enter_data|enter_data|100.0%|✅|
|889|🟢|I want to build a bot that can substitute our entire workforce|enter_data|enter_data|100.0%|✅|
|890|🟢|I wrote it in mandarin|enter_data|enter_data|100.0%|✅|
|891|🟢|I'm project manager|enter_data|enter_data|100.0%|✅|
|892|🟢|My name is Louise Caudill|enter_data|enter_data|100.0%|✅|
|893|🟢|The name of the company is Daimler|enter_data|enter_data|100.0%|✅|
|894|🟢|20000k|enter_data|enter_data|100.0%|✅|
|895|🟢|BBC|enter_data|enter_data|100.0%|✅|
|896|🟢|IT manager|enter_data|enter_data|100.0%|✅|
|897|🟢|Willie@gmail.com|enter_data|enter_data|100.0%|✅|
|898|🟢|botium|enter_data|enter_data|100.0%|✅|
|899|🟢|data analyst|enter_data|enter_data|100.0%|✅|
|900|🟢|engineer|enter_data|enter_data|100.0%|✅|
|901|🟢|one which asks me loads about myself|enter_data|enter_data|100.0%|✅|
|902|🟢|a big ol transformer|enter_data|enter_data|100.0%|✅|
|903|🟢|i am interested in ordinals|enter_data|enter_data|100.0%|✅|
|904|🟢|it’s an spanish bot|enter_data|enter_data|100.0%|✅|
|905|🟢|it’s in english|enter_data|enter_data|100.0%|✅|
|906|🟢|it’s in portuguese|enter_data|enter_data|100.0%|✅|
|907|🟢|it’s in spanish|enter_data|enter_data|100.0%|✅|
|908|🟢|my name is Brian Leung|enter_data|enter_data|100.0%|✅|
|909|🟢|one bot|enter_data|enter_data|100.0%|✅|
|910|🟢|picking my nose|enter_data|enter_data|100.0%|✅|
|911|🟢|something to talk to my friends while I'm busy working|enter_data|enter_data|100.0%|✅|
|912|🟢|the assistant speaks mandarin|enter_data|enter_data|100.0%|✅|
|913|🟢|the language of the ai assistant is chinese|enter_data|enter_data|100.0%|✅|
|914|🟢|user can communicate with the bot in english|enter_data|enter_data|100.0%|✅|
|915|🟢|the company is called t10|enter_data|enter_data|100.0%|✅|
|916|🟢|locally|enter_data|enter_data|100.0%|✅|
|917|🟢|Dialogue management|enter_data|enter_data|100.0%|✅|
|918|🟢|can tell me about rasa_sdk|technical_question|technical_question|100.0%|✅|
|919|🟢|What is DIET|technical_question|technical_question|100.0%|✅|
|920|🟢|what is custom actions|technical_question|technical_question|100.0%|✅|
|921|🟢|i want to run rasa x in ibm cloud|technical_question|technical_question|100.0%|✅|
|922|🟢|How are things?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|923|🟢|how is your day|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|924|🟢|How long have you occupied the earth?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|925|🟢|are you real lol|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|926|🟢|are you robot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|927|🟢|are you sure that you're a bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|928|🟢|are you real human?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|929|🟢|How many languages are you familiar with?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|930|🟢|Can you find a restaurant for me?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|931|🟢|Can you find me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|932|🟢|Show me the closest open restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|933|🟢|can you find me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|934|🟢|i want a french restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|935|🟢|What might the time be?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|936|🟢|what time is it|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|937|🟢|what time is it?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|938|🟢|what time it is|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|939|🟢|Can I ask you something about weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|940|🟢|Where are your origins?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|941|🟢|我该如何使用|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|942|🟢|What channels for messaging does rasa support?|faq/channels|faq/channels|100.0%|✅|
|943|🟢|which messaging channels are supported by rasa?|faq/channels|faq/channels|100.0%|✅|
|944|🟢|How large is the community?|faq/community_size|faq/community_size|100.0%|✅|
|945|🟢|How many people are in that community?|faq/community_size|faq/community_size|100.0%|✅|
|946|🟢|what is the difference between nlu and rasa core|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|947|🟢|what the different with rasa nlu and rasa core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|948|🟢|what programming language?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|949|🟢|what programming languages do you support|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|950|🟢|in what programming language is your api|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|951|🟢|How can I change the language|faq/languages|faq/languages|100.0%|✅|
|952|🟢|What languages does rasa work with?|faq/languages|faq/languages|100.0%|✅|
|953|🟢|what are the languages that is supported by rasa?|faq/languages|faq/languages|100.0%|✅|
|954|🟢|Subscription cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|955|🟢|Is Rasa a software formatted as open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|956|🟢|is the project open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|957|🟢|Can I build a rasa voice bot?|faq/voice|faq/voice|100.0%|✅|
|958|🟢|How to build a voice bot?|faq/voice|faq/voice|100.0%|✅|
|959|🟢|I can build a voice bot with rasa, right?|faq/voice|faq/voice|100.0%|✅|
|960|🟢|can I construct a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|961|🟢|can I invent a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|962|🟢|can i build a voice bot|faq/voice|faq/voice|100.0%|✅|
|963|🟢|with rasa can I construct a voice bot?|faq/voice|faq/voice|100.0%|✅|
|964|🟢|with rasa can I invent a voice bot?|faq/voice|faq/voice|100.0%|✅|
|965|🟢|what can people in Rasa do at the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|966|🟢|what is the forum in your community used for|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|967|🟢|1 euro|enter_data|enter_data|100.0%|✅|
|968|🟢|150,000 USD|enter_data|enter_data|100.0%|✅|
|969|🟢|2 euro|enter_data|enter_data|100.0%|✅|
|970|🟢|50,000,000 INR|enter_data|enter_data|100.0%|✅|
|971|🟢|I’ve trained it in chinese|enter_data|enter_data|100.0%|✅|
|972|🟢|My name is jessie maglione|enter_data|enter_data|100.0%|✅|
|973|🟢|1 million big ones|enter_data|enter_data|100.0%|✅|
|974|🟢|I am a freelancer|enter_data|enter_data|100.0%|✅|
|975|🟢|Owner|enter_data|enter_data|100.0%|✅|
|976|🟢|data scientist|enter_data|enter_data|100.0%|✅|
|977|🟢|one|enter_data|enter_data|100.0%|✅|
|978|🟢|extracting durations|enter_data|enter_data|100.0%|✅|
|979|🟢|it's a small company from the US, the name is Microsoft|enter_data|enter_data|100.0%|✅|
|980|🟢|its an dutch bot|enter_data|enter_data|100.0%|✅|
|981|🟢|it’s only in german but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|982|🟢|maybe then instead James@Anast.com|enter_data|enter_data|100.0%|✅|
|983|🟢|my name is Claude Ake|enter_data|enter_data|100.0%|✅|
|984|🟢|sales assitant|enter_data|enter_data|100.0%|✅|
|985|🟢|the assistant speaks portuguese|enter_data|enter_data|100.0%|✅|
|986|🟢|the people speak french|enter_data|enter_data|100.0%|✅|
|987|🟢|the people speak mandarin|enter_data|enter_data|100.0%|✅|
|988|🟢|until now it’s only in french|enter_data|enter_data|100.0%|✅|
|989|🟢|user can communicate with the bot in dutch|enter_data|enter_data|100.0%|✅|
|990|🟢|T10|enter_data|enter_data|100.0%|✅|
|991|🟢|dialogue management|enter_data|enter_data|100.0%|✅|
|992|🟢|DIALOGUE MANAGEMENT|enter_data|enter_data|100.0%|✅|
|993|🟢|how to restart story if am drooping in between|technical_question|technical_question|100.0%|✅|
|994|🟢|Can I run Rasa on a raspberry pi ?|technical_question|technical_question|100.0%|✅|
|995|🟢|can I run rasa on a raspberry pi|technical_question|technical_question|100.0%|✅|
|996|🟢|Can I run rasa on a raspberry pi ?|technical_question|technical_question|100.0%|✅|
|997|🟢|how to add dropdowns?|technical_question|technical_question|100.0%|✅|
|998|🟢|is Rasa works with Unity3d?|technical_question|technical_question|100.0%|✅|
|999|🟢|How long have you been alive?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|1000|🟢|Do you find me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1001|🟢|is it hot outside ?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1002|🟢|como te llamas|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|1003|🟢|sfasd|out_of_scope/other|out_of_scope/other|100.0%|✅|
|1004|🟢|what makes core and nlu unique from each other?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|1005|🟢|Which programming language is rasa written in?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1006|🟢|What languages can rasa use?|faq/languages|faq/languages|100.0%|✅|
|1007|🟢|can we make bot who speaks Japanese?|faq/languages|faq/languages|100.0%|✅|
|1008|🟢|which language do you support?|faq/languages|faq/languages|100.0%|✅|
|1009|🟢|could I call rasa open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1010|🟢|yes, where I can find some hand-on tutorials to use RASA products?|faq/tutorials|faq/tutorials|100.0%|✅|
|1011|🟢|what can people do in the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1012|🟢|I want to build a health insurance bot|enter_data|enter_data|100.0%|✅|
|1013|🟢|I wrote it in portuguese|enter_data|enter_data|100.0%|✅|
|1014|🟢|I wrote it in spanish|enter_data|enter_data|100.0%|✅|
|1015|🟢|I'm a project manager|enter_data|enter_data|100.0%|✅|
|1016|🟢|My budget is oov|enter_data|enter_data|100.0%|✅|
|1017|🟢|300 rupees|enter_data|enter_data|100.0%|✅|
|1018|🟢|CTO|enter_data|enter_data|100.0%|✅|
|1019|🟢|Keith Donnell PhD|enter_data|enter_data|100.0%|✅|
|1020|🟢|Steven Carter's company|enter_data|enter_data|100.0%|✅|
|1021|🟢|brand manager|enter_data|enter_data|100.0%|✅|
|1022|🟢|clue|enter_data|enter_data|100.0%|✅|
|1023|🟢|intel|enter_data|enter_data|100.0%|✅|
|1024|🟢|reddit|enter_data|enter_data|100.0%|✅|
|1025|🟢|all the training data was in italian|enter_data|enter_data|100.0%|✅|
|1026|🟢|all the training data was in mandarin|enter_data|enter_data|100.0%|✅|
|1027|🟢|bout 4,000,000 INR|enter_data|enter_data|100.0%|✅|
|1028|🟢|company: uber|enter_data|enter_data|100.0%|✅|
|1029|🟢|get dates from messages|enter_data|enter_data|100.0%|✅|
|1030|🟢|it’s available in english|enter_data|enter_data|100.0%|✅|
|1031|🟢|it’s in french|enter_data|enter_data|100.0%|✅|
|1032|🟢|it’s only in portuguese but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|1033|🟢|it’s trained in german|enter_data|enter_data|100.0%|✅|
|1034|🟢|my bot is in english|enter_data|enter_data|100.0%|✅|
|1035|🟢|my email is Elinor_Stock@Higgenbotham.com|enter_data|enter_data|100.0%|✅|
|1036|🟢|my name is Earl Ring|enter_data|enter_data|100.0%|✅|
|1037|🟢|my name's Michael Peppers|enter_data|enter_data|100.0%|✅|
|1038|🟢|n/a|enter_data|enter_data|100.0%|✅|
|1039|🟢|sales guy|enter_data|enter_data|100.0%|✅|
|1040|🟢|so far it only speaks italian|enter_data|enter_data|100.0%|✅|
|1041|🟢|the assistant is in chinese|enter_data|enter_data|100.0%|✅|
|1042|🟢|the assistant speaks italian|enter_data|enter_data|100.0%|✅|
|1043|🟢|the bot speaks mandarin|enter_data|enter_data|100.0%|✅|
|1044|🟢|the language is french|enter_data|enter_data|100.0%|✅|
|1045|🟢|the language of the ai assistant is portuguese|enter_data|enter_data|100.0%|✅|
|1046|🟢|the people speak english|enter_data|enter_data|100.0%|✅|
|1047|🟢|until now it’s only in portuguese|enter_data|enter_data|100.0%|✅|
|1048|🟢|until now it’s only in spanish|enter_data|enter_data|100.0%|✅|
|1049|🟢|general and sales|enter_data|enter_data|100.0%|✅|
|1050|🟢|dialog management|enter_data|enter_data|100.0%|✅|
|1051|🟢|what is the policy|technical_question|technical_question|100.0%|✅|
|1052|🟢|hey can i run this onpremise|technical_question|technical_question|100.0%|✅|
|1053|🟢|what is a webhook|technical_question|technical_question|100.0%|✅|
|1054|🟢|Is there a technical paper about DIET?|technical_question|technical_question|100.0%|✅|
|1055|🟢|HI Sara, what are you up to?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1056|🟢|How's it hanging?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1057|🟢|hi how u doing|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1058|🟢|what languages are you good at speaking?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1059|🟢|Hey help me find a restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1060|🟢|What is the exact time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1061|🟢|What is the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1062|🟢|tell me the current time.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1063|🟢|tell me the time it is.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1064|🟢|what is the time ?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1065|🟢|what is the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1066|🟢|Inform me what my name is|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|1067|🟢|Please let me know what my name is|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|1068|🟢|Where do you consider home?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1069|🟢|como inicio en rasa|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|1070|🟢|What channels for messaging are supported by rasa?|faq/channels|faq/channels|100.0%|✅|
|1071|🟢|Which languages can be used by rasa?|faq/languages|faq/languages|100.0%|✅|
|1072|🟢|does rasa aid other languages?|faq/languages|faq/languages|100.0%|✅|
|1073|🟢|does rasa support this language?|faq/languages|faq/languages|100.0%|✅|
|1074|🟢|what different languages does rasa support|faq/languages|faq/languages|100.0%|✅|
|1075|🟢|what is the variety of languages rasa uses|faq/languages|faq/languages|100.0%|✅|
|1076|🟢|what is pricing of rasa|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1077|🟢|are you open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1078|🟢|does rasa fall into the open source software category?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1079|🟢|you are open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1080|🟢|Is rasa suitable to build voice bots?|faq/voice|faq/voice|100.0%|✅|
|1081|🟢|What can I do to build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|1082|🟢|what do we do in the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1083|🟢|10000 dollars|enter_data|enter_data|100.0%|✅|
|1084|🟢|5 euros|enter_data|enter_data|100.0%|✅|
|1085|🟢|I work at the NYT|enter_data|enter_data|100.0%|✅|
|1086|🟢|I work for the new york times|enter_data|enter_data|100.0%|✅|
|1087|🟢|I'm a software engineer|enter_data|enter_data|100.0%|✅|
|1088|🟢|None|enter_data|enter_data|100.0%|✅|
|1089|🟢|Denise Armstrong's company|enter_data|enter_data|100.0%|✅|
|1090|🟢|Jamie Moore|enter_data|enter_data|100.0%|✅|
|1091|🟢|K_Claytor@yahoo.com|enter_data|enter_data|100.0%|✅|
|1092|🟢|None?|enter_data|enter_data|100.0%|✅|
|1093|🟢|abhbose3k@gmail.com|enter_data|enter_data|100.0%|✅|
|1094|🟢|designer|enter_data|enter_data|100.0%|✅|
|1095|🟢|french|enter_data|enter_data|100.0%|✅|
|1096|🟢|mandarin is the language of my bot|enter_data|enter_data|100.0%|✅|
|1097|🟢|it is in french|enter_data|enter_data|100.0%|✅|
|1098|🟢|it’s an mandarin bot|enter_data|enter_data|100.0%|✅|
|1099|🟢|it’s available in french|enter_data|enter_data|100.0%|✅|
|1100|🟢|language = dutch|enter_data|enter_data|100.0%|✅|
|1101|🟢|language: dutch|enter_data|enter_data|100.0%|✅|
|1102|🟢|my email is M_Jones@Luna.com|enter_data|enter_data|100.0%|✅|
|1103|🟢|my name is Tabitha Schoenthal|enter_data|enter_data|100.0%|✅|
|1104|🟢|the language of the ai assistant is german|enter_data|enter_data|100.0%|✅|
|1105|🟢|the language of the ai assistant is spanish|enter_data|enter_data|100.0%|✅|
|1106|🟢|user can talk to my bot in dutch|enter_data|enter_data|100.0%|✅|
|1107|🟢|user can talk to my bot in english|enter_data|enter_data|100.0%|✅|
|1108|🟢|db processing|technical_question|technical_question|100.0%|✅|
|1109|🟢|does rasa support prestashop?|technical_question|technical_question|100.0%|✅|
|1110|🟢|there are some python incompatibilities|technical_question|technical_question|100.0%|✅|
|1111|🟢|can this be integrated with mongo db|technical_question|technical_question|100.0%|✅|
|1112|🟢|In what manner were you constructed?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|1113|🟢|What's the current time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1114|🟢|ljljl|out_of_scope/other|out_of_scope/other|100.0%|✅|
|1115|🟢|Can you tell which messaging channels does rasa support?|faq/channels|faq/channels|100.0%|✅|
|1116|🟢|What messaging channels are supported by rasa?|faq/channels|faq/channels|100.0%|✅|
|1117|🟢|When is the best time to build a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|1118|🟢|5 bucks|enter_data|enter_data|100.0%|✅|
|1119|🟢|50,000 dollar|enter_data|enter_data|100.0%|✅|
|1120|🟢|I'm an AI researcher|enter_data|enter_data|100.0%|✅|
|1121|🟢|200 bucks|enter_data|enter_data|100.0%|✅|
|1122|🟢|200k|enter_data|enter_data|100.0%|✅|
|1123|🟢|5 quid|enter_data|enter_data|100.0%|✅|
|1124|🟢|dev|enter_data|enter_data|100.0%|✅|
|1125|🟢|all the training data was in portuguese|enter_data|enter_data|100.0%|✅|
|1126|🟢|i want to built a Eric Jones bot|enter_data|enter_data|100.0%|✅|
|1127|🟢|i'm Herbert Ball|enter_data|enter_data|100.0%|✅|
|1128|🟢|it’s an french bot|enter_data|enter_data|100.0%|✅|
|1129|🟢|it’s only in chinese but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|1130|🟢|Which other tools can be used to create chatbots?|technical_question|technical_question|100.0%|✅|
|1131|🟢|what does on-premise mean?|technical_question|technical_question|100.0%|✅|
|1132|🟢|i am having trouble setting this up|technical_question|technical_question|100.0%|✅|
|1133|🟢|What was the process for making you?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|1134|🟢|Help me find a restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1135|🟢|i'm looking for a Chinese restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1136|🟢|how's the weather ?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1137|🟢|how's the weather in berlin|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1138|🟢|how's the weather?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1139|🟢|I need help|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1140|🟢|can you do anything else?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1141|🟢|i need help|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1142|🟢|where are you from|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1143|🟢|where are you from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1144|🟢|refresh|out_of_scope/other|out_of_scope/other|100.0%|✅|
|1145|🟢|what are the messaging channels supported by rasa?|faq/channels|faq/channels|100.0%|✅|
|1146|🟢|what is the primary difference between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|1147|🟢|difference between rasa and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|1148|🟢|Does rasa support different languages|faq/languages|faq/languages|100.0%|✅|
|1149|🟢|Which languages can I use with rasa?|faq/languages|faq/languages|100.0%|✅|
|1150|🟢|available for German?|faq/languages|faq/languages|100.0%|✅|
|1151|🟢|what language list can I find for rasa|faq/languages|faq/languages|100.0%|✅|
|1152|🟢|no budget, that why i looking for open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1153|🟢|What is included in rasa open source edition?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1154|🟢|Can you build a voice bot using rasa?|faq/voice|faq/voice|100.0%|✅|
|1155|🟢|what area is the forum for?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1156|🟢|$1|enter_data|enter_data|100.0%|✅|
|1157|🟢|I'm a janitor|enter_data|enter_data|100.0%|✅|
|1158|🟢|$1000|enter_data|enter_data|100.0%|✅|
|1159|🟢|Angel Robinson company|enter_data|enter_data|100.0%|✅|
|1160|🟢|italian is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|1161|🟢|manager|enter_data|enter_data|100.0%|✅|
|1162|🟢|it’s available in spanish|enter_data|enter_data|100.0%|✅|
|1163|🟢|it’s in mandarin|enter_data|enter_data|100.0%|✅|
|1164|🟢|my email is S_Calderon@Cofield.com|enter_data|enter_data|100.0%|✅|
|1165|🟢|ok its P_Simpkins@Suehs.com|enter_data|enter_data|100.0%|✅|
|1166|🟢|the assistant speaks spanish|enter_data|enter_data|100.0%|✅|
|1167|🟢|the bot speaks french|enter_data|enter_data|100.0%|✅|
|1168|🟢|the people speak italian|enter_data|enter_data|100.0%|✅|
|1169|🟢|we plan to build a sales bot to increase our revenue by 100%.|enter_data|enter_data|100.0%|✅|
|1170|🟢|what is significance of domain.yml file|technical_question|technical_question|100.0%|✅|
|1171|🟢|how's life been treating you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1172|🟢|can I ask you anything else?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1173|🟢|what can u do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1174|🟢|what u can do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1175|🟢|what u can do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1176|🟢|what are the primary areas of difference between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|1177|🟢|what's your programming language|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1178|🟢|How do I find out if rasa is open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1179|🟢|is there a tutorial for this?|faq/tutorials|faq/tutorials|100.0%|✅|
|1180|🟢|do you take voice input?|faq/voice|faq/voice|100.0%|✅|
|1181|🟢|What is the scope of the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1182|🟢|ys|affirm|affirm|100.0%|✅|
|1183|🟢|yup|affirm|affirm|100.0%|✅|
|1184|🟢|An ice cube bot|enter_data|enter_data|100.0%|✅|
|1185|🟢|I'm a real good engineer|enter_data|enter_data|100.0%|✅|
|1186|🟢|This is Norma Taylor|enter_data|enter_data|100.0%|✅|
|1187|🟢|mandarin|enter_data|enter_data|100.0%|✅|
|1188|🟢|all the training data was in spanish|enter_data|enter_data|100.0%|✅|
|1189|🟢|it is in mandarin|enter_data|enter_data|100.0%|✅|
|1190|🟢|mail: Geneva.Favors@yahoo.com|enter_data|enter_data|100.0%|✅|
|1191|🟢|so far it only speaks chinese|enter_data|enter_data|100.0%|✅|
|1192|🟢|the bot speaks portuguese|enter_data|enter_data|100.0%|✅|
|1193|🟢|what database rasa use|technical_question|technical_question|100.0%|✅|
|1194|🟢|what is the knowledge base server|technical_question|technical_question|100.0%|✅|
|1195|🟢|does mongodb works for rasax|technical_question|technical_question|100.0%|✅|
|1196|🟢|Recommend me a restaurant around here.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1197|🟢|Could you tell me the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1198|🟢|What's it like out there?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1199|🟢|excellent - is it hot in Berlin?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1200|🟢|is the sun out where zou are?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1201|🟢|what's the weather like where you are?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1202|🟢|what else can you do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1203|🟢|What citizenship do you lay claim to?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1204|🟢|which particular messaging channels are supported by rasa?|faq/channels|faq/channels|100.0%|✅|
|1205|🟢|How do core and nlu differ?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|1206|🟢|Does it have a java library|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1207|🟢|Is RASA NLU avaiable for German?|faq/languages|faq/languages|100.0%|✅|
|1208|🟢|What languages does rasa know?|faq/languages|faq/languages|100.0%|✅|
|1209|🟢|Which different languages does rasa support?|faq/languages|faq/languages|100.0%|✅|
|1210|🟢|I would like to know the cost first.|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1211|🟢|would rasa fall into the category of open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1212|🟢|which python version should i install|faq/python_version|faq/python_version|100.0%|✅|
|1213|🟢|get me some tutorials|faq/tutorials|faq/tutorials|100.0%|✅|
|1214|🟢|Building a voice bot using rasa.|faq/voice|faq/voice|100.0%|✅|
|1215|🟢|what is the forum used for?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1216|🟢|I am a Data Scientist|enter_data|enter_data|100.0%|✅|
|1217|🟢|I work at EXAMPLE insurance group as Head of Innovation|enter_data|enter_data|100.0%|✅|
|1218|🟢|I'm the developer|enter_data|enter_data|100.0%|✅|
|1219|🟢|COO|enter_data|enter_data|100.0%|✅|
|1220|🟢|companies|enter_data|enter_data|100.0%|✅|
|1221|🟢|one that flatters me every morning|enter_data|enter_data|100.0%|✅|
|1222|🟢|i am a projject manager|enter_data|enter_data|100.0%|✅|
|1223|🟢|it speaks english|enter_data|enter_data|100.0%|✅|
|1224|🟢|it’s available in mandarin|enter_data|enter_data|100.0%|✅|
|1225|🟢|my bot is in mandarin|enter_data|enter_data|100.0%|✅|
|1226|🟢|the language is italian|enter_data|enter_data|100.0%|✅|
|1227|🟢|Sorry  it's not suleman is Shehzad|enter_data|enter_data|100.0%|✅|
|1228|🟢|how to use formaction|technical_question|technical_question|100.0%|✅|
|1229|🟢|can I form a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|1230|🟢|with rasa can I form a voice bot|faq/voice|faq/voice|100.0%|✅|
|1231|🟢|YUP|affirm|affirm|100.0%|✅|
|1232|🟢|Evaluate Rasa :-)|enter_data|enter_data|100.0%|✅|
|1233|🟢|My name is Shane Goodyear|enter_data|enter_data|100.0%|✅|
|1234|🟢|K_Rainey@Yochum.net|enter_data|enter_data|100.0%|✅|
|1235|🟢|english|enter_data|enter_data|100.0%|✅|
|1236|🟢|i'm a race car driver|enter_data|enter_data|100.0%|✅|
|1237|🟢|it's Robert Weir|enter_data|enter_data|100.0%|✅|
|1238|🟢|it’s an italian bot|enter_data|enter_data|100.0%|✅|
|1239|🟢|my email is Virginia@Brown.com|enter_data|enter_data|100.0%|✅|
|1240|🟢|the people speak chinese|enter_data|enter_data|100.0%|✅|
|1241|🟢|user can communicate with the bot in mandarin|enter_data|enter_data|100.0%|✅|
|1242|🟢|i need help with policies|technical_question|technical_question|100.0%|✅|
|1243|🟢|is slot teh same as entity|technical_question|technical_question|100.0%|✅|
|1244|🟢|How you doing?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1245|🟢|how are xou|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1246|🟢|how you doing|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1247|🟢|how you doing?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1248|🟢|are you really a bot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1249|🟢|In what languages are you fluent enough?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1250|🟢|Speak any other languages?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1251|🟢|Excuse me, what time is it?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1252|🟢|What time is it in Berlin?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1253|🟢|do you know the current time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1254|🟢|what is the time in Sydney?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1255|🟢|Will I require my raincoat today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1256|🟢|I'd like to know what my name is|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|1257|🟢|help pls|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1258|🟢|how can you help?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1259|🟢|show me the menu|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1260|🟢|what can you teache me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1261|🟢|What location are you from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1262|🟢|how to use rasa in salesforce|faq/channels|faq/channels|100.0%|✅|
|1263|🟢|Rasa supports some messaging channels, what are those?|faq/channels|faq/channels|100.0%|✅|
|1264|🟢|What is the magnitude of the Rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|1265|🟢|difference between Rasa and Rasa X|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|1266|🟢|Can you tell me about the enterprise edition?|faq/ee|faq/ee|100.0%|✅|
|1267|🟢|I want information about the enterprise edition|faq/ee|faq/ee|100.0%|✅|
|1268|🟢|what programming languge do i use|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1269|🟢|shall i use Nodejs as a programming language|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1270|🟢|in which langauges can i build a rasa bot|faq/languages|faq/languages|100.0%|✅|
|1271|🟢|What lanquages do you serve|faq/languages|faq/languages|100.0%|✅|
|1272|🟢|Could you tell me whether rasa is open source or not?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1273|🟢|which python version|faq/python_version|faq/python_version|100.0%|✅|
|1274|🟢|what is the chance of building a rasa voice bot?|faq/voice|faq/voice|100.0%|✅|
|1275|🟢|What happens in the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1276|🟢|ACME bank|enter_data|enter_data|100.0%|✅|
|1277|🟢|I'm a machine learning engineer|enter_data|enter_data|100.0%|✅|
|1278|🟢|accenture|enter_data|enter_data|100.0%|✅|
|1279|🟢|german is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|1280|🟢|around $500,000 per year|enter_data|enter_data|100.0%|✅|
|1281|🟢|i have about 200 bucks in my savings account|enter_data|enter_data|100.0%|✅|
|1282|🟢|i sell turtles|enter_data|enter_data|100.0%|✅|
|1283|🟢|the bot speaks italian|enter_data|enter_data|100.0%|✅|
|1284|🟢|until now it’s only in italian|enter_data|enter_data|100.0%|✅|
|1285|🟢|can we use regex is rasa code|technical_question|technical_question|100.0%|✅|
|1286|🟢|how can I get a docker image|technical_question|technical_question|100.0%|✅|
|1287|🟢|how to connect mongodb|technical_question|technical_question|100.0%|✅|
|1288|🟢|Would you find any restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1289|🟢|I work as a project manager|enter_data|enter_data|100.0%|✅|
|1290|🟢|It is Drew@Mccarthy.com|enter_data|enter_data|100.0%|✅|
|1291|🟢|My email is Richard@Simmons.com|enter_data|enter_data|100.0%|✅|
|1292|🟢|2000k|enter_data|enter_data|100.0%|✅|
|1293|🟢|Lithuanian|enter_data|enter_data|100.0%|✅|
|1294|🟢|a chatbot for mops - mopbot|enter_data|enter_data|100.0%|✅|
|1295|🟢|it’s in italian|enter_data|enter_data|100.0%|✅|
|1296|🟢|mi name is Kathy Wright|enter_data|enter_data|100.0%|✅|
|1297|🟢|my bot is in portuguese|enter_data|enter_data|100.0%|✅|
|1298|🟢|the assistant speaks chinese|enter_data|enter_data|100.0%|✅|
|1299|🟢|user can communicate with the bot in french|enter_data|enter_data|100.0%|✅|
|1300|🟢|best policies to be used|technical_question|technical_question|100.0%|✅|
|1301|🟢|what are the policy available|technical_question|technical_question|100.0%|✅|
|1302|🟢|Do you know how you were built?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|1303|🟢|I want to know how you were formed|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|1304|🟢|how's life|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1305|🟢|Are you a bot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1306|🟢|are you a BOT|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1307|🟢|are you a bot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1308|🟢|are you a bot ?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1309|🟢|are you a bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1310|🟢|are you a robot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1311|🟢|you are a robot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1312|🟢|Could you please show me what you can|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1313|🟢|what can i do now|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1314|🟢|Nice name|out_of_scope/other|out_of_scope/other|100.0%|✅|
|1315|🟢|can someone help me with infos about rasa x|faq/rasax|faq/rasax|100.0%|✅|
|1316|🟢|whats the diff between rasa and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|1317|🟢|Does rasa require programming knowledge|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1318|🟢|your NLU understand spanish?|faq/languages|faq/languages|100.0%|✅|
|1319|🟢|basic tutorials|faq/tutorials|faq/tutorials|100.0%|✅|
|1320|🟢|what exactly is the forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1321|🟢|what is the forum in Rasa used for|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1322|🟢|yes i accept|affirm|affirm|100.0%|✅|
|1323|🟢|50k|enter_data|enter_data|100.0%|✅|
|1324|🟢|I'm a full stack developer|enter_data|enter_data|100.0%|✅|
|1325|🟢|500k|enter_data|enter_data|100.0%|✅|
|1326|🟢|data science engineer|enter_data|enter_data|100.0%|✅|
|1327|🟢|french is the language of my bot|enter_data|enter_data|100.0%|✅|
|1328|🟢|one that will get me promoted|enter_data|enter_data|100.0%|✅|
|1329|🟢|faq|enter_data|enter_data|100.0%|✅|
|1330|🟢|it is in english|enter_data|enter_data|100.0%|✅|
|1331|🟢|its an mandarin bot|enter_data|enter_data|100.0%|✅|
|1332|🟢|it’s only in spanish but I plan to train it in other languages|enter_data|enter_data|100.0%|✅|
|1333|🟢|my name is james culpit|enter_data|enter_data|100.0%|✅|
|1334|🟢|my name is Jermaine Mccleery|enter_data|enter_data|100.0%|✅|
|1335|🟢|sales bot|enter_data|enter_data|100.0%|✅|
|1336|🟢|the bot speaks spanish|enter_data|enter_data|100.0%|✅|
|1337|🟢|we plan with 250.000 euro for one year|enter_data|enter_data|100.0%|✅|
|1338|🟢|what is endpoint|technical_question|technical_question|100.0%|✅|
|1339|🟢|how to handle sending scheduled message to custom webhooks|technical_question|technical_question|100.0%|✅|
|1340|🟢|can you help me with this problem|technical_question|technical_question|100.0%|✅|
|1341|🟢|rasa sdk|technical_question|technical_question|100.0%|✅|
|1342|🟢|are you bot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1343|🟢|are you bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1344|🟢|what is the temperature|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1345|🟢|What makes core distinct to nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|1346|🟢|Do you see an application of rasa in voice bot building?|faq/voice|faq/voice|100.0%|✅|
|1347|🟢|60 million INR|enter_data|enter_data|100.0%|✅|
|1348|🟢|900 dollars|enter_data|enter_data|100.0%|✅|
|1349|🟢|CEO|enter_data|enter_data|100.0%|✅|
|1350|🟢|Carolyn.Eisenhauer@Watkins.com|enter_data|enter_data|100.0%|✅|
|1351|🟢|it is in italian|enter_data|enter_data|100.0%|✅|
|1352|🟢|oov per year|enter_data|enter_data|100.0%|✅|
|1353|🟢|until now it’s only in chinese|enter_data|enter_data|100.0%|✅|
|1354|🟢|can you show me buttons|technical_question|technical_question|100.0%|✅|
|1355|🟢|rasa uses deep learning ?|technical_question|technical_question|100.0%|✅|
|1356|🟢|By what method were you fashioned?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|1357|🟢|Ahoy matey how are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1358|🟢|Hi Sara! How are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1359|🟢|hi sara, how are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1360|🟢|what languages you can handle well?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1361|🟢|Could you tell me the time, please?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1362|🟢|Are there any meteorological changes that I need to be aware of?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1363|🟢|whats the temperature in delhi?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1364|🟢|show me what's possible|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1365|🟢|So where are you from|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1366|🟢|What is your original location?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1367|🟢|colder|out_of_scope/other|out_of_scope/other|100.0%|✅|
|1368|🟢|lunch|out_of_scope/other|out_of_scope/other|100.0%|✅|
|1369|🟢|lunch??|out_of_scope/other|out_of_scope/other|100.0%|✅|
|1370|🟢|contextual|out_of_scope/other|out_of_scope/other|100.0%|✅|
|1371|🟢|tell me about rasa enterprise|faq/ee|faq/ee|100.0%|✅|
|1372|🟢|which programming language are you written in?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1373|🟢|Not sure what slots are.|faq/slots|faq/slots|100.0%|✅|
|1374|🟢|Not sure what slots are?|faq/slots|faq/slots|100.0%|✅|
|1375|🟢|When can I build a voice bot using rasa?|faq/voice|faq/voice|100.0%|✅|
|1376|🟢|can I make a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|1377|🟢|with rasa can I make a voice bot?|faq/voice|faq/voice|100.0%|✅|
|1378|🟢|Could you please describe the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1379|🟢|what does a person do in the Rasa forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1380|🟢|ya|affirm|affirm|100.0%|✅|
|1381|🟢|I'm a business woman|enter_data|enter_data|100.0%|✅|
|1382|🟢|around one millon euros|enter_data|enter_data|100.0%|✅|
|1383|🟢|i use anaconda|enter_data|enter_data|100.0%|✅|
|1384|🟢|it’s available in italian|enter_data|enter_data|100.0%|✅|
|1385|🟢|my email is Carole@Hart.com|enter_data|enter_data|100.0%|✅|
|1386|🟢|is this test compatible with linux?|technical_question|technical_question|100.0%|✅|
|1387|🟢|how to use form actions|technical_question|technical_question|100.0%|✅|
|1388|🟢|do you know what language rasa uses|faq/languages|faq/languages|100.0%|✅|
|1389|🟢|Yes, I accept|affirm|affirm|100.0%|✅|
|1390|🟢|I am a data scientist|enter_data|enter_data|100.0%|✅|
|1391|🟢|I'm in project mgmt|enter_data|enter_data|100.0%|✅|
|1392|🟢|Terri Cline|enter_data|enter_data|100.0%|✅|
|1393|🟢|can you try E_Conder@gmail.com instead?|enter_data|enter_data|100.0%|✅|
|1394|🟢|it's Katie Betz|enter_data|enter_data|100.0%|✅|
|1395|🟢|what is helm|technical_question|technical_question|100.0%|✅|
|1396|🟢|yes what if i have to code open end responses into some categories|technical_question|technical_question|100.0%|✅|
|1397|🟢|hm that doesnt quite help me is there anything else you can do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1398|🟢|Today|out_of_scope/other|out_of_scope/other|100.0%|✅|
|1399|🟢|german?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|1400|🟢|How many people are in your community|faq/community_size|faq/community_size|100.0%|✅|
|1401|🟢|How many people are in your community?|faq/community_size|faq/community_size|100.0%|✅|
|1402|🟢|What facts diverge core from nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|1403|🟢|the difference between Rasa and Rasa X|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|1404|🟢|what's the rasa x enterprise edition|faq/ee|faq/ee|100.0%|✅|
|1405|🟢|which language can I use with rasa?|faq/languages|faq/languages|100.0%|✅|
|1406|🟢|can I use rasa to build alexa skills|faq/voice|faq/voice|100.0%|✅|
|1407|🟢|whats in the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1408|🟢|Robert.Sparks@gmail.com|enter_data|enter_data|100.0%|✅|
|1409|🟢|german|enter_data|out_of_scope/other|100.0%|❌|
|1410|🟢|i'm in customer success|enter_data|enter_data|100.0%|✅|
|1411|🟢|it is in portuguese|enter_data|enter_data|100.0%|✅|
|1412|🟢|it’s available in portuguese|enter_data|enter_data|100.0%|✅|
|1413|🟢|my bot is in french|enter_data|enter_data|100.0%|✅|
|1414|🟢|so far it only speaks spanish|enter_data|enter_data|100.0%|✅|
|1415|🟢|how to use forms|technical_question|technical_question|100.0%|✅|
|1416|🟢|deploy rasa chat bot in flask|technical_question|technical_question|100.0%|✅|
|1417|🟢|Show me how to find a restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1418|🟢|languages|faq/languages|faq/languages|100.0%|✅|
|1419|🟢|what dialects does rasa support|faq/languages|faq/languages|100.0%|✅|
|1420|🟢|Okay|affirm|affirm|100.0%|✅|
|1421|🟢|Okay!|affirm|affirm|100.0%|✅|
|1422|🟢|yeeeeezzzzz|affirm|affirm|100.0%|✅|
|1423|🟢|150,000$/ year|enter_data|enter_data|100.0%|✅|
|1424|🟢|20k|enter_data|enter_data|100.0%|✅|
|1425|🟢|400 trilion|enter_data|enter_data|100.0%|✅|
|1426|🟢|chief lemonade officer|enter_data|enter_data|100.0%|✅|
|1427|🟢|it's Shannon.Adelman@Hurt.com|enter_data|enter_data|100.0%|✅|
|1428|🟢|my job function is developer|enter_data|enter_data|100.0%|✅|
|1429|🟢|my name is Alexander Kohn|enter_data|enter_data|100.0%|✅|
|1430|🟢|the language is chinese|enter_data|enter_data|100.0%|✅|
|1431|🟢|user can talk to my bot in mandarin|enter_data|enter_data|100.0%|✅|
|1432|🟢|Hello, where can I find the paper about DIET?|technical_question|technical_question|100.0%|✅|
|1433|🟢|how to set threshold ?|technical_question|technical_question|100.0%|✅|
|1434|🟢|I'd like to know how you were created|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|1435|🟢|Tell me your day, month and year of birth.|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|1436|🟢|can i be shown a gluten free restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1437|🟢|What city were you born in?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1438|🟢|Which languages can you do?|faq/languages|faq/languages|100.0%|✅|
|1439|🟢|What is the cost of RASA?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1440|🟢|Building a rasa voice bot?|faq/voice|faq/voice|100.0%|✅|
|1441|🟢|what can you put in the forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1442|🟢|I’ve trained it in german|enter_data|enter_data|100.0%|✅|
|1443|🟢|Software engineer.|enter_data|enter_data|100.0%|✅|
|1444|🟢|my function is to serve butter|enter_data|enter_data|100.0%|✅|
|1445|🟢|oov|enter_data|enter_data|100.0%|✅|
|1446|🟢|host models|technical_question|technical_question|100.0%|✅|
|1447|🟢|multipass issue|technical_question|technical_question|100.0%|✅|
|1448|🟢|which UI channel is used by Rasa ?|faq/channels|faq/channels|100.0%|✅|
|1449|🟢|What is the magnitude of the community?|faq/community_size|faq/community_size|100.0%|✅|
|1450|🟢|how slots are filled|faq/slots|faq/slots|100.0%|✅|
|1451|🟢|I am a head of business intelligence|enter_data|enter_data|100.0%|✅|
|1452|🟢|My name is Sondra Boyd|enter_data|enter_data|100.0%|✅|
|1453|🟢|90k|enter_data|enter_data|100.0%|✅|
|1454|🟢|software engineer|enter_data|enter_data|100.0%|✅|
|1455|🟢|Can I have multiple .md data files?|technical_question|technical_question|100.0%|✅|
|1456|🟢|Pick a restaurant for me, please|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1457|🟢|What would be the name on my tombstone?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|1458|🟢|can you pls explain what rasa does|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|1459|🟢|gsaf|out_of_scope/other|out_of_scope/other|100.0%|✅|
|1460|🟢|What components does Rasa have?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|1461|🟢|what is the difference between rasa and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|1462|🟢|what language would rasa use|faq/languages|faq/languages|100.0%|✅|
|1463|🟢|can a voice bot be built using rasa?|faq/voice|faq/voice|100.0%|✅|
|1464|🟢|what is the Rasa forum used for|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1465|🟢|Yea|affirm|affirm|100.0%|✅|
|1466|🟢|what is the latest version of rasa?|technical_question|technical_question|100.0%|✅|
|1467|🟢|Hi the command rasa init doesn't do anything in windows|technical_question|technical_question|100.0%|✅|
|1468|🟢|How were you built?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|1469|🟢|help me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1470|🟢|What makes core and nlu incompatible?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|1471|🟢|Yup|affirm|affirm|100.0%|✅|
|1472|🟢|yess|affirm|affirm|100.0%|✅|
|1473|🟢|I work in innovation|enter_data|enter_data|100.0%|✅|
|1474|🟢|I'm in business|enter_data|enter_data|100.0%|✅|
|1475|🟢|25,000|enter_data|enter_data|100.0%|✅|
|1476|🟢|italian is the language of my bot|enter_data|enter_data|100.0%|✅|
|1477|🟢|i'm a product manager|enter_data|enter_data|100.0%|✅|
|1478|🟢|how to get the metadata file|technical_question|technical_question|100.0%|✅|
|1479|🟢|r u a human|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|1480|🟢|What languages do you know?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1481|🟢|what foreign languages do you know?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1482|🟢|what languages do you know?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1483|🟢|What's the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1484|🟢|what's the time|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1485|🟢|Can you explain me in one sentence what you are doing?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1486|🟢|so what can you do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1487|🟢|so what can you do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1488|🟢|what's the difference between rasa and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|1489|🟢|I want Vietnamese language processing|faq/languages|faq/languages|100.0%|✅|
|1490|🟢|What to do if I want to build a voice bot using rasa?|faq/voice|faq/voice|100.0%|✅|
|1491|🟢|I wrote it in chinese|enter_data|enter_data|100.0%|✅|
|1492|🟢|it’s available in chinese|enter_data|enter_data|100.0%|✅|
|1493|🟢|the assistant is in german|enter_data|enter_data|100.0%|✅|
|1494|🟢|Hello, Sara. How can I configure etnity extraction for russian lnguage?|technical_question|technical_question|100.0%|✅|
|1495|🟢|which technology is used to create you|technical_question|technical_question|100.0%|✅|
|1496|🟢|rasa templates|technical_question|technical_question|100.0%|✅|
|1497|🟢|For training data, to we need to exclusively write the file in MD format?|technical_question|technical_question|100.0%|✅|
|1498|🟢|can you tell me exactly how old you are?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|1499|🟢|wheather be like at your place?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1500|🟢|yap|affirm|affirm|100.0%|✅|
|1501|🟢|yes i agree|affirm|affirm|100.0%|✅|
|1502|🟢|I want to build a kick ass bot|enter_data|enter_data|100.0%|✅|
|1503|🟢|I'm a product manager|enter_data|enter_data|100.0%|✅|
|1504|🟢|chinese is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|1505|🟢|my email is Kelly@Coulter.net|enter_data|enter_data|100.0%|✅|
|1506|🟢|what is a synonym called?|technical_question|technical_question|100.0%|✅|
|1507|🟢|How've you been?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1508|🟢|How long have you been around?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|1509|🟢|Are you the bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1510|🟢|what is the whether today|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1511|🟢|What could be my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|1512|🟢|Rasa is good for messaging chanels|faq/channels|faq/channels|100.0%|✅|
|1513|🟢|how to build rasa with different languages?|faq/languages|faq/languages|100.0%|✅|
|1514|🟢|which version of python do i need|faq/python_version|faq/python_version|100.0%|✅|
|1515|🟢|i want to build a voice bot|faq/voice|faq/voice|100.0%|✅|
|1516|🟢|which are the topics covered in this forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1517|🟢|Ok|affirm|affirm|100.0%|✅|
|1518|🟢|Ok.|affirm|affirm|100.0%|✅|
|1519|🟢|oh super|affirm|affirm|100.0%|✅|
|1520|🟢|Im a full stack developer|enter_data|enter_data|100.0%|✅|
|1521|🟢|My name is Richard smith|enter_data|enter_data|100.0%|✅|
|1522|🟢|a sales bot|enter_data|enter_data|100.0%|✅|
|1523|🟢|how can I use transformers|technical_question|technical_question|100.0%|✅|
|1524|🟢|must i have to be a good programmer|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1525|🟢|Subscription price|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1526|🟢|Yes|affirm|affirm|100.0%|✅|
|1527|🟢|Yes.|affirm|affirm|100.0%|✅|
|1528|🟢|yea|affirm|affirm|100.0%|✅|
|1529|🟢|yessoo|affirm|affirm|100.0%|✅|
|1530|🟢|contact call with sales|contact_sales|contact_sales|100.0%|✅|
|1531|🟢|I am Robert Starks|enter_data|enter_data|100.0%|✅|
|1532|🟢|1 million|enter_data|enter_data|100.0%|✅|
|1533|🟢|2 million|enter_data|enter_data|100.0%|✅|
|1534|🟢|500 million|enter_data|enter_data|100.0%|✅|
|1535|🟢|it speaks portuguese|enter_data|enter_data|100.0%|✅|
|1536|🟢|How was your day?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1537|🟢|Tell me the time.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1538|🟢|tell me the time.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1539|🟢|what is the wather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1540|🟢|whats the temperature|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1541|🟢|Do I have a name? What is it?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|1542|🟢|I need some help|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1543|🟢|List the dissimilar qualities of core and nlu|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|1544|🟢|Is there API for any other programming languages?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1545|🟢|yop|affirm|affirm|100.0%|✅|
|1546|🟢|100k|enter_data|enter_data|100.0%|✅|
|1547|🟢|I work as a frontend dev|enter_data|enter_data|100.0%|✅|
|1548|🟢|My name is chelsea Parker|enter_data|enter_data|100.0%|✅|
|1549|🟢|so far it only speaks portuguese|enter_data|enter_data|100.0%|✅|
|1550|🟢|education bot|enter_data|enter_data|100.0%|✅|
|1551|🟢|my machine|enter_data|enter_data|100.0%|✅|
|1552|🟢|action_restart in rasa|technical_question|technical_question|100.0%|✅|
|1553|🟢|work with buttons?|technical_question|technical_question|100.0%|✅|
|1554|🟢|How do I get yes / no answer buttons|technical_question|technical_question|100.0%|✅|
|1555|🟢|hi how are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1556|🟢|May i know my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|1557|🟢|try rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|1558|🟢|what is the difference between rasa open source and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|1559|🟢|is there a tutorial?|faq/tutorials|faq/tutorials|100.0%|✅|
|1560|🟢|Is rasa any good for building a voice bot?|faq/voice|faq/voice|100.0%|✅|
|1561|🟢|What is the purpose of the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1562|🟢|what can I do in the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1563|🟢|yay|affirm|affirm|100.0%|✅|
|1564|🟢|yes it is|affirm|affirm|100.0%|✅|
|1565|🟢|google enginer|enter_data|enter_data|100.0%|✅|
|1566|🟢|my bot is in italian|enter_data|enter_data|100.0%|✅|
|1567|🟢|I have a problem|technical_question|technical_question|100.0%|✅|
|1568|🟢|I need help with a problem|technical_question|technical_question|100.0%|✅|
|1569|🟢|python sdk|technical_question|technical_question|100.0%|✅|
|1570|🟢|Should I run the 'rasa init' command in the anaconda prompt ?|technical_question|technical_question|100.0%|✅|
|1571|🟢|explain me what rasa is|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|1572|🟢|i havent understood yet what rasa actually is|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|1573|🟢|where's your home town?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1574|🟢|Is the Rasa Community large?|faq/community_size|faq/community_size|100.0%|✅|
|1575|🟢|Is the Rasa community large?|faq/community_size|faq/community_size|100.0%|✅|
|1576|🟢|must i have to be a good programmer to use RasA|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1577|🟢|Can one make a voice bot with rasa?|faq/voice|faq/voice|100.0%|✅|
|1578|🟢|what can be performed in the forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1579|🟢|yez|affirm|affirm|100.0%|✅|
|1580|🟢|it speaks spanish|enter_data|enter_data|100.0%|✅|
|1581|🟢|the assistant speaks german|enter_data|enter_data|100.0%|✅|
|1582|🟢|until now it’s only in german|enter_data|enter_data|100.0%|✅|
|1583|🟢|user can talk to my bot in french|enter_data|enter_data|100.0%|✅|
|1584|🟢|What is the difference between entities and slots?|technical_question|technical_question|100.0%|✅|
|1585|🟢|fallback|technical_question|technical_question|100.0%|✅|
|1586|🟢|implement buttons|technical_question|technical_question|100.0%|✅|
|1587|🟢|which messaging channels are compatible with rasa?|faq/channels|faq/channels|100.0%|✅|
|1588|🟢|Is there a tutorial for Rasa?|faq/tutorials|faq/tutorials|100.0%|✅|
|1589|🟢|ook|affirm|affirm|100.0%|✅|
|1590|🟢|can i makae rest calls|technical_question|technical_question|100.0%|✅|
|1591|🟢|How d I use a boolean slot|technical_question|technical_question|100.0%|✅|
|1592|🟢|how do i detect entities|technical_question|technical_question|100.0%|✅|
|1593|🟢|How did they build you?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|1594|🟢|How many years have you lived?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|1595|🟢|i am qq|out_of_scope/other|out_of_scope/other|100.0%|✅|
|1596|🟢|which messaging channels can be used with rasa?|faq/channels|faq/channels|100.0%|✅|
|1597|🟢|does rasa use open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1598|🟢|yes it was okay|affirm|affirm|100.0%|✅|
|1599|🟢|yesss|affirm|affirm|100.0%|✅|
|1600|🟢|it’s an chinese bot|enter_data|enter_data|100.0%|✅|
|1601|🟢|my name is Felicia Cosby|enter_data|enter_data|100.0%|✅|
|1602|🟢|our estimation is 10k|enter_data|enter_data|100.0%|✅|
|1603|🟢|My name is manuel|enter_data|enter_data|100.0%|✅|
|1604|🟢|How can i talk to RASA through the url|technical_question|technical_question|100.0%|✅|
|1605|🟢|fallback actions|technical_question|technical_question|100.0%|✅|
|1606|🟢|hello, how are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1607|🟢|can you tell me what number represents your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|1608|🟢|What communication channels does rasa support?|faq/channels|faq/channels|100.0%|✅|
|1609|🟢|what is the price of rasa|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1610|🟢|OK|affirm|affirm|100.0%|✅|
|1611|🟢|Whatever it costs|enter_data|enter_data|100.0%|✅|
|1612|🟢|10k|enter_data|enter_data|100.0%|✅|
|1613|🟢|are you artificial intelligence|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1614|🟢|cuz you are a bot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1615|🟢|what can I do with this bot|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1616|🟢|Is the community large?|faq/community_size|faq/community_size|100.0%|✅|
|1617|🟢|tell me the difference between rasa and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|1618|🟢|tell me difference between Rasa and Rasa X|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|1619|🟢|tell me about rasa enterpeise|faq/ee|faq/ee|100.0%|✅|
|1620|🟢|are you really free|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1621|🟢|are you really free?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1622|🟢|is it free|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1623|🟢|is it free?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1624|🟢|Can I use Rasa with Thai language|faq/languages|faq/languages|100.0%|✅|
|1625|🟢|okay|affirm|affirm|100.0%|✅|
|1626|🟢|okay..|affirm|affirm|100.0%|✅|
|1627|🟢|eisenkleber limited co kg|enter_data|enter_data|100.0%|✅|
|1628|🟢|the people speak spanish|enter_data|enter_data|100.0%|✅|
|1629|🟢|bash: poetry: command not found|technical_question|technical_question|100.0%|✅|
|1630|🟢|whats your birth year?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|1631|🟢|you robo|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1632|🟢|I need a new restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1633|🟢|try out the playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|1634|🟢|i am using rasa, why would i need rasa x?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|1635|🟢|Can i use python to program my bot?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1636|🟢|help mi with slots|faq/slots|faq/slots|100.0%|✅|
|1637|🟢|are there tutorials about rasa?|faq/tutorials|faq/tutorials|100.0%|✅|
|1638|🟢|well yes|affirm|affirm|100.0%|✅|
|1639|🟢|yaps|affirm|affirm|100.0%|✅|
|1640|🟢|I want a sales call|contact_sales|contact_sales|100.0%|✅|
|1641|🟢|i want a sales call|contact_sales|contact_sales|100.0%|✅|
|1642|🟢|it speaks french|enter_data|enter_data|100.0%|✅|
|1643|🟢|ok it's Hee@yahoo.com|enter_data|enter_data|100.0%|✅|
|1644|🟢|the people speak portuguese|enter_data|enter_data|100.0%|✅|
|1645|🟢|having trouble with rasa installation|technical_question|technical_question|100.0%|✅|
|1646|🟢|what is an intemt|technical_question|technical_question|100.0%|✅|
|1647|🟢|is this free?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1648|🟢|this is free?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1649|🟢|tell me about the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1650|🟢|accepted|affirm|affirm|100.0%|✅|
|1651|🟢|none|enter_data|enter_data|100.0%|✅|
|1652|🟢|i want a great bot to impress my boss|enter_data|enter_data|100.0%|✅|
|1653|🟢|im in marketing|enter_data|enter_data|100.0%|✅|
|1654|🟢|it's a tech company, apple|enter_data|enter_data|100.0%|✅|
|1655|🟢|hows the waether|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1656|🟢|What name do I go by?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|1657|🟢|Do I have to be a programmer to use rasa?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1658|🟢|Im looking for some tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|1659|🟢|How can I build my voice bot using rasa?|faq/voice|faq/voice|100.0%|✅|
|1660|🟢|portuguese|enter_data|enter_data|100.0%|✅|
|1661|🟢|don't have one|enter_data|enter_data|100.0%|✅|
|1662|🟢|How can i automate retraining of my rasa models|technical_question|technical_question|100.0%|✅|
|1663|🟢|testing chatbot|technical_question|technical_question|100.0%|✅|
|1664|🟢|would rasa be open source software?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1665|🟢|Tutorials for learning rasa ?|faq/tutorials|faq/tutorials|100.0%|✅|
|1666|🟢|yyeeeh|affirm|affirm|100.0%|✅|
|1667|🟢|tensorflow-text|technical_question|technical_question|100.0%|✅|
|1668|🟢|how r u|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1669|🟢|how r u ?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1670|🟢|how r u>|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1671|🟢|What's the closest restaurant open near me|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1672|🟢|help me find restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1673|🟢|What exactly is my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|1674|🟢|how can i integrate the rasa chat bot to my website|faq/channels|faq/channels|100.0%|✅|
|1675|🟢|are there some tutorials i could look at|faq/tutorials|faq/tutorials|100.0%|✅|
|1676|🟢|ja|affirm|affirm|100.0%|✅|
|1677|🟢|yes accept please|affirm|affirm|100.0%|✅|
|1678|🟢|$0.00|enter_data|enter_data|100.0%|✅|
|1679|🟢|10 m|enter_data|enter_data|100.0%|✅|
|1680|🟢|spanish|enter_data|enter_data|100.0%|✅|
|1681|🟢|embeddings|technical_question|technical_question|100.0%|✅|
|1682|🟢|sara, are you a robot or human?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|1683|🟢|What languages do you know how to use?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1684|🟢|what is time in US ?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1685|🟢|what is the enterprise edition|faq/ee|faq/ee|100.0%|✅|
|1686|🟢|what is price?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1687|🟢|where slots getting values|faq/slots|faq/slots|100.0%|✅|
|1688|🟢|yes baby|affirm|affirm|100.0%|✅|
|1689|🟢|contact sales for me|contact_sales|contact_sales|100.0%|✅|
|1690|🟢|software developer|enter_data|enter_data|100.0%|✅|
|1691|🟢|all the training data was in chinese|enter_data|enter_data|100.0%|✅|
|1692|🟢|i want to build an insurance bot|enter_data|enter_data|100.0%|✅|
|1693|🟢|what is fallback policy in rasa|technical_question|technical_question|100.0%|✅|
|1694|🟢|how are you doing today my sweet friend|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1695|🟢|I'm gonna need help finding a restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1696|🟢|what is rasa enterprise|faq/ee|faq/ee|100.0%|✅|
|1697|🟢|yesssss|affirm|affirm|100.0%|✅|
|1698|🟢|sales call|contact_sales|contact_sales|100.0%|✅|
|1699|🟢|I would like to build an ice cube dispenser bot|enter_data|enter_data|100.0%|✅|
|1700|🟢|Michele Perry|enter_data|enter_data|100.0%|✅|
|1701|🟢|chinese is the language of my bot|enter_data|enter_data|100.0%|✅|
|1702|🟢|my bot is in chinese|enter_data|enter_data|100.0%|✅|
|1703|🟢|slack|enter_data|enter_data|100.0%|✅|
|1704|🟢|how are u|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1705|🟢|how are u?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1706|🟢|oh are you chatbot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1707|🟢|what foreign languages are you fluent in?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1708|🟢|are there any other options?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1709|🟢|How small is the community?|faq/community_size|faq/community_size|100.0%|✅|
|1710|🟢|what can be done in the forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1711|🟢|whats the task of this forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1712|🟢|YES|affirm|affirm|100.0%|✅|
|1713|🟢|Yepp|affirm|affirm|100.0%|✅|
|1714|🟢|yes I do|affirm|affirm|100.0%|✅|
|1715|🟢|portuguese is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|1716|🟢|its an english bot|enter_data|enter_data|100.0%|✅|
|1717|🟢|php|technical_question|technical_question|100.0%|✅|
|1718|🟢|I need to find this restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1719|🟢|How do I do the programming?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1720|🟢|which programming languages does rasa supports?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1721|🟢|Can you built text bot with Japanese?|faq/languages|faq/languages|100.0%|✅|
|1722|🟢|chatbot language ?|faq/languages|faq/languages|100.0%|✅|
|1723|🟢|Is rasa open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1724|🟢|Is rasa open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1725|🟢|is rasa open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1726|🟢|is rasa open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1727|🟢|What are slots?|faq/slots|faq/slots|100.0%|✅|
|1728|🟢|slots are what ?|faq/slots|faq/slots|100.0%|✅|
|1729|🟢|what are slots|faq/slots|faq/slots|100.0%|✅|
|1730|🟢|what slots are?|faq/slots|faq/slots|100.0%|✅|
|1731|🟢|confirm|affirm|affirm|100.0%|✅|
|1732|🟢|call sales|contact_sales|contact_sales|100.0%|✅|
|1733|🟢|so far it only speaks german|enter_data|enter_data|100.0%|✅|
|1734|🟢|Do you have friends the same age as you, if so, how old are they?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|1735|🟢|How many candles were on your last birthday cake?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|1736|🟢|what languages you know?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1737|🟢|rasa enterprise plans|faq/ee|faq/ee|100.0%|✅|
|1738|🟢|my bot can be in italian?|faq/languages|faq/languages|100.0%|✅|
|1739|🟢|Is rasa a good fit for building a voice bot?|faq/voice|faq/voice|100.0%|✅|
|1740|🟢|ya go for it|affirm|affirm|100.0%|✅|
|1741|🟢|saler|enter_data|enter_data|100.0%|✅|
|1742|🟢|my name is John Evers|enter_data|enter_data|100.0%|✅|
|1743|🟢|problem solving|enter_data|enter_data|100.0%|✅|
|1744|🟢|the bot that helps you choose insurance for the car ;)|enter_data|enter_data|100.0%|✅|
|1745|🟢|how to evaluate model|technical_question|technical_question|100.0%|✅|
|1746|🟢|how is it going|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1747|🟢|Do you know the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1748|🟢|is it sunny|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1749|🟢|You were conceived in what location?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1750|🟢|more info about enterprise|faq/ee|faq/ee|100.0%|✅|
|1751|🟢|ya i want|affirm|affirm|100.0%|✅|
|1752|🟢|yes pleae|affirm|affirm|100.0%|✅|
|1753|🟢|I would like to have a call with sales team|contact_sales|contact_sales|100.0%|✅|
|1754|🟢|how about interactive learning|technical_question|technical_question|100.0%|✅|
|1755|🟢|I'd like to handle chitchat|technical_question|technical_question|100.0%|✅|
|1756|🟢|Yes I do|affirm|affirm|100.0%|✅|
|1757|🟢|I want to contact sales|contact_sales|contact_sales|100.0%|✅|
|1758|🟢|TypeError: 'module' object is not callable|technical_question|technical_question|100.0%|✅|
|1759|🟢|how to run sdk endpoint in background|technical_question|technical_question|100.0%|✅|
|1760|🟢|What languages are you fluent in?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1761|🟢|What languages can you use?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1762|🟢|From where did you come?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1763|🟢|What country are you from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1764|🟢|Where did you come from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1765|🟢|what country are you from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1766|🟢|where did you come from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1767|🟢|difference between rasa core and nlu|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|1768|🟢|language|faq/languages|faq/languages|100.0%|✅|
|1769|🟢|what is slots|faq/slots|faq/slots|100.0%|✅|
|1770|🟢|you have speech recognition?|faq/voice|faq/voice|100.0%|✅|
|1771|🟢|what is the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1772|🟢|ok|affirm|affirm|100.0%|✅|
|1773|🟢|ok...|affirm|affirm|100.0%|✅|
|1774|🟢|yes,i am|affirm|affirm|100.0%|✅|
|1775|🟢|ok..|affirm|affirm|100.0%|✅|
|1776|🟢|i want to have a call with sales|contact_sales|contact_sales|100.0%|✅|
|1777|🟢|I work for the AI research group of the turing centre of the UBC, Vancouver, Canada|enter_data|enter_data|100.0%|✅|
|1778|🟢|susi ai|enter_data|enter_data|100.0%|✅|
|1779|🟢|I'm interested in local installation|enter_data|enter_data|100.0%|✅|
|1780|🟢|Do you know how you were made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|1781|🟢|I need a restaurant.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1782|🟢|will you see any restaurant for me?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1783|🟢|How big is the community?|faq/community_size|faq/community_size|100.0%|✅|
|1784|🟢|Yep|affirm|affirm|100.0%|✅|
|1785|🟢|Yep!|affirm|affirm|100.0%|✅|
|1786|🟢|i agree|affirm|affirm|100.0%|✅|
|1787|🟢|yep|affirm|affirm|100.0%|✅|
|1788|🟢|yep. :/|affirm|affirm|100.0%|✅|
|1789|🟢|spanish is the language of my bot|enter_data|enter_data|100.0%|✅|
|1790|🟢|about 10 k|enter_data|enter_data|100.0%|✅|
|1791|🟢|big old bot|enter_data|enter_data|100.0%|✅|
|1792|🟢|boo|enter_data|enter_data|100.0%|✅|
|1793|🟢|Subscribe newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|1794|🟢|Can you help me with forms|technical_question|technical_question|100.0%|✅|
|1795|🟢|What channels of communication does rasa support?|faq/channels|faq/channels|100.0%|✅|
|1796|🟢|in which rasa version google hangouts chat available|faq/channels|faq/channels|100.0%|✅|
|1797|🟢|How big is the Rasa community|faq/community_size|faq/community_size|100.0%|✅|
|1798|🟢|How big is the Rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|1799|🟢|How massive is the Rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|1800|🟢|what is a Rasa forum for?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1801|🟢|yes go ahead|affirm|affirm|100.0%|✅|
|1802|🟢|a insurance tool that consults potential customers on the best life insurance to choose.|enter_data|enter_data|100.0%|✅|
|1803|🟢|are you having a good day|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1804|🟢|what is the difference between rasaand rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|1805|🟢|perfect|affirm|affirm|100.0%|✅|
|1806|🟢|si|affirm|affirm|100.0%|✅|
|1807|🟢|yes sirfr|affirm|affirm|100.0%|✅|
|1808|🟢|i'm a dev|enter_data|enter_data|100.0%|✅|
|1809|🟢|the language is portuguese|enter_data|enter_data|100.0%|✅|
|1810|🟢|Is it quite breezy outside?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1811|🟢|Voice bot|faq/voice|faq/voice|100.0%|✅|
|1812|🟢|yes|affirm|affirm|100.0%|✅|
|1813|🟢|yes ...|affirm|affirm|100.0%|✅|
|1814|🟢|yes'|affirm|affirm|100.0%|✅|
|1815|🟢|yes.|affirm|affirm|100.0%|✅|
|1816|🟢|i want to book a sales call|contact_sales|contact_sales|100.0%|✅|
|1817|🟢|sales contact|contact_sales|contact_sales|100.0%|✅|
|1818|🟢|How do I use ngrok with rasa x?|technical_question|technical_question|100.0%|✅|
|1819|🟢|actions|technical_question|technical_question|100.0%|✅|
|1820|🟢|okie|affirm|affirm|100.0%|✅|
|1821|🟢|i want to bookk a sales call|contact_sales|contact_sales|100.0%|✅|
|1822|🟢|i want to extract names|enter_data|enter_data|100.0%|✅|
|1823|🟢|tell me about intent classification|nlu_info|nlu_info|100.0%|✅|
|1824|🟢|training model?|technical_question|technical_question|100.0%|✅|
|1825|🟢|credentials|technical_question|technical_question|100.0%|✅|
|1826|🟢|What process was used to create you?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|1827|🟢|What is the definition of slots|faq/slots|faq/slots|100.0%|✅|
|1828|🟢|oui|affirm|affirm|100.0%|✅|
|1829|🟢|how easy is it to use rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|1830|🟢|jo|affirm|affirm|100.0%|✅|
|1831|🟢|yres|affirm|affirm|100.0%|✅|
|1832|🟢|where is rasa sdk?|technical_question|technical_question|100.0%|✅|
|1833|🟢|Will the skies be clear today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1834|🟢|again?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|1835|🟢|How do core and nlu conflict?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|1836|🟢|you have to be a good programmer|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1837|🟢|rasa tutorials|faq/tutorials|faq/tutorials|100.0%|✅|
|1838|🟢|can i programm a vocal assistant|faq/voice|faq/voice|100.0%|✅|
|1839|🟢|List the characteristics of rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1840|🟢|kk|affirm|affirm|100.0%|✅|
|1841|🟢|CSI|enter_data|enter_data|100.0%|✅|
|1842|🟢|Do you mind helping me install Rasa?|install_rasa|install_rasa|100.0%|✅|
|1843|🟢|Is it possible to integrate Rasa with Android to run on mobile devices|technical_question|technical_question|100.0%|✅|
|1844|🟢|I want to learn what rasa is|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|1845|🟢|Where do you come from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1846|🟢|where do you come from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1847|🟢|how to integrate u in my react application|faq/channels|faq/channels|100.0%|✅|
|1848|🟢|what are the messaging channels that can be used with rasa?|faq/channels|faq/channels|100.0%|✅|
|1849|🟢|i want to contact sales|contact_sales|contact_sales|100.0%|✅|
|1850|🟢|an ice cream bot|enter_data|enter_data|100.0%|✅|
|1851|🟢|i am self emplayed|enter_data|enter_data|100.0%|✅|
|1852|🟢|the bot speaks chinese|enter_data|enter_data|100.0%|✅|
|1853|🟢|we are a covert government organisation|enter_data|enter_data|100.0%|✅|
|1854|🟢|I'll subscribe to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|1855|🟢|hosting|technical_question|technical_question|100.0%|✅|
|1856|🟢|How exactly were you devised?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|1857|🟢|Do you have the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1858|🟢|do you have the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1859|🟢|weatger|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1860|🟢|Do I have a name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|1861|🟢|help please|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1862|🟢|what are the components of rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|1863|🟢|what are the components of RASA|faq/rasa_components|faq/rasa_components|100.0%|✅|
|1864|🟢|what are the components of Rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|1865|🟢|What are the components of Rasa?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|1866|🟢|What are the components of rasa?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|1867|🟢|what can I post in the forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1868|🟢|yes of course|affirm|affirm|100.0%|✅|
|1869|🟢|yes pls|affirm|affirm|100.0%|✅|
|1870|🟢|the assistant is in spanish|enter_data|enter_data|100.0%|✅|
|1871|🟢|any other tools to create chatbots?|technical_question|technical_question|100.0%|✅|
|1872|🟢|Do you have a python sdk?|technical_question|technical_question|100.0%|✅|
|1873|🟢|how can create multilingual chatbor|technical_question|technical_question|100.0%|✅|
|1874|🟢|what languages are you comfortable speaking at?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1875|🟢|Can you tell me the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1876|🟢|where are from|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1877|🟢|What exactly are slots?|faq/slots|faq/slots|100.0%|✅|
|1878|🟢|slots are what exactly?|faq/slots|faq/slots|100.0%|✅|
|1879|🟢|best tutorial for rasa|faq/tutorials|faq/tutorials|100.0%|✅|
|1880|🟢|I also want to book a sales call|contact_sales|contact_sales|100.0%|✅|
|1881|🟢|I want to contact the sales team|contact_sales|contact_sales|100.0%|✅|
|1882|🟢|10000000|enter_data|enter_data|100.0%|✅|
|1883|🟢|1000000|enter_data|enter_data|100.0%|✅|
|1884|🟢|100000|enter_data|enter_data|100.0%|✅|
|1885|🟢|120000|enter_data|enter_data|100.0%|✅|
|1886|🟢|200000000|enter_data|enter_data|100.0%|✅|
|1887|🟢|20000|enter_data|enter_data|100.0%|✅|
|1888|🟢|300000|enter_data|enter_data|100.0%|✅|
|1889|🟢|500000|enter_data|enter_data|100.0%|✅|
|1890|🟢|6000000|enter_data|enter_data|100.0%|✅|
|1891|🟢|driver|enter_data|enter_data|100.0%|✅|
|1892|🟢|i don't have one|enter_data|enter_data|100.0%|✅|
|1893|🟢|user can talk to my bot in italian|enter_data|enter_data|100.0%|✅|
|1894|🟢|How were you devised?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|1895|🟢|How are you men?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1896|🟢|What's up|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1897|🟢|what's up|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1898|🟢|what's up?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1899|🟢|Dumme sara|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|1900|🟢|which programming languages do you support?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1901|🟢|how do i get the open source rasa|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1902|🟢|what's the best tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|1903|🟢|is there an alexa integration|faq/voice|faq/voice|100.0%|✅|
|1904|🟢|jezz|affirm|affirm|100.0%|✅|
|1905|🟢|it’s in chinese|enter_data|enter_data|100.0%|✅|
|1906|🟢|how to visualise dialogue flow|technical_question|technical_question|100.0%|✅|
|1907|🟢|knowledge base action|technical_question|technical_question|100.0%|✅|
|1908|🟢|help|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1909|🟢|help?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1910|🟢|Deploy to a Server|technical_question|technical_question|100.0%|✅|
|1911|🟢|buttons|technical_question|technical_question|100.0%|✅|
|1912|🟢|what are you up to?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1913|🟢|How few members in the community?|faq/community_size|faq/community_size|100.0%|✅|
|1914|🟢|slots, what do youi mean?|faq/slots|faq/slots|100.0%|✅|
|1915|🟢|what slots are there?|faq/slots|faq/slots|100.0%|✅|
|1916|🟢|contact sales|contact_sales|contact_sales|100.0%|✅|
|1917|🟢|how to extract relationship|enter_data|enter_data|100.0%|✅|
|1918|🟢|language = mandarin|enter_data|enter_data|100.0%|✅|
|1919|🟢|language: mandarin|enter_data|enter_data|100.0%|✅|
|1920|🟢|contexual|enter_data|enter_data|100.0%|✅|
|1921|🟢|are you really a bbot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|1922|🟢|Nice day out today?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1923|🟢|how can i integrate rasa in my siteweb ?|faq/channels|faq/channels|100.0%|✅|
|1924|🟢|why should I join the forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1925|🟢|yeah|affirm|affirm|100.0%|✅|
|1926|🟢|yeah'=|affirm|affirm|100.0%|✅|
|1927|🟢|book sales call|contact_sales|contact_sales|100.0%|✅|
|1928|🟢|sdk|technical_question|technical_question|100.0%|✅|
|1929|🟢|my nlu cant detect entities|technical_question|technical_question|100.0%|✅|
|1930|🟢|I need to know what time it is.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1931|🟢|Can we expect any thunderstorms?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|1932|🟢|What is rasa doing exactly?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|1933|🟢|Do you know where you come from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|1934|🟢|Will it work for german|faq/languages|faq/languages|100.0%|✅|
|1935|🟢|How can i integrate voice in RASA CORE|faq/voice|faq/voice|100.0%|✅|
|1936|🟢|does rasa support voice input|faq/voice|faq/voice|100.0%|✅|
|1937|🟢|distances|enter_data|enter_data|100.0%|✅|
|1938|🟢|not sure yet, we plan with 50 thousand euro at the moment|enter_data|enter_data|100.0%|✅|
|1939|🟢|can I use Rasa with my Raspberry Pi|technical_question|technical_question|100.0%|✅|
|1940|🟢|Give me the time.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1941|🟢|tutorials|faq/tutorials|faq/tutorials|100.0%|✅|
|1942|🟢|let me contact sales|contact_sales|contact_sales|100.0%|✅|
|1943|🟢|I work in project management|enter_data|enter_data|100.0%|✅|
|1944|🟢|ceo|enter_data|enter_data|100.0%|✅|
|1945|🟢|what is the last version of rasa core?|technical_question|technical_question|100.0%|✅|
|1946|🟢|go back|out_of_scope/other|out_of_scope/other|100.0%|✅|
|1947|🟢|which programming language uses rasa?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1948|🟢|Give me a description of slots.|faq/slots|faq/slots|100.0%|✅|
|1949|🟢|booking sales call|contact_sales|contact_sales|100.0%|✅|
|1950|🟢|how are yuo|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1951|🟢|I want to know what rasa actually does that isn't clear to me yet|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|1952|🟢|i asked you if you can do anything else|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1953|🟢|what programming knowledge do I need to learn?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|1954|🟢|What's the slots?|faq/slots|faq/slots|100.0%|✅|
|1955|🟢|How are You?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1956|🟢|How are you|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1957|🟢|How are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1958|🟢|how are you|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1959|🟢|how are you ?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1960|🟢|how are you'|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1961|🟢|how are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1962|🟢|how are you????|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1963|🟢|where can i find some tutorials?|faq/tutorials|faq/tutorials|100.0%|✅|
|1964|🟢|so what exactly is the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|1965|🟢|yep i want that|affirm|affirm|100.0%|✅|
|1966|🟢|newsletter, here is my email: Marcus.Miller@yahoo.com|signup_newsletter|signup_newsletter|100.0%|✅|
|1967|🟢|what's pip|technical_question|technical_question|100.0%|✅|
|1968|🟢|what is action server|technical_question|technical_question|100.0%|✅|
|1969|🟢|de donde eres|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|1970|🟢|I agree|affirm|affirm|100.0%|✅|
|1971|🟢|yes go for it|affirm|affirm|100.0%|✅|
|1972|🟢|what is rasa cost ?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1973|🟢|how do slots work|faq/slots|faq/slots|100.0%|✅|
|1974|🟢|50 p|enter_data|enter_data|100.0%|✅|
|1975|🟢|rasa shell|technical_question|technical_question|100.0%|✅|
|1976|🟢|Can you tell the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|1977|🟢|do you have a nlu tutorial i can follow|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|1978|🟢|yep if i have to|affirm|affirm|100.0%|✅|
|1979|🟢|tell me how to start|how_to_get_started|how_to_get_started|100.0%|✅|
|1980|🟢|can i user rasa for my text classification problem?|technical_question|technical_question|100.0%|✅|
|1981|🟢|i'm looking for the youtube tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|1982|🟢|Rasa voice bot building.|faq/voice|faq/voice|100.0%|✅|
|1983|🟢|sort of|affirm|affirm|100.0%|✅|
|1984|🟢|have no idea|enter_data|enter_data|100.0%|✅|
|1985|🟢|i'm in sales|enter_data|enter_data|100.0%|✅|
|1986|🟢|IS there any near by restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1987|🟢|Does anyone know what slots are?|faq/slots|faq/slots|100.0%|✅|
|1988|🟢|how do i get started with rasa myself?|how_to_get_started|how_to_get_started|100.0%|✅|
|1989|🟢|hey how are you?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|1990|🟢|are u human|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|1991|🟢|Are you familiar with more than one language?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1992|🟢|what languages you can be comfortable speaking?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|1993|🟢|Do you seek me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|1994|🟢|what can you do, sara?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|1995|🟢|how much is Rasa stack?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|1996|🟢|You can tell me info on slots.|faq/slots|faq/slots|100.0%|✅|
|1997|🟢|ofcoure i do|affirm|affirm|100.0%|✅|
|1998|🟢|we think 4 million INR/ year|enter_data|enter_data|100.0%|✅|
|1999|🟢|Can I use Rasa for E-Mail|technical_question|technical_question|100.0%|✅|
|2000|🟢|so how were you made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2001|🟢|i want to contact sales support|contact_sales|contact_sales|100.0%|✅|
|2002|🟢|howareyou|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|2003|🟢|you sound like a real human|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|2004|🟢|I have a name, what is it?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2005|🟢|What is my full name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2006|🟢|what is rasa x enterprise|faq/ee|faq/ee|100.0%|✅|
|2007|🟢|Rasa can be programmed in python|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|2008|🟢|Oh yes|affirm|affirm|100.0%|✅|
|2009|🟢|please conda|enter_data|enter_data|100.0%|✅|
|2010|🟢|Accept|affirm|affirm|100.0%|✅|
|2011|🟢|the language is german|enter_data|enter_data|100.0%|✅|
|2012|🟢|there is no budget|enter_data|enter_data|100.0%|✅|
|2013|🟢|subscribe to our newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2014|🟢|can you help with some documentation|technical_question|technical_question|100.0%|✅|
|2015|🟢|how to build stories|technical_question|technical_question|100.0%|✅|
|2016|🟢|你好|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|2017|🟢|What communication channels are supported by rasa?|faq/channels|faq/channels|100.0%|✅|
|2018|🟢|what chat channels does rasa uses|faq/channels|faq/channels|100.0%|✅|
|2019|🟢|What is the price ?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2020|🟢|what is the price?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2021|🟢|what is the forum about|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|2022|🟢|around 200k|enter_data|enter_data|100.0%|✅|
|2023|🟢|how i deploy my bot on production server?|technical_question|technical_question|100.0%|✅|
|2024|🟢|RASA sdk|technical_question|technical_question|100.0%|✅|
|2025|🟢|Rara, are you a human?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|2026|🟢|How many in the community?|faq/community_size|faq/community_size|100.0%|✅|
|2027|🟢|how cost to install Rasa?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2028|🟢|rasa is the open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2029|🟢|yas|affirm|affirm|100.0%|✅|
|2030|🟢|I wanna build a super bot to send me cute animal pictures|enter_data|enter_data|100.0%|✅|
|2031|🟢|more|out_of_scope/other|out_of_scope/other|100.0%|✅|
|2032|🟢|How big is this community?|faq/community_size|faq/community_size|100.0%|✅|
|2033|🟢|what's the  difference between rasa nlu and rasa core|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|2034|🟢|which programming languages|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|2035|🟢|whats the cost of rasa|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2036|🟢|fine|affirm|affirm|100.0%|✅|
|2037|🟢|a good one?|enter_data|enter_data|100.0%|✅|
|2038|🟢|it speaks mandarin|enter_data|enter_data|100.0%|✅|
|2039|🟢|how do I install rasa in windows|install_rasa|install_rasa|100.0%|✅|
|2040|🟢|testing|technical_question|technical_question|100.0%|✅|
|2041|🟢|what's up sara|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|2042|🟢|Do you speak german?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2043|🟢|do you speak german?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2044|🟢|your cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2045|🟢|do you know what slots are?|faq/slots|faq/slots|100.0%|✅|
|2046|🟢|a sentient robot|enter_data|enter_data|100.0%|✅|
|2047|🟢|I'd like to know how you were put together?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2048|🟢|What is the rough size of the community?|faq/community_size|faq/community_size|100.0%|✅|
|2049|🟢|Definition of slots please.|faq/slots|faq/slots|100.0%|✅|
|2050|🟢|What is the meaning of the word slots?|faq/slots|faq/slots|100.0%|✅|
|2051|🟢|i'm a developer|enter_data|enter_data|100.0%|✅|
|2052|🟢|i'm a developer|enter_data|enter_data|100.0%|✅|
|2053|🟢|Beautiful day, isn't it?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|2054|🟢|What is my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2055|🟢|what is my name|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2056|🟢|what is my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2057|🟢|user can communicate with the bot in italian|enter_data|enter_data|100.0%|✅|
|2058|🟢|How were you made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2059|🟢|how were you made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2060|🟢|when is your birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|2061|🟢|Talk slots over with me.|faq/slots|faq/slots|100.0%|✅|
|2062|🟢|whats int he forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|2063|🟢|amazing!|affirm|affirm|100.0%|✅|
|2064|🟢|I'm a python developer|enter_data|enter_data|100.0%|✅|
|2065|🟢|spanish is the only language but I want to add more|enter_data|enter_data|100.0%|✅|
|2066|🟢|it is in chinese|enter_data|enter_data|100.0%|✅|
|2067|🟢|subscribe me to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2068|🟢|Does Rasa have the functionality of being able to set up the bot on web pages?|faq/channels|faq/channels|100.0%|✅|
|2069|🟢|ya please|affirm|affirm|100.0%|✅|
|2070|🟢|Weather?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|2071|🟢|weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|2072|🟢|weather?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|2073|🟢|What sets nlu apart from core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|2074|🟢|do i need to know how to program to create a bot?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|2075|🟢|When I use Rasa, Can I make bot speaking Japanese?|faq/languages|faq/languages|100.0%|✅|
|2076|🟢|I'm a developer|enter_data|enter_data|100.0%|✅|
|2077|🟢|its an spanish bot|enter_data|enter_data|100.0%|✅|
|2078|🟢|first lets sign up for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2079|🟢|how can i deploy my server on production?|technical_question|technical_question|100.0%|✅|
|2080|🟢|what is your exact age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|2081|🟢|The master of desaster|enter_data|enter_data|100.0%|✅|
|2082|🟢|Sign me up for the newsletter.|signup_newsletter|signup_newsletter|100.0%|✅|
|2083|🟢|subscribing to our newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2084|🟢|how many words can you handle?|technical_question|technical_question|100.0%|✅|
|2085|🟢|database rasa is using|technical_question|technical_question|100.0%|✅|
|2086|🟢|replace default nlu with custom component|technical_question|technical_question|100.0%|✅|
|2087|🟢|domain|technical_question|technical_question|100.0%|✅|
|2088|🟢|which python libraries are used|technical_question|technical_question|100.0%|✅|
|2089|🟢|are you a chatbot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|2090|🟢|Is rasa support message channels?|faq/channels|faq/channels|100.0%|✅|
|2091|🟢|ah ok|affirm|affirm|100.0%|✅|
|2092|🟢|i want to contact your sales team|contact_sales|contact_sales|100.0%|✅|
|2093|🟢|tell me about the nlu training data format|technical_question|technical_question|100.0%|✅|
|2094|🟢|are you artificial|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|2095|🟢|ok, I behave now|affirm|affirm|100.0%|✅|
|2096|🟢|I would like to book a sales call|contact_sales|contact_sales|100.0%|✅|
|2097|🟢|contact to sales|contact_sales|contact_sales|100.0%|✅|
|2098|🟢|i'd like to call Johnnie Essig|contact_sales|contact_sales|100.0%|✅|
|2099|🟢|subscribe to newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2100|🟢|Can you recommend a restaurant open right now|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|2101|🟢|Hot to get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2102|🟢|subscribe me to newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2103|🟢|oh cool|affirm|affirm|100.0%|✅|
|2104|🟢|sure|affirm|affirm|100.0%|✅|
|2105|🟢|sure!|affirm|affirm|100.0%|✅|
|2106|🟢|but I want a sales call|contact_sales|contact_sales|100.0%|✅|
|2107|🟢|it’s an german bot|enter_data|enter_data|100.0%|✅|
|2108|🟢|I want to build RASA DIET in google colab|technical_question|technical_question|100.0%|✅|
|2109|🟢|Tell me my name|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2110|🟢|Tell me my name.|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2111|🟢|what is rasa actually|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2112|🟢|what else can I do here?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2113|🟢|is the Rasa project open sourced?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2114|🟢|my laptop|enter_data|enter_data|100.0%|✅|
|2115|🟢|Tell me how to get started|how_to_get_started|how_to_get_started|100.0%|✅|
|2116|🟢|Tell me how to get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2117|🟢|subscribe to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2118|🟢|how to train model|technical_question|technical_question|100.0%|✅|
|2119|🟢|what is knowledge base|technical_question|technical_question|100.0%|✅|
|2120|🟢|are you happy|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|2121|🟢|hw r u?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|2122|🟢|Could you please give me a description of the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|2123|🟢|ok, Sara|affirm|affirm|100.0%|✅|
|2124|🟢|subscription newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2125|🟢|you are chatbot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|2126|🟢|Do you know any other languages?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2127|🟢|In which languages are you fluent?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2128|🟢|Do you know what my name is?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2129|🟢|Which version of Python to install?|faq/python_version|faq/python_version|100.0%|✅|
|2130|🟢|how to integrate speech to text in rasa|faq/voice|faq/voice|100.0%|✅|
|2131|🟢|let me talk to your sales people|contact_sales|contact_sales|100.0%|✅|
|2132|🟢|let me talk to your sales people!|contact_sales|contact_sales|100.0%|✅|
|2133|🟢|it’s in german|enter_data|enter_data|100.0%|✅|
|2134|🟢|user can communicate with the bot in portuguese|enter_data|enter_data|100.0%|✅|
|2135|🟢|lets do it|affirm|affirm|100.0%|✅|
|2136|🟢|yes i have!|affirm|affirm|100.0%|✅|
|2137|🟢|interactive learning?|technical_question|technical_question|100.0%|✅|
|2138|🟢|whats the time now|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|2139|🟢|Could you please explain the Rasa forum to me?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|2140|🟢|yes great|affirm|affirm|100.0%|✅|
|2141|🟢|actions on rasa|technical_question|technical_question|100.0%|✅|
|2142|🟢|dinner|out_of_scope/other|out_of_scope/other|100.0%|✅|
|2143|🟢|whar are the components of rasa?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2144|🟢|it speaks italian|enter_data|enter_data|100.0%|✅|
|2145|🟢|Hows it going|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|2146|🟢|Sure|affirm|affirm|100.0%|✅|
|2147|🟢|but please sign me up for the newsletter!|signup_newsletter|signup_newsletter|100.0%|✅|
|2148|🟢|conda throws some unexpected error|technical_question|technical_question|100.0%|✅|
|2149|🟢|which languages do you understand?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2150|🟢|yesyesyes|affirm|affirm|100.0%|✅|
|2151|🟢|What is your birthplace?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|2152|🟢|Nice|affirm|affirm|100.0%|✅|
|2153|🟢|fair enough|affirm|affirm|100.0%|✅|
|2154|🟢|i have none|enter_data|enter_data|100.0%|✅|
|2155|🟢|hw to get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2156|🟢|What can you demo|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2157|🟢|what is the Rasa forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|2158|🟢|What is my first name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2159|🟢|What city do you claim to for your birth?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|2160|🟢|Are you free?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2161|🟢|are you free ?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2162|🟢|slots can be described as ?|faq/slots|faq/slots|100.0%|✅|
|2163|🟢|How do you define the Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|2164|🟢|ok good|affirm|affirm|100.0%|✅|
|2165|🟢|in health care domain|enter_data|enter_data|100.0%|✅|
|2166|🟢|Please help me install Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|2167|🟢|i want to receive the newsletter emails|signup_newsletter|signup_newsletter|100.0%|✅|
|2168|🟢|lets try the newsletter signup|signup_newsletter|signup_newsletter|100.0%|✅|
|2169|🟢|agreed|affirm|affirm|100.0%|✅|
|2170|🟢|booking a sales call|contact_sales|contact_sales|100.0%|✅|
|2171|🟢|tell me, are you a bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|2172|🟢|Hi, can you give me the nearest fast food place?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|2173|🟢|How does nlu contrast to core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|2174|🟢|i ues chinese|enter_data|enter_data|100.0%|✅|
|2175|🟢|Create ecommerce bot|technical_question|technical_question|100.0%|✅|
|2176|🟢|RASA IS SOFTWARE?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2177|🟢|tell me about slots|faq/slots|faq/slots|100.0%|✅|
|2178|🟢|How exactly were you made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2179|🟢|hell yes|affirm|affirm|100.0%|✅|
|2180|🟢|yes please|affirm|affirm|100.0%|✅|
|2181|🟢|yes please!|affirm|affirm|100.0%|✅|
|2182|🟢|a sales call with Rufus Gardner would be nice|contact_sales|contact_sales|100.0%|✅|
|2183|🟢|what  are values of a boolean slot|technical_question|technical_question|100.0%|✅|
|2184|🟢|what is a custom action?|technical_question|technical_question|100.0%|✅|
|2185|🟢|What languages can you communicate in?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2186|🟢|book a sales call|contact_sales|contact_sales|100.0%|✅|
|2187|🟢|newsletter subscription|signup_newsletter|signup_newsletter|100.0%|✅|
|2188|🟢|i choose the call with sales|contact_sales|contact_sales|100.0%|✅|
|2189|🟢|I accept|affirm|affirm|100.0%|✅|
|2190|🟢|I accept.|affirm|affirm|100.0%|✅|
|2191|🟢|sales pl|contact_sales|contact_sales|100.0%|✅|
|2192|🟢|portuguese is the language of my bot|enter_data|enter_data|100.0%|✅|
|2193|🟢|register me for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2194|🟢|Where are your roots?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|2195|🟢|Do I need both Rasa and Rasa X?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|2196|🟢|Elise|enter_data|enter_data|100.0%|✅|
|2197|🟢|lets do the newsletter signup|signup_newsletter|signup_newsletter|100.0%|✅|
|2198|🟢|how to implement buttons|technical_question|technical_question|100.0%|✅|
|2199|🟢|credentials.yml|technical_question|technical_question|100.0%|✅|
|2200|🟢|you are bot or human?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|2201|🟢|you are human or bot|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|2202|🟢|i dont know the difference|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|2203|🟢|would an example of open source software be rasa?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2204|🟢|I dunno what a slot is|faq/slots|faq/slots|100.0%|✅|
|2205|🟢|I want to book a call with your sales team|contact_sales|contact_sales|100.0%|✅|
|2206|🟢|book call|contact_sales|contact_sales|100.0%|✅|
|2207|🟢|wassup>|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|2208|🟢|what are Rasa's components|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2209|🟢|What are Rasa's components?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2210|🟢|How many individuals are in your community?|faq/community_size|faq/community_size|100.0%|✅|
|2211|🟢|how mush does rasa cost|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2212|🟢|how to get started with|how_to_get_started|how_to_get_started|100.0%|✅|
|2213|🟢|please sign me up for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2214|🟢|subscribe to your newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2215|🟢|how to restart the rasa server|technical_question|technical_question|100.0%|✅|
|2216|🟢|which python do you support?|faq/python_version|faq/python_version|100.0%|✅|
|2217|🟢|yeeees|affirm|affirm|100.0%|✅|
|2218|🟢|subsribing to our newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2219|🟢|book a sale call|contact_sales|contact_sales|100.0%|✅|
|2220|🟢|yes cool|affirm|affirm|100.0%|✅|
|2221|🟢|yes, cool|affirm|affirm|100.0%|✅|
|2222|🟢|book a call|contact_sales|contact_sales|100.0%|✅|
|2223|🟢|IBM|enter_data|enter_data|100.0%|✅|
|2224|🟢|como estas|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|2225|🟢|what is this rasa playground thing. could you tell me more?|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|2226|🟢|i want some tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|2227|🟢|SURE|affirm|affirm|100.0%|✅|
|2228|🟢|request call with sales team|contact_sales|contact_sales|100.0%|✅|
|2229|🟢|microsoft|enter_data|enter_data|100.0%|✅|
|2230|🟢|you are a human|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|2231|🟢|are you a human ?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|2232|🟢|What can you do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2233|🟢|What can you do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2234|🟢|what can you do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2235|🟢|what can you do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2236|🟢|what you can do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2237|🟢|what you can do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2238|🟢|i would like to follow a core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|2239|🟢|Please tell me how to get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2240|🟢|how to install rasa on windows?|install_rasa|install_rasa|100.0%|✅|
|2241|🟢|tell me more about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2242|🟢|I am Hattie Rice|enter_data|enter_data|100.0%|✅|
|2243|🟢|can you give me prices ?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2244|🟢|done|affirm|affirm|100.0%|✅|
|2245|🟢|I want to sign up for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2246|🟢|I want to sign up for the newsletter.|signup_newsletter|signup_newsletter|100.0%|✅|
|2247|🟢|restaurants|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|2248|🟢|do you support french ?|faq/languages|faq/languages|100.0%|✅|
|2249|🟢|do rasa provide speech intent|faq/voice|faq/voice|100.0%|✅|
|2250|🟢|Are you a chat bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|2251|🟢|How does core compare to nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|2252|🟢|Can you tell me whats the price for rasa platform?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2253|🟢|i would like to follow a nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|2254|🟢|Yeah|affirm|affirm|100.0%|✅|
|2255|🟢|next the sales contact|contact_sales|contact_sales|100.0%|✅|
|2256|🟢|how do i get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2257|🟢|how can i install rasa|install_rasa|install_rasa|100.0%|✅|
|2258|🟢|How can you help me find a restaurant.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|2259|🟢|is rasa a studio?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|2260|🟢|ok fine|affirm|affirm|100.0%|✅|
|2261|🟢|Can you give me the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|2262|🟢|I'd like to know my name|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2263|🟢|What does core and nlu mean?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|2264|🟢|do I need programming experience to use rasa|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|2265|🟢|Is it a open source or any premium offer is available|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2266|🟢|yes, I'd love to|affirm|affirm|100.0%|✅|
|2267|🟢|yesh|affirm|affirm|100.0%|✅|
|2268|🟢|newsletter please my email is M_Moore@yahoo.com|signup_newsletter|signup_newsletter|100.0%|✅|
|2269|🟢|what infrastructure is required to run a bot?|technical_question|technical_question|100.0%|✅|
|2270|🟢|booking sales ca;;|contact_sales|contact_sales|100.0%|✅|
|2271|🟢|sign up for newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2272|🟢|how to integrate rasa chatbot with my website|faq/channels|faq/channels|100.0%|✅|
|2273|🟢|What is the number of people in this community?|faq/community_size|faq/community_size|100.0%|✅|
|2274|🟢|Help me to figure out the meaning of slots.|faq/slots|faq/slots|100.0%|✅|
|2275|🟢|Please define the word slots for me.|faq/slots|faq/slots|100.0%|✅|
|2276|🟢|I would love to subscribe to a newsletter!|signup_newsletter|signup_newsletter|100.0%|✅|
|2277|🟢|conda threw some weird error|technical_question|technical_question|100.0%|✅|
|2278|🟢|How to get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2279|🟢|How to get started with Rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|2280|🟢|Specify how you were created?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2281|🟢|Looks like a beautiful day hey?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|2282|🟢|What are my options|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2283|🟢|how to get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2284|🟢|how to get started with rasa ?|how_to_get_started|how_to_get_started|100.0%|✅|
|2285|🟢|let me call the sales team|contact_sales|contact_sales|100.0%|✅|
|2286|🟢|I wrote it in german|enter_data|enter_data|100.0%|✅|
|2287|🟢|its an italian bot|enter_data|enter_data|100.0%|✅|
|2288|🟢|Can you help me to install Rasa?|install_rasa|install_rasa|100.0%|✅|
|2289|🟢|So I'm here Today to ask one very simple question, what are you ?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|2290|🟢|Custom Connectors|faq/channels|faq/channels|100.0%|✅|
|2291|🟢|can someone help me with infos about the enterprise edition|faq/ee|faq/ee|100.0%|✅|
|2292|🟢|i prefer to get the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2293|🟢|Tell me how you were made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2294|🟢|Do you feel good?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|2295|🟢|Are you a human being?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|2296|🟢|Pardon me, but do you know the time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|2297|🟢|explain me what rasa does|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2298|🟢|all the training data was in german|enter_data|enter_data|100.0%|✅|
|2299|🟢|how cna i get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2300|🟢|how to get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2301|🟢|how to get started with Rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|2302|🟢|Do you speak italian?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2303|🟢|i need a help to integrate rasa with a messenger|faq/channels|faq/channels|100.0%|✅|
|2304|🟢|I would like to contact your sales team please|contact_sales|contact_sales|100.0%|✅|
|2305|🟢|talk to sales team|contact_sales|contact_sales|100.0%|✅|
|2306|🟢|We plan to build a sales bot to increase our sales by 500%.|enter_data|enter_data|100.0%|✅|
|2307|🟢|Dialogue Management please|enter_data|enter_data|100.0%|✅|
|2308|🟢|more info on components of rasa pls|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2309|🟢|i want to sign up for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2310|🟢|I want information about rasa x|faq/rasax|faq/rasax|100.0%|✅|
|2311|🟢|I want to use pip|enter_data|enter_data|100.0%|✅|
|2312|🟢|I wanna sign up for the newsletter.|signup_newsletter|signup_newsletter|100.0%|✅|
|2313|🟢|kiss me|out_of_scope/other|out_of_scope/other|100.0%|✅|
|2314|🟢|i'm a glibber and glitter salesman|enter_data|enter_data|100.0%|✅|
|2315|🟢|my name is Joseph Parson|enter_data|enter_data|100.0%|✅|
|2316|🟢|the bot speaks german|enter_data|enter_data|100.0%|✅|
|2317|🟢|Let me install Rasa Stack.|install_rasa|install_rasa|100.0%|✅|
|2318|🟢|How were you materialized?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2319|🟢|i want to integrate my rasa bot to webex  may i know how|faq/channels|faq/channels|100.0%|✅|
|2320|🟢|enterprise features|faq/ee|faq/ee|100.0%|✅|
|2321|🟢|hmmm sales|contact_sales|contact_sales|100.0%|✅|
|2322|🟢|let' contact sales now|contact_sales|contact_sales|100.0%|✅|
|2323|🟢|how to get started with rassa|how_to_get_started|how_to_get_started|100.0%|✅|
|2324|🟢|subscribe my email Evan@Palmer.net to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2325|🟢|sign up to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2326|🟢|What is the hour and minute right now?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|2327|🟢|tu pagal|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|2328|🟢|which programming language used for RASA.|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|2329|🟢|download the tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|2330|🟢|can you pelase subscribe me to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2331|🟢|Let me know how you were made exactly|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2332|🟢|tell me about the different parts of rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2333|🟢|Do you know how big the Rasa community is?|faq/community_size|faq/community_size|100.0%|✅|
|2334|🟢|0|enter_data|enter_data|100.0%|✅|
|2335|🟢|1000|enter_data|enter_data|100.0%|✅|
|2336|🟢|100|enter_data|enter_data|100.0%|✅|
|2337|🟢|10|enter_data|enter_data|100.0%|✅|
|2338|🟢|1231|enter_data|enter_data|100.0%|✅|
|2339|🟢|12|enter_data|enter_data|100.0%|✅|
|2340|🟢|3|enter_data|enter_data|100.0%|✅|
|2341|🟢|5000|enter_data|enter_data|100.0%|✅|
|2342|🟢|99|enter_data|enter_data|100.0%|✅|
|2343|🟢|how toget strated?|how_to_get_started|how_to_get_started|100.0%|✅|
|2344|🟢|tell me how i can get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2345|🟢|newsletter registration first|signup_newsletter|signup_newsletter|100.0%|✅|
|2346|🟢|on what channels can I use rasa|faq/channels|faq/channels|100.0%|✅|
|2347|🟢|fuck yeah!|affirm|affirm|100.0%|✅|
|2348|🟢|How do I get started with Rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|2349|🟢|okay sure|affirm|affirm|100.0%|✅|
|2350|🟢|But I wanted a sales call|contact_sales|contact_sales|100.0%|✅|
|2351|🟢|request sales call|contact_sales|contact_sales|100.0%|✅|
|2352|🟢|can you subscribe me to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2353|🟢|sign up newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2354|🟢|Can I die|out_of_scope/other|out_of_scope/other|100.0%|✅|
|2355|🟢|is it for free?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2356|🟢|ok sara|affirm|affirm|100.0%|✅|
|2357|🟢|let me talk to sales|contact_sales|contact_sales|100.0%|✅|
|2358|🟢|Bosch|enter_data|enter_data|100.0%|✅|
|2359|🟢|its an french bot|enter_data|enter_data|100.0%|✅|
|2360|🟢|what is the difference between slot and entity|technical_question|technical_question|100.0%|✅|
|2361|🟢|how to book a sales call|contact_sales|contact_sales|100.0%|✅|
|2362|🟢|how to book a sales call>|contact_sales|contact_sales|100.0%|✅|
|2363|🟢|how to book a sales call?|contact_sales|contact_sales|100.0%|✅|
|2364|🟢|how do I get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2365|🟢|Subscribe me to you newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2366|🟢|what is pip?|technical_question|technical_question|100.0%|✅|
|2367|🟢|In what manner were you built?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2368|🟢|In what way were you made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2369|🟢|in what way were you made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2370|🟢|I want to build a bot in Hindi|faq/languages|faq/languages|100.0%|✅|
|2371|🟢|Is the Rasa community medium?|faq/community_size|faq/community_size|100.0%|✅|
|2372|🟢|Michelle Vinion|enter_data|enter_data|100.0%|✅|
|2373|🟢|get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2374|🟢|let me have the call|contact_sales|contact_sales|100.0%|✅|
|2375|🟢|a turtle|enter_data|enter_data|100.0%|✅|
|2376|🟢|Please install Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|2377|🟢|how can I install RASA|install_rasa|install_rasa|100.0%|✅|
|2378|🟢|are you ai|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|2379|🟢|you are ai|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|2380|🟢|simple bpt|enter_data|enter_data|100.0%|✅|
|2381|🟢|Are you from around here?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|2382|🟢|are you from around here?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|2383|🟢|so... i trying to deploy my rasa bot on|faq/channels|faq/channels|100.0%|✅|
|2384|🟢|ok friend|affirm|affirm|100.0%|✅|
|2385|🟢|ok i accept|affirm|affirm|100.0%|✅|
|2386|🟢|have a call with the sales team|contact_sales|contact_sales|100.0%|✅|
|2387|🟢|what is the difference between rasa and rasax|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|2388|🟢|i want to chat to sales|contact_sales|contact_sales|100.0%|✅|
|2389|🟢|im a developer|enter_data|enter_data|100.0%|✅|
|2390|🟢|Have you seen me a restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|2391|🟢|Yes please|affirm|affirm|100.0%|✅|
|2392|🟢|Yes please!|affirm|affirm|100.0%|✅|
|2393|🟢|y|affirm|affirm|100.0%|✅|
|2394|🟢|yes that's great|affirm|affirm|100.0%|✅|
|2395|🟢|customer service automation bot|enter_data|enter_data|100.0%|✅|
|2396|🟢|get strarted with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2397|🟢|Subscribe me to the newsletter please!|signup_newsletter|signup_newsletter|100.0%|✅|
|2398|🟢|stories files|technical_question|technical_question|100.0%|✅|
|2399|🟢|By what means were you made?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2400|🟢|are u a real person?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|2401|🟢|what else do you know besides English?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2402|🟢|What is the difference between rasa nlu and rasa core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|2403|🟢|what is the difference between rasa nlu and rasa core|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|2404|🟢|what is the difference between rasa nlu and rasa core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|2405|🟢|i go for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2406|🟢|Can I use the rasa code for my own website?|faq/channels|faq/channels|100.0%|✅|
|2407|🟢|get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2408|🟢|Cars|out_of_scope/other|out_of_scope/other|100.0%|✅|
|2409|🟢|absolutely|affirm|affirm|100.0%|✅|
|2410|🟢|german is the language of my bot|enter_data|enter_data|100.0%|✅|
|2411|🟢|No, I mean how it is possible to use Skype as channel?|faq/channels|faq/channels|100.0%|✅|
|2412|🟢|yes you can|affirm|affirm|100.0%|✅|
|2413|🟢|Founder|enter_data|enter_data|100.0%|✅|
|2414|🟢|how do I get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2415|🟢|i also want to sign up for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2416|🟢|do you speak dutch?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2417|🟢|fcourse|affirm|affirm|100.0%|✅|
|2418|🟢|i want to contact sales now|contact_sales|contact_sales|100.0%|✅|
|2419|🟢|How does Rasa work?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2420|🟢|how does RASA work?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2421|🟢|how does rasa work|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2422|🟢|how does rasa work?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2423|🟢|show me comparison between rasa x and rasa|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|2424|🟢|sales department|contact_sales|contact_sales|100.0%|✅|
|2425|🟢|a killer bot|enter_data|enter_data|100.0%|✅|
|2426|🟢|how to get start with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2427|🟢|a chocolate bot|enter_data|enter_data|100.0%|✅|
|2428|🟢|How do I install Rasa Stack?|install_rasa|install_rasa|100.0%|✅|
|2429|🟢|what is in rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2430|🟢|Explain slots to me?|faq/slots|faq/slots|100.0%|✅|
|2431|🟢|yesyestyes|affirm|affirm|100.0%|✅|
|2432|🟢|can you connect me to sales|contact_sales|contact_sales|100.0%|✅|
|2433|🟢|server|enter_data|enter_data|100.0%|✅|
|2434|🟢|I would like to sign up for the newsletter.|signup_newsletter|signup_newsletter|100.0%|✅|
|2435|🟢|hey are you human|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|2436|🟢|What country were you born in?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|2437|🟢|Who ?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|2438|🟢|i want to be connected to your sales team|contact_sales|contact_sales|100.0%|✅|
|2439|🟢|my bot is in spanish|enter_data|enter_data|100.0%|✅|
|2440|🟢|we cant converse in french?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2441|🟢|How far does the Rasa community spread?|faq/community_size|faq/community_size|100.0%|✅|
|2442|🟢|yep, will do thank you|affirm|affirm|100.0%|✅|
|2443|🟢|i want to connect to your sales team|contact_sales|contact_sales|100.0%|✅|
|2444|🟢|how to get sarted|how_to_get_started|how_to_get_started|100.0%|✅|
|2445|🟢|docker is restarting|technical_question|technical_question|100.0%|✅|
|2446|🟢|install rasa stack|install_rasa|install_rasa|100.0%|✅|
|2447|🟢|what do I need to install Rasa|install_rasa|install_rasa|100.0%|✅|
|2448|🟢|NLW|out_of_scope/other|out_of_scope/other|100.0%|✅|
|2449|🟢|Oh, ok|affirm|affirm|100.0%|✅|
|2450|🟢|yep please|affirm|affirm|100.0%|✅|
|2451|🟢|ok, well, then a sales call with the fabulous Theodora Estrada|contact_sales|contact_sales|100.0%|✅|
|2452|🟢|come back|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2453|🟢|How many individuals reside in your community?|faq/community_size|faq/community_size|100.0%|✅|
|2454|🟢|rasa tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|2455|🟢|accept|affirm|affirm|100.0%|✅|
|2456|🟢|a bot to get a promotion|enter_data|enter_data|100.0%|✅|
|2457|🟢|tell me how to get started with core|how_to_get_started|how_to_get_started|100.0%|✅|
|2458|🟢|tell me your age number?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|2459|🟢|wow you sound like real human|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|2460|🟢|hi, can you help in understanding NLU|faq/nlu|faq/nlu|100.0%|✅|
|2461|🟢|What are slots used for?|faq/slots|faq/slots|100.0%|✅|
|2462|🟢|I am new|how_to_get_started|how_to_get_started|100.0%|✅|
|2463|🟢|how to learn RASA|how_to_get_started|how_to_get_started|100.0%|✅|
|2464|🟢|What is the name I was given?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2465|🟢|and what are slots|faq/slots|faq/slots|100.0%|✅|
|2466|🟢|and what are slots?|faq/slots|faq/slots|100.0%|✅|
|2467|🟢|intent classification - what is that?|nlu_info|nlu_info|100.0%|✅|
|2468|🟢|If I use Rasa, do I also need Rasa X?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|2469|🟢|please compare rasa and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|2470|🟢|how does intent classification work?|nlu_info|nlu_info|100.0%|✅|
|2471|🟢|install rasa x with or without rasa open source ?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|2472|🟢|please teach me|how_to_get_started|how_to_get_started|100.0%|✅|
|2473|🟢|Help me install Rasa|install_rasa|install_rasa|100.0%|✅|
|2474|🟢|how to get strated|how_to_get_started|how_to_get_started|100.0%|✅|
|2475|🟢|how to get strated?|how_to_get_started|how_to_get_started|100.0%|✅|
|2476|🟢|add me to the newsletter list|signup_newsletter|signup_newsletter|100.0%|✅|
|2477|🟢|what can you answer|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2478|🟢|whats the purpose of this forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|2479|🟢|A wolf bot|enter_data|enter_data|100.0%|✅|
|2480|🟢|my own|enter_data|enter_data|100.0%|✅|
|2481|🟢|ow to get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2482|🟢|do you cost anything?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2483|🟢|how t oget started|how_to_get_started|how_to_get_started|100.0%|✅|
|2484|🟢|newsletter pls|signup_newsletter|signup_newsletter|100.0%|✅|
|2485|🟢|could you elaborate more about rasa x|faq/rasax|faq/rasax|100.0%|✅|
|2486|🟢|TUTORIAL !!!!!!!!!!|faq/tutorials|faq/tutorials|100.0%|✅|
|2487|🟢|tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|2488|🟢|tutorial?|faq/tutorials|faq/tutorials|100.0%|✅|
|2489|🟢|a chatbot for our company|enter_data|enter_data|100.0%|✅|
|2490|🟢|user can communicate with the bot in german|enter_data|enter_data|100.0%|✅|
|2491|🟢|how to get started|how_to_get_started|how_to_get_started|100.0%|✅|
|2492|🟢|how to get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|2493|🟢|Subscribe to Rasa newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2494|🟢|newsletter - my email is Mabel@Brown.com|signup_newsletter|signup_newsletter|100.0%|✅|
|2495|🟢|what model do you use|technical_question|technical_question|100.0%|✅|
|2496|🟢|What are the requirements for connecting messaging channel to rasa?|faq/channels|faq/channels|100.0%|✅|
|2497|🟢|i accept|affirm|affirm|100.0%|✅|
|2498|🟢|could you elaborate more about rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|2499|🟢|an explanation of how entity recognition work would help|nlu_info|nlu_info|100.0%|✅|
|2500|🟢|i want to signup for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2501|🟢|What is the min requirements to run rasa|technical_question|technical_question|100.0%|✅|
|2502|🟢|wheather at you location?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|2503|🟢|is rasa open source needed for rasa x?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|2504|🟢|newsletter registration|signup_newsletter|signup_newsletter|100.0%|✅|
|2505|🟢|中文|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|2506|🟢|what about nlu?|faq/nlu|faq/nlu|100.0%|✅|
|2507|🟢|how do i get started|how_to_get_started|how_to_get_started|100.0%|✅|
|2508|🟢|how do i get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|2509|🟢|use of stories files|technical_question|technical_question|100.0%|✅|
|2510|🟢|i want to build all the bots|enter_data|enter_data|100.0%|✅|
|2511|🟢|the language is spanish|enter_data|enter_data|100.0%|✅|
|2512|🟢|how do I get started|how_to_get_started|how_to_get_started|100.0%|✅|
|2513|🟢|how do I get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|2514|🟢|i want to connect to sales|contact_sales|contact_sales|100.0%|✅|
|2515|🟢|how to setup rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2516|🟢|i am new to rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2517|🟢|i want to subsribe to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2518|🟢|Can you send messages based on events?|technical_question|technical_question|100.0%|✅|
|2519|🟢|are you a Skynet ?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|2520|🟢|i am new|how_to_get_started|how_to_get_started|100.0%|✅|
|2521|🟢|please subscribe me to the newsletter gregory_lilley@yahoo.com|signup_newsletter|signup_newsletter|100.0%|✅|
|2522|🟢|badass bot tester|enter_data|enter_data|100.0%|✅|
|2523|🟢|do i need to be able to program to use rasa?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|2524|🟢|How to get started|how_to_get_started|how_to_get_started|100.0%|✅|
|2525|🟢|How to get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|2526|🟢|I want to know if rasa works with duckling|nlu_info|nlu_info|100.0%|✅|
|2527|🟢|do you have docker image for rasa?|technical_question|technical_question|100.0%|✅|
|2528|🟢|how are the slots?|faq/slots|faq/slots|100.0%|✅|
|2529|🟢|is rasa opensource?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2530|🟢|docs|out_of_scope/other|out_of_scope/other|100.0%|✅|
|2531|🟢|relationship between rasa open source and rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|2532|🟢|sales team|contact_sales|contact_sales|100.0%|✅|
|2533|🟢|i am a new|how_to_get_started|how_to_get_started|100.0%|✅|
|2534|🟢|what is intent recognition?|nlu_info|nlu_info|100.0%|✅|
|2535|🟢|newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2536|🟢|sign me up for the rasa newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2537|🟢|when should i use rasa and when should i use rasa x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|2538|🟢|what about slots|faq/slots|faq/slots|100.0%|✅|
|2539|🟢|More a less|affirm|affirm|100.0%|✅|
|2540|🟢|call with sales team|contact_sales|contact_sales|100.0%|✅|
|2541|🟢|Do you have good weather?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|2542|🟢|i want to talk to sales|contact_sales|contact_sales|100.0%|✅|
|2543|🟢|I am searching the changlog|technical_question|technical_question|100.0%|✅|
|2544|🟢|i guess you are a chatbot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|2545|🟢|I want to talk to sales|contact_sales|contact_sales|100.0%|✅|
|2546|🟢|Newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2547|🟢|I guess so|affirm|affirm|100.0%|✅|
|2548|🟢|you are realy intelligent|react_positive|react_positive|100.0%|✅|
|2549|🟢|I'm going to install Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|2550|🟢|entity recognition|nlu_info|nlu_info|100.0%|✅|
|2551|🟢|newslettwr|signup_newsletter|signup_newsletter|100.0%|✅|
|2552|🟢|i want to connect your sales|contact_sales|contact_sales|100.0%|✅|
|2553|🟢|custom connection|faq/channels|faq/channels|100.0%|✅|
|2554|🟢|I'm a construction worker|enter_data|enter_data|100.0%|✅|
|2555|🟢|I am Aniket|enter_data|enter_data|100.0%|✅|
|2556|🟢|I want to subscribe to your newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2557|🟢|ja thats great|affirm|affirm|100.0%|✅|
|2558|🟢|How do I get started|how_to_get_started|how_to_get_started|100.0%|✅|
|2559|🟢|How do I get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|2560|🟢|i want to signup for the nl|signup_newsletter|signup_newsletter|100.0%|✅|
|2561|🟢|how do you retrieve previous messages|technical_question|technical_question|100.0%|✅|
|2562|🟢|which programming language can I use?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|2563|🟢|yeah do that|affirm|affirm|100.0%|✅|
|2564|🟢|iwant booking sales|contact_sales|contact_sales|100.0%|✅|
|2565|🟢|how do i set up a chatbot?|how_to_get_started|how_to_get_started|100.0%|✅|
|2566|🟢|cool! can I do something else here?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2567|🟢|tell me what is rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|2568|🟢|top|affirm|affirm|100.0%|✅|
|2569|🟢|Lol thats funny|react_positive|react_positive|100.0%|✅|
|2570|🟢|I want to build a lot of different bots|enter_data|enter_data|100.0%|✅|
|2571|🟢|I am new to Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2572|🟢|Please tell me how to get started|how_to_get_started|how_to_get_started|100.0%|✅|
|2573|🟢|Tell me more about Get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2574|🟢|I want to know more about tracker|technical_question|technical_question|100.0%|✅|
|2575|🟢|what languages you prefer more speaking at?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2576|🟢|get the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2577|🟢|do we need to write training data nlu.md|technical_question|technical_question|100.0%|✅|
|2578|🟢|tell me the slots?|faq/slots|faq/slots|100.0%|✅|
|2579|🟢|intent recognition|nlu_info|nlu_info|100.0%|✅|
|2580|🟢|can i talk to a sales representative|contact_sales|contact_sales|100.0%|✅|
|2581|🟢|user can talk to my bot in spanish|enter_data|enter_data|100.0%|✅|
|2582|🟢|what is the difference between you and LUIS|technical_question|technical_question|100.0%|✅|
|2583|🟢|How were you formed?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2584|🟢|i'd like to talk to sales|contact_sales|contact_sales|100.0%|✅|
|2585|🟢|the bot should help with HR stuff|enter_data|enter_data|100.0%|✅|
|2586|🟢|can rasa run standalone|technical_question|technical_question|100.0%|✅|
|2587|🟢|please explain what is dialogue management|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|2588|🟢|lets try the newsletter registration|signup_newsletter|signup_newsletter|100.0%|✅|
|2589|🟢|its okay|affirm|affirm|100.0%|✅|
|2590|🟢|ye|affirm|affirm|100.0%|✅|
|2591|🟢|how can i get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2592|🟢|hm intents?|nlu_info|nlu_info|100.0%|✅|
|2593|🟢|what is the weatehr|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|2594|🟢|oh good !!|affirm|affirm|100.0%|✅|
|2595|🟢|tell me about the components|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2596|🟢|How do i get started|how_to_get_started|how_to_get_started|100.0%|✅|
|2597|🟢|Can Rasa be incorporated into iOS apps?|technical_question|technical_question|100.0%|✅|
|2598|🟢|What name should I recognize for myself?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2599|🟢|I want to learn what rasa does|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2600|🟢|I'm a bot developer|enter_data|enter_data|100.0%|✅|
|2601|🟢|I'm a bot developer|enter_data|enter_data|100.0%|✅|
|2602|🟢|like 60 quid|enter_data|enter_data|100.0%|✅|
|2603|🟢|I want to integrate a database and look up values based on an entity the user gave me. How is this possible?|technical_question|technical_question|100.0%|✅|
|2604|🟢|In what manner were you formed?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2605|🟢|so what is this forum for?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|2606|🟢|Help me with finding this restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|2607|🟢|how to write stories to train rasa|technical_question|technical_question|100.0%|✅|
|2608|🟢|Where might you be from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|2609|🟢|how can i get started with Rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|2610|🟢|i need to talk to sales|contact_sales|contact_sales|100.0%|✅|
|2611|🟢|slots|faq/slots|faq/slots|100.0%|✅|
|2612|🟢|slots?|faq/slots|faq/slots|100.0%|✅|
|2613|🟢|please subscribe me to your newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2614|🟢|where can i fid tutorials for rasa|faq/tutorials|faq/tutorials|100.0%|✅|
|2615|🟢|i need the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2616|🟢|tell me about rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|2617|🟢|My name is Kenneth Sherman|enter_data|enter_data|100.0%|✅|
|2618|🟢|Is it raining|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|2619|🟢|Is it raining?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|2620|🟢|When are the events in Paris?|ask_which_events|ask_which_events|100.0%|✅|
|2621|🟢|how to start with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2622|🟢|how to start with rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|2623|🟢|can you explain to me how intent classification works?|nlu_info|nlu_info|100.0%|✅|
|2624|🟢|tell me about Rasa Playground please|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|2625|🟢|Did you know the size of rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|2626|🟢|do you have tutorials about nlu|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|2627|🟢|I still don’t get how intent classification works|nlu_info|nlu_info|100.0%|✅|
|2628|🟢|Entity recognition|nlu_info|nlu_info|100.0%|✅|
|2629|🟢|How can I visualise conversation flow?|technical_question|technical_question|100.0%|✅|
|2630|🟢|the components of Rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2631|🟢|the components of rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2632|🟢|The components of Rasa?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2633|🟢|I'd absolutely love that|affirm|affirm|100.0%|✅|
|2634|🟢|I want to talk to your sales people|contact_sales|contact_sales|100.0%|✅|
|2635|🟢|How to get started with Rasa core?|how_to_get_started|how_to_get_started|100.0%|✅|
|2636|🟢|pls explain how to get started|how_to_get_started|how_to_get_started|100.0%|✅|
|2637|🟢|what languages you are well versed ?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2638|🟢|i want to know what rasa does|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2639|🟢|what components of Rasa are open source|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2640|🟢|ok great|affirm|affirm|100.0%|✅|
|2641|🟢|italian|enter_data|enter_data|100.0%|✅|
|2642|🟢|how to install rasa in my system|install_rasa|install_rasa|100.0%|✅|
|2643|🟢|i just want to signup for your newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2644|🟢|Can I use Rasa X without using Rasa?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|2645|🟢|i want to subscribe to your newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2646|🟢|hep me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2647|🟢|find out how to get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2648|🟢|what number represents your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|2649|🟢|h r u ?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|2650|🟢|I'd like to know the meaning of slots|faq/slots|faq/slots|100.0%|✅|
|2651|🟢|When are the events in paris?|ask_which_events|ask_which_events|100.0%|✅|
|2652|🟢|can i get a ssales call|contact_sales|contact_sales|100.0%|✅|
|2653|🟢|help me get started|how_to_get_started|how_to_get_started|100.0%|✅|
|2654|🟢|what language do you use|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2655|🟢|Help me get started|how_to_get_started|how_to_get_started|100.0%|✅|
|2656|🟢|Where is the restaurant|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|2657|🟢|Michelle Garcia|enter_data|enter_data|100.0%|✅|
|2658|🟢|I need to install Rasa Core.|install_rasa|install_rasa|100.0%|✅|
|2659|🟢|I need to install Rasa|install_rasa|install_rasa|100.0%|✅|
|2660|🟢|health care|enter_data|enter_data|100.0%|✅|
|2661|🟢|Can you explain how you were created?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2662|🟢|could you inform me of the meaning of slots?|faq/slots|faq/slots|100.0%|✅|
|2663|🟢|i want to join the newsletter mails|signup_newsletter|signup_newsletter|100.0%|✅|
|2664|🟢|i want on this dope newsletter - my email is R_Grove@gmail.com|signup_newsletter|signup_newsletter|100.0%|✅|
|2665|🟢|Can you tell me about rasa x?|faq/rasax|faq/rasax|100.0%|✅|
|2666|🟢|how to get started with nlu|how_to_get_started|how_to_get_started|100.0%|✅|
|2667|🟢|Are we in for a scorcher?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|2668|🟢|it’s available in german|enter_data|enter_data|100.0%|✅|
|2669|🟢|How can I get started with rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|2670|🟢|Can you find me a burger joint?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|2671|🟢|What is your heritage?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|2672|🟢|it speaks chinese|enter_data|enter_data|100.0%|✅|
|2673|🟢|I need assistance in getting Rasa Stack.|install_rasa|install_rasa|100.0%|✅|
|2674|🟢|ok, i know i confused you there being a human! :)|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|2675|🟢|i would like a call with Mr Hughes|contact_sales|contact_sales|100.0%|✅|
|2676|🟢|whats tensorflow|technical_question|technical_question|100.0%|✅|
|2677|🟢|what are the components?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2678|🟢|What kinds of events are scheduled?|ask_which_events|ask_which_events|100.0%|✅|
|2679|🟢|a shitty bot|enter_data|enter_data|100.0%|✅|
|2680|🟢|id like to receive the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2681|🟢|sign me up for the newsletter - my email is Carolyn_Caskey@yahoo.com|signup_newsletter|signup_newsletter|100.0%|✅|
|2682|🟢|i want to signup for your newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2683|🟢|what are you, a bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|2684|🟢|Where from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|2685|🟢|what channels do you support?|faq/channels|faq/channels|100.0%|✅|
|2686|🟢|yep thats cool|affirm|affirm|100.0%|✅|
|2687|🟢|the intent|nlu_info|nlu_info|100.0%|✅|
|2688|🟢|Is there any restaurant?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|2689|🟢|show me restaurents|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|2690|🟢|HOW CAN I BOOK A SALES CALL ?|contact_sales|contact_sales|100.0%|✅|
|2691|🟢|does rasa work with duckling?|nlu_info|nlu_info|100.0%|✅|
|2692|🟢|Ar you a bot ?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|2693|🟢|rasa bot tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|2694|🟢|I book a bus ticket|enter_data|enter_data|100.0%|✅|
|2695|🟢|what is entity recognition?|nlu_info|nlu_info|100.0%|✅|
|2696|🟢|Whats your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|2697|🟢|whats your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|2698|🟢|I want to buy the rasa platform|contact_sales|contact_sales|100.0%|✅|
|2699|🟢|ConveRTFeaturizer|technical_question|technical_question|100.0%|✅|
|2700|🟢|How to install rasa stack|install_rasa|install_rasa|100.0%|✅|
|2701|🟢|Is the Rasa community small?|faq/community_size|faq/community_size|100.0%|✅|
|2702|🟢|i m new|how_to_get_started|how_to_get_started|100.0%|✅|
|2703|🟢|i'm new|how_to_get_started|how_to_get_started|100.0%|✅|
|2704|🟢|an explanation of how intent classification work would help|nlu_info|nlu_info|100.0%|✅|
|2705|🟢|eres humana|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|2706|🟢|i need a bot for customer service automation|enter_data|enter_data|100.0%|✅|
|2707|🟢|intents|nlu_info|nlu_info|100.0%|✅|
|2708|🟢|yeaaah lets go for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2709|🟢|How many languages do you know?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2710|🟢|how many languages do you know?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2711|🟢|Can you tell me my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2712|🟢|can you tell me my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2713|🟢|Can you tell me more about rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2714|🟢|How can I determine who I am?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|2715|🟢|How can I determine who am I?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|2716|🟢|what can I do in your community's forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|2717|🟢|i need a call from sales|contact_sales|contact_sales|100.0%|✅|
|2718|🟢|i'd like your newspaper please|signup_newsletter|signup_newsletter|100.0%|✅|
|2719|🟢|newsletter please|signup_newsletter|signup_newsletter|100.0%|✅|
|2720|🟢|I want to book a call|contact_sales|contact_sales|100.0%|✅|
|2721|🟢|WHAT IS RASA|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2722|🟢|What Is rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2723|🟢|What is Rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2724|🟢|What is rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2725|🟢|what is rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2726|🟢|what is rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2727|🟢|what is rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2728|🟢|what is rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2729|🟢|what is Rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2730|🟢|How can I get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2731|🟢|How can I get started with Rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|2732|🟢|I was looking for Duckling integration|nlu_info|nlu_info|100.0%|✅|
|2733|🟢|my bot is in german|enter_data|enter_data|100.0%|✅|
|2734|🟢|how to install rasa stack|install_rasa|install_rasa|100.0%|✅|
|2735|🟢|can i sign up to the newsletter too?|signup_newsletter|signup_newsletter|100.0%|✅|
|2736|🟢|i'm craving the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2737|🟢|i'm a solutions architect|enter_data|enter_data|100.0%|✅|
|2738|🟢|get newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2739|🟢|What was I named?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2740|🟢|What size is the Rasa community?|faq/community_size|faq/community_size|100.0%|✅|
|2741|🟢|what is duckling|nlu_info|nlu_info|100.0%|✅|
|2742|🟢|what is duckling?|nlu_info|nlu_info|100.0%|✅|
|2743|🟢|can you speak in italian?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2744|🟢|Whats the cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2745|🟢|newsletter it is|signup_newsletter|signup_newsletter|100.0%|✅|
|2746|🟢|connect me to your sales department|contact_sales|contact_sales|100.0%|✅|
|2747|🟢|Could you please tell me more about Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|2748|🟢|entity recognition - what is that?|nlu_info|nlu_info|100.0%|✅|
|2749|🟢|What language is the open source coding done in?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|2750|🟢|I'm new|how_to_get_started|how_to_get_started|100.0%|✅|
|2751|🟢|I want to learn about intent classification|nlu_info|nlu_info|100.0%|✅|
|2752|🟢|whatchya upto ?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|2753|🟢|i just want to signup for our newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2754|🟢|こにちは|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|2755|🟢|What Python version should I use?|faq/python_version|faq/python_version|100.0%|✅|
|2756|🟢|what python version should i use|faq/python_version|faq/python_version|100.0%|✅|
|2757|🟢|What types of events are planned?|ask_which_events|ask_which_events|100.0%|✅|
|2758|🟢|whatsapp|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|2759|🟢|Can you tell me about rasa playground?|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|2760|🟢|tell me how old you are?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|2761|🟢|yep that's nice|affirm|affirm|100.0%|✅|
|2762|🟢|let me talk sales|contact_sales|contact_sales|100.0%|✅|
|2763|🟢|how do i get started with NLU|how_to_get_started|how_to_get_started|100.0%|✅|
|2764|🟢|how do i get started with rasa nlu|how_to_get_started|how_to_get_started|100.0%|✅|
|2765|🟢|what is ur name|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|2766|🟢|Help me understand what slots are.|faq/slots|faq/slots|100.0%|✅|
|2767|🟢|why is Rasa useful|why_rasa|why_rasa|100.0%|✅|
|2768|🟢|ok i am new to Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2769|🟢|can you tell me prices|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2770|🟢|Where to run rasa init command ?|technical_question|technical_question|100.0%|✅|
|2771|🟢|an I use Rasa for e-mail applications|technical_question|technical_question|100.0%|✅|
|2772|🟢|Voice in Rasa|faq/voice|faq/voice|100.0%|✅|
|2773|🟢|how can i get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|2774|🟢|Please assist me with installing Rasa Stack.|install_rasa|install_rasa|100.0%|✅|
|2775|🟢|ja cool|affirm|affirm|100.0%|✅|
|2776|🟢|what are the names of all the events?|ask_which_events|ask_which_events|100.0%|✅|
|2777|🟢|what are intents ?|nlu_info|nlu_info|100.0%|✅|
|2778|🟢|what are intents?|nlu_info|nlu_info|100.0%|✅|
|2779|🟢|Hey, can you help me with locating this restaurant.|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|2780|🟢|ok.bye|bye|bye|100.0%|✅|
|2781|🟢|i need to be on the newsletter list|signup_newsletter|signup_newsletter|100.0%|✅|
|2782|🟢|now i want to signup for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2783|🟢|wer bist Du?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|2784|🟢|a cool boy|enter_data|enter_data|100.0%|✅|
|2785|🟢|i want to get the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2786|🟢|installation steps of rasa|install_rasa|install_rasa|100.0%|✅|
|2787|🟢|lets talk to sales|contact_sales|contact_sales|100.0%|✅|
|2788|🟢|how to get started with rasa nlu|how_to_get_started|how_to_get_started|100.0%|✅|
|2789|🟢|How did you come into being?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2790|🟢|what is components|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2791|🟢|yes give me information|affirm|affirm|100.0%|✅|
|2792|🟢|Can I have a call tomorrow at 3pm?|contact_sales|contact_sales|100.0%|✅|
|2793|🟢|When are the events for Paris?|ask_which_events|ask_which_events|100.0%|✅|
|2794|🟢|dialogue management please|enter_data|enter_data|100.0%|✅|
|2795|🟢|Just install Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|2796|🟢|how to add a database?|technical_question|technical_question|100.0%|✅|
|2797|🟢|what do you mean by slots?|faq/slots|faq/slots|100.0%|✅|
|2798|🟢|ok, I understood|affirm|affirm|100.0%|✅|
|2799|🟢|how do i get started with nlu|how_to_get_started|how_to_get_started|100.0%|✅|
|2800|🟢|explain about the rasa dialogue management|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|2801|🟢|how do i get startd?|how_to_get_started|how_to_get_started|100.0%|✅|
|2802|🟢|duckling|nlu_info|nlu_info|100.0%|✅|
|2803|🟢|Newsletter please.|signup_newsletter|signup_newsletter|100.0%|✅|
|2804|🟢|bye|bye|bye|100.0%|✅|
|2805|🟢|bye .|bye|bye|100.0%|✅|
|2806|🟢|bye!|bye|bye|100.0%|✅|
|2807|🟢|call|contact_sales|contact_sales|100.0%|✅|
|2808|🟢|What is your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|2809|🟢|what is your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|2810|🟢|sales|contact_sales|contact_sales|100.0%|✅|
|2811|🟢|intent classification|nlu_info|nlu_info|100.0%|✅|
|2812|🟢|bye bot|bye|bye|100.0%|✅|
|2813|🟢|i would love to get the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2814|🟢|how aold are you|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|2815|🟢|What state were you born in?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|2816|🟢|Do you know other languages?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2817|🟢|let me talk to your sales guys|contact_sales|contact_sales|100.0%|✅|
|2818|🟢|how can i setup rasa in django project ?|faq/channels|faq/channels|100.0%|✅|
|2819|🟢|Is rasa forum reliable?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|2820|🟢|do you have a large community|faq/community_size|faq/community_size|100.0%|✅|
|2821|🟢|When are the events for paris?|ask_which_events|ask_which_events|100.0%|✅|
|2822|🟢|how long to train|technical_question|technical_question|100.0%|✅|
|2823|🟢|What exactly is Rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2824|🟢|a voice bot|enter_data|enter_data|100.0%|✅|
|2825|🟢|what is intent classification?|nlu_info|nlu_info|100.0%|✅|
|2826|🟢|i love you|react_positive|react_positive|100.0%|✅|
|2827|🟢|having some problems with installation|install_rasa|install_rasa|100.0%|✅|
|2828|🟢|how to subdcribe?|signup_newsletter|signup_newsletter|100.0%|✅|
|2829|🟢|What do my colleagues call me?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2830|🟢|Sales|contact_sales|contact_sales|100.0%|✅|
|2831|🟢|does the open source version have core?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|2832|🟢|I want to build an FAQ bot|enter_data|enter_data|100.0%|✅|
|2833|🟢|I want to install Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|2834|🟢|I am hungry, find me some place to go|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|2835|🟢|sure thing|affirm|affirm|100.0%|✅|
|2836|🟢|hello sara, can you subscribe me to the newsletter?|signup_newsletter|signup_newsletter|100.0%|✅|
|2837|🟢|install Rasa on Mac|install_rasa|install_rasa|100.0%|✅|
|2838|🟢|subscribe Denise@gmail.com to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2839|🟢|what is componenbts|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2840|🟢|what are the features does rasa have?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2841|🟢|how to initialize a new project?|technical_question|technical_question|100.0%|✅|
|2842|🟢|tell me what is rasa x ee|faq/ee|faq/ee|100.0%|✅|
|2843|🟢|tell me about entity recognition|nlu_info|nlu_info|100.0%|✅|
|2844|🟢|how to use flask?|technical_question|technical_question|100.0%|✅|
|2845|🟢|are you real person or chat bot?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|2846|🟢|its an portuguese bot|enter_data|enter_data|100.0%|✅|
|2847|🟢|options|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2848|🟢|where can i get a tutorial on rasa|faq/tutorials|faq/tutorials|100.0%|✅|
|2849|🟢|How to install Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|2850|🟢|In what way were you created?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2851|🟢|How get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|2852|🟢|I'm fine and you|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|2853|🟢|whatsapp bro|technical_question|technical_question|100.0%|✅|
|2854|🟢|I need a expert opinion on slots.|faq/slots|faq/slots|100.0%|✅|
|2855|🟢|你是谁|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|2856|🟢|i want to get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2857|🟢|In which manner were you devised?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2858|🟢|please tell me more about rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|2859|🟢|what is default fall back|technical_question|technical_question|100.0%|✅|
|2860|🟢|tell me the difference between rasa and x|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|2861|🟢|is rasa available for node?|faq/languages|faq/languages|100.0%|✅|
|2862|🟢|oh actually i want to get the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2863|🟢|how can we keep buttons to get slots|faq/slots|faq/slots|100.0%|✅|
|2864|🟢|i want to buy the rasa platform|contact_sales|contact_sales|100.0%|✅|
|2865|🟢|i'm new to rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2866|🟢|What is COnvert?|technical_question|technical_question|100.0%|✅|
|2867|🟢|how's weather|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|2868|🟢|sign up for the NL|signup_newsletter|signup_newsletter|100.0%|✅|
|2869|🟢|obviously talk to your awesome sales team|contact_sales|contact_sales|100.0%|✅|
|2870|🟢|can i subscribe to news letter|signup_newsletter|signup_newsletter|100.0%|✅|
|2871|🟢|In what way were you formed?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2872|🟢|I want to speak binary with you|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|2873|🟢|is it a best practice to connect an external cms|technical_question|technical_question|100.0%|✅|
|2874|🟢|what is dialogue management|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|2875|🟢|What is dialogue management ?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|2876|🟢|I would like to book a call|contact_sales|contact_sales|100.0%|✅|
|2877|🟢|Im new|how_to_get_started|how_to_get_started|100.0%|✅|
|2878|🟢|ha ha|react_positive|react_positive|100.0%|✅|
|2879|🟢|how do you integrate duckling|nlu_info|nlu_info|100.0%|✅|
|2880|🟢|what do i need for programming?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|2881|🟢|how can i use rasa with alexa|faq/voice|faq/voice|100.0%|✅|
|2882|🟢|I am facing some issues with LMS|technical_question|technical_question|100.0%|✅|
|2883|🟢|i would like to know how to get started with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2884|🟢|i would like to talk to sales please|contact_sales|contact_sales|100.0%|✅|
|2885|🟢|I want to talk to your sales team|contact_sales|contact_sales|100.0%|✅|
|2886|🟢|In what way were you shaped?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|2887|🟢|i wanna build all the bots|enter_data|enter_data|100.0%|✅|
|2888|🟢|how to start with it|how_to_get_started|how_to_get_started|100.0%|✅|
|2889|🟢|hahaha|react_positive|react_positive|100.0%|✅|
|2890|🟢|so, how do I use rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|2891|🟢|Are Rasa and Rasa X the same thing?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|2892|🟢|can you explain me what intents are ?|nlu_info|nlu_info|100.0%|✅|
|2893|🟢|what's my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|2894|🟢|tudo bom|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|2895|🟢|Now?|out_of_scope/other|out_of_scope/other|100.0%|✅|
|2896|🟢|subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|2897|🟢|i have never programed before|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|2898|🟢|What's the size of the community?|faq/community_size|faq/community_size|100.0%|✅|
|2899|🟢|I'd like to install Rasa Core|install_rasa|install_rasa|100.0%|✅|
|2900|🟢|Where do you live?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|2901|🟢|where do you live|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|2902|🟢|where do you live?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|2903|🟢|is duckling part of rasa?|nlu_info|nlu_info|100.0%|✅|
|2904|🟢|What is the RASA Stack?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2905|🟢|Subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|2906|🟢|i want to subscribe to the newsletter with Joseph_Pyles@yahoo.com|signup_newsletter|signup_newsletter|100.0%|✅|
|2907|🟢|When is the next community event?|ask_which_events|ask_which_events|100.0%|✅|
|2908|🟢|how can I get started|how_to_get_started|how_to_get_started|100.0%|✅|
|2909|🟢|how can I get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|2910|🟢|I need to install Rasa NLU.|install_rasa|install_rasa|100.0%|✅|
|2911|🟢|components of Rasa?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2912|🟢|components of rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|2913|🟢|What are the events for Detroit?|ask_which_events|ask_which_events|100.0%|✅|
|2914|🟢|I do|affirm|affirm|100.0%|✅|
|2915|🟢|news|signup_newsletter|signup_newsletter|100.0%|✅|
|2916|🟢|do RASA has sdk to develop bot|technical_question|technical_question|100.0%|✅|
|2917|🟢|gimme the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2918|🟢|i am new but so how can i start|how_to_get_started|how_to_get_started|100.0%|✅|
|2919|🟢|i want to talk to a human|human_handoff|human_handoff|100.0%|✅|
|2920|🟢|i want to talk to a human \|human_handoff|human_handoff|100.0%|✅|
|2921|🟢|can i talk to your disagreeable sales man?|contact_sales|contact_sales|100.0%|✅|
|2922|🟢|i want to talk to human|human_handoff|human_handoff|100.0%|✅|
|2923|🟢|im a new to rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2924|🟢|intent classificaton|nlu_info|nlu_info|100.0%|✅|
|2925|🟢|request sales team|contact_sales|contact_sales|100.0%|✅|
|2926|🟢|i need this dope newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2927|🟢|tell me what time you have.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|2928|🟢|What's going on?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|2929|🟢|Rasa development in Java|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|2930|🟢|What does Rasa do?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2931|🟢|what does rasa do|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2932|🟢|what does rasa do ?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2933|🟢|what does rasa do?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2934|🟢|¿Qué pasa?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|2935|🟢|How you help me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2936|🟢|how you help me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2937|🟢|Bye|bye|bye|100.0%|✅|
|2938|🟢|may i receive the newsletter from now on|signup_newsletter|signup_newsletter|100.0%|✅|
|2939|🟢|subcribe|signup_newsletter|signup_newsletter|100.0%|✅|
|2940|🟢|I want to talk to a human|human_handoff|human_handoff|100.0%|✅|
|2941|🟢|what are the events for berlin?|ask_which_events|ask_which_events|100.0%|✅|
|2942|🟢|coolio|react_positive|react_positive|100.0%|✅|
|2943|🟢|hAHAHA|react_positive|react_positive|100.0%|✅|
|2944|🟢|cool beans|react_positive|react_positive|100.0%|✅|
|2945|🟢|I checked the documentation on intent classification but I still don’t understand it|nlu_info|nlu_info|100.0%|✅|
|2946|🟢|show me a tutorial?|faq/tutorials|faq/tutorials|100.0%|✅|
|2947|🟢|How can i launch a bot?|how_to_get_started|how_to_get_started|100.0%|✅|
|2948|🟢|what is Rasa Playground ?|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|2949|🟢|what is rasa playground ?|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|2950|🟢|you are my new bestfriend|react_positive|react_positive|100.0%|✅|
|2951|🟢|can you sign me up for the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2952|🟢|what can I do here|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2953|🟢|what can i do here|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|2954|🟢|booking a sall|contact_sales|contact_sales|100.0%|✅|
|2955|🟢|i want to learn more about Rasa X|faq/rasax|faq/rasax|100.0%|✅|
|2956|🟢|what are the difference?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|2957|🟢|whats the diference|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|2958|🟢|nl|signup_newsletter|signup_newsletter|100.0%|✅|
|2959|🟢|Can i use rasa without rasa x?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|2960|🟢|cost|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2961|🟢|cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2962|🟢|how to keep button system for slot selection|faq/slots|faq/slots|100.0%|✅|
|2963|🟢|I mean to say that I liked the explanation|react_positive|react_positive|100.0%|✅|
|2964|🟢|integrate rasa with ui|faq/channels|faq/channels|100.0%|✅|
|2965|🟢|I want the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2966|🟢|What are the events in Switzerland?|ask_which_events|ask_which_events|100.0%|✅|
|2967|🟢|send me the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|2968|🟢|give me the pricing|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|2969|🟢|i want to talk to a real person|human_handoff|human_handoff|100.0%|✅|
|2970|🟢|Installing Rasa Stack will be extremely helpful to me.|install_rasa|install_rasa|100.0%|✅|
|2971|🟢|channels supported by Rasa|faq/channels|faq/channels|100.0%|✅|
|2972|🟢|rasa enterprise|faq/ee|faq/ee|100.0%|✅|
|2973|🟢|I'm new to Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|2974|🟢|install Rasa NLU|install_rasa|install_rasa|100.0%|✅|
|2975|🟢|can you tell me your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|2976|🟢|need to use portuguese|faq/languages|faq/languages|100.0%|✅|
|2977|🟢|lets do this|affirm|affirm|100.0%|✅|
|2978|🟢|im lonely|enter_data|enter_data|100.0%|✅|
|2979|🟢|please connect me to sales|contact_sales|contact_sales|100.0%|✅|
|2980|🟢|can i talk to human|human_handoff|human_handoff|100.0%|✅|
|2981|🟢|Hoe do I install Rasa X|install_rasa|install_rasa|100.0%|✅|
|2982|🟢|it would be helpful to learn more about intent classification|nlu_info|nlu_info|100.0%|✅|
|2983|🟢|I love you|react_positive|react_positive|100.0%|✅|
|2984|🟢|bye bye bot|bye|bye|100.0%|✅|
|2985|🟢|which slots are there?|faq/slots|faq/slots|100.0%|✅|
|2986|🟢|what language do I need to program?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|2987|🟢|Lets start with the basics|how_to_get_started|how_to_get_started|100.0%|✅|
|2988|🟢|Is there any Rasa meetups?|ask_which_events|ask_which_events|100.0%|✅|
|2989|🟢|What's up man|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|2990|🟢|I am looking for tutorial on Rasa NLU|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|2991|🟢|OK can u brief me Abt rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|2992|🟢|I need to know about slot filling|faq/slots|faq/slots|100.0%|✅|
|2993|🟢|definitely yes without a doubt|affirm|affirm|100.0%|✅|
|2994|🟢|have a call|contact_sales|contact_sales|100.0%|✅|
|2995|🟢|ok bye|bye|bye|100.0%|✅|
|2996|🟢|ok, bye|bye|bye|100.0%|✅|
|2997|🟢|how can i get stared|how_to_get_started|how_to_get_started|100.0%|✅|
|2998|🟢|i want to join the newsletter list|signup_newsletter|signup_newsletter|100.0%|✅|
|2999|🟢|go for it|affirm|affirm|100.0%|✅|
|3000|🟢|What is your birthdate?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|3001|🟢|Is there any special in next community event?|ask_which_events|ask_which_events|100.0%|✅|
|3002|🟢|i'd like to get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|3003|🟢|I want to install Rasa Core|install_rasa|install_rasa|100.0%|✅|
|3004|🟢|I want to install rasa|install_rasa|install_rasa|100.0%|✅|
|3005|🟢|What year were you born?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|3006|🟢|what year were you born?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|3007|🟢|Hi there, are you the bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|3008|🟢|I want to know more about core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|3009|🟢|byee|bye|bye|100.0%|✅|
|3010|🟢|i want to speak to human|human_handoff|human_handoff|100.0%|✅|
|3011|🟢|tell me about Rasa X please|faq/rasax|faq/rasax|100.0%|✅|
|3012|🟢|I'm new to rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|3013|🟢|what python version do i install|faq/python_version|faq/python_version|100.0%|✅|
|3014|🟢|language = french|enter_data|enter_data|100.0%|✅|
|3015|🟢|language: french|enter_data|enter_data|100.0%|✅|
|3016|🟢|i want to speak to a real person|human_handoff|human_handoff|100.0%|✅|
|3017|🟢|go ahead|affirm|affirm|100.0%|✅|
|3018|🟢|i dont get what rasa is|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3019|🟢|In what ways are core and nlu unalike?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|3020|🟢|No, not really.|deny|deny|100.0%|✅|
|3021|🟢|more info on components|faq/rasa_components|faq/rasa_components|100.0%|✅|
|3022|🟢|what are the events?|ask_which_events|ask_which_events|100.0%|✅|
|3023|🟢|id like a call please|contact_sales|contact_sales|100.0%|✅|
|3024|🟢|let me talk to a human|human_handoff|human_handoff|100.0%|✅|
|3025|🟢|Please elaborate on the game of slots?|faq/slots|faq/slots|100.0%|✅|
|3026|🟢|i choose the call|contact_sales|contact_sales|100.0%|✅|
|3027|🟢|amounts of money|enter_data|enter_data|100.0%|✅|
|3028|🟢|呵呵|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|3029|🟢|you asked me a yes or no question, which i answered with yes|affirm|affirm|100.0%|✅|
|3030|🟢|lol|react_positive|react_positive|100.0%|✅|
|3031|🟢|I'd like to perform an installation of Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|3032|🟢|i am happy today|react_positive|react_positive|100.0%|✅|
|3033|🟢|can give tell me about components of Rosa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|3034|🟢|Hei|greet|greet|100.0%|✅|
|3035|🟢|you are awesome|react_positive|react_positive|100.0%|✅|
|3036|🟢|How can I get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|3037|🟢|I want to subscribing to the Rasa newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|3038|🟢|What are the prerequisites for installing RASA|how_to_get_started|how_to_get_started|100.0%|✅|
|3039|🟢|love you|react_positive|react_positive|100.0%|✅|
|3040|🟢|how do i start|how_to_get_started|how_to_get_started|100.0%|✅|
|3041|🟢|the people speak german|enter_data|enter_data|100.0%|✅|
|3042|🟢|it would be helpful to learn more about entity recognition|nlu_info|nlu_info|100.0%|✅|
|3043|🟢|can yiu send me a tutorial?|faq/tutorials|faq/tutorials|100.0%|✅|
|3044|🟢|i want to know about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3045|🟢|What are the events in Detroit?|ask_which_events|ask_which_events|100.0%|✅|
|3046|🟢|I wanna talk to your sales people.|contact_sales|contact_sales|100.0%|✅|
|3047|🟢|will there be an event in my city?|ask_which_events|ask_which_events|100.0%|✅|
|3048|🟢|what are the events in Berlin?|ask_which_events|ask_which_events|100.0%|✅|
|3049|🟢|how are you Rasa|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|3050|🟢|I want to know how to get started with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|3051|🟢|what are the events in berlin?|ask_which_events|ask_which_events|100.0%|✅|
|3052|🟢|sorry its ner|nlu_info|nlu_info|100.0%|✅|
|3053|🟢|Do you know about rasa supporting channels?|faq/channels|faq/channels|100.0%|✅|
|3054|🟢|bye bye|bye|bye|100.0%|✅|
|3055|🟢|dude, i want install rasa|install_rasa|install_rasa|100.0%|✅|
|3056|🟢|whatchcha doing|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|3057|🟢|whats goin on|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|3058|🟢|i want to install rasa|install_rasa|install_rasa|100.0%|✅|
|3059|🟢|Hi, I need the time.|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|3060|🟢|tell me more about rasa x EE|faq/ee|faq/ee|100.0%|✅|
|3061|🟢|How do I discover who I am?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|3062|🟢|How do I discover who am I?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|3063|🟢|卧槽|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|3064|🟢|you're a bot|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|3065|🟢|What can I ask you?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3066|🟢|what can I ask you?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3067|🟢|What are the events for New York?|ask_which_events|ask_which_events|100.0%|✅|
|3068|🟢|how to install sara in my server|install_rasa|install_rasa|100.0%|✅|
|3069|🟢|i want to about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3070|🟢|i need a core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|3071|🟢|how about the newsletter signup|signup_newsletter|signup_newsletter|100.0%|✅|
|3072|🟢|what else can i do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3073|🟢|what else can i do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3074|🟢|ya thats cool|affirm|affirm|100.0%|✅|
|3075|🟢|Hey|greet|greet|100.0%|✅|
|3076|🟢|Can i talk to a human?|human_handoff|human_handoff|100.0%|✅|
|3077|🟢|so what events are there?|ask_which_events|ask_which_events|100.0%|✅|
|3078|🟢|Its urgent for me to install Rasa.|install_rasa|install_rasa|100.0%|✅|
|3079|🟢|where can i find api documentation for rasa x|technical_question|technical_question|100.0%|✅|
|3080|🟢|are you a real person|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|3081|🟢|Are you a real person?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|3082|🟢|are you a real person?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|3083|🟢|what channels does rasa support|faq/channels|faq/channels|100.0%|✅|
|3084|🟢|What channels does Rasa support?|faq/channels|faq/channels|100.0%|✅|
|3085|🟢|Is rasa have more than 1000 members?|faq/community_size|faq/community_size|100.0%|✅|
|3086|🟢|i want to be part of the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|3087|🟢|yes.I.would.like.to.subscrbe|signup_newsletter|signup_newsletter|100.0%|✅|
|3088|🟢|NER|nlu_info|nlu_info|100.0%|✅|
|3089|🟢|i am looking for a nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|3090|🟢|add me to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|3091|🟢|Where can I find the definition of slots?|faq/slots|faq/slots|100.0%|✅|
|3092|🟢|interactive playground|enter_data|enter_data|100.0%|✅|
|3093|🟢|Great, is there anything else you can do, bot?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3094|🟢|how many languages are you fluent in?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|3095|🟢|byr|bye|bye|100.0%|✅|
|3096|🟢|How can I start with RASA on a legacy windows without Python?|how_to_get_started|how_to_get_started|100.0%|✅|
|3097|🟢|are you human|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|3098|🟢|Are you human?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|3099|🟢|Are you human ?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|3100|🟢|are you human ?|chitchat/ask_ishuman|chitchat/ask_ishuman|100.0%|✅|
|3101|🟢|what is your name|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|3102|🟢|what is your name?|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|3103|🟢|When do you celebrate your day of birth?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|3104|🟢|ofcourse|affirm|affirm|100.0%|✅|
|3105|🟢|how can you tell me what a slot is ?|faq/slots|faq/slots|100.0%|✅|
|3106|🟢|ya cool|affirm|affirm|100.0%|✅|
|3107|🟢|what kind of events are there?|ask_which_events|ask_which_events|100.0%|✅|
|3108|🟢|I have used it in the past|affirm|affirm|100.0%|✅|
|3109|🟢|Lol|react_positive|react_positive|100.0%|✅|
|3110|🟢|head of biz deve|enter_data|enter_data|100.0%|✅|
|3111|🟢|how i program the bot?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|3112|🟢|I am not able to restart action in some action|technical_question|technical_question|100.0%|✅|
|3113|🟢|LOL|react_positive|react_positive|100.0%|✅|
|3114|🟢|I want to talk to your sales guys|contact_sales|contact_sales|100.0%|✅|
|3115|🟢|it speaks german|enter_data|enter_data|100.0%|✅|
|3116|🟢|voice|faq/voice|faq/voice|100.0%|✅|
|3117|🟢|what's your name|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|3118|🟢|i would love to receive the rasa newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|3119|🟢|good bye|bye|bye|100.0%|✅|
|3120|🟢|What do you know about rasa meetups?|ask_which_events|ask_which_events|100.0%|✅|
|3121|🟢|subscribe Bruce_harryman@Olsen.com to the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|3122|🟢|it is cold|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|3123|🟢|elaborate on rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|3124|🟢|what is python version required?|faq/python_version|faq/python_version|100.0%|✅|
|3125|🟢|haha|react_positive|react_positive|100.0%|✅|
|3126|🟢|more info|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3127|🟢|can you tell all of the events?|ask_which_events|ask_which_events|100.0%|✅|
|3128|🟢|i am a new user|how_to_get_started|how_to_get_started|100.0%|✅|
|3129|🟢|can you help me get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|3130|🟢|i want a tutorial of rasa|faq/tutorials|faq/tutorials|100.0%|✅|
|3131|🟢|what is this rasa x thing. could you tell me more?|faq/rasax|faq/rasax|100.0%|✅|
|3132|🟢|alright|affirm|affirm|100.0%|✅|
|3133|🟢|ok i want to talk to your sales guys|contact_sales|contact_sales|100.0%|✅|
|3134|🟢|dialogueflow|enter_data|enter_data|100.0%|✅|
|3135|🟢|help me wih the installation|install_rasa|install_rasa|100.0%|✅|
|3136|🟢|you are a badass bot!|react_positive|react_positive|100.0%|✅|
|3137|🟢|i want to learn about nlu|faq/nlu|faq/nlu|100.0%|✅|
|3138|🟢|you seem pretty cool :D|react_positive|react_positive|100.0%|✅|
|3139|🟢|a slot is what|faq/slots|faq/slots|100.0%|✅|
|3140|🟢|what is a slot?|faq/slots|faq/slots|100.0%|✅|
|3141|🟢|ok Bye|bye|bye|100.0%|✅|
|3142|🟢|can rasa be used with alexa|faq/voice|faq/voice|100.0%|✅|
|3143|🟢|thats good|affirm|affirm|100.0%|✅|
|3144|🟢|so what exactly are these events?|ask_which_events|ask_which_events|100.0%|✅|
|3145|🟢|ok I'm actually an engineer|enter_data|enter_data|100.0%|✅|
|3146|🟢|new|how_to_get_started|how_to_get_started|100.0%|✅|
|3147|🟢|can I talk to human?|human_handoff|human_handoff|100.0%|✅|
|3148|🟢|can I talk to human|human_handoff|human_handoff|100.0%|✅|
|3149|🟢|is the sun out where you are?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|3150|🟢|how to set text slot without mentioned json|faq/slots|faq/slots|100.0%|✅|
|3151|🟢|can you show me a nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|3152|🟢|no, my frst time|deny|deny|100.0%|✅|
|3153|🟢|what events will there be?|ask_which_events|ask_which_events|100.0%|✅|
|3154|🟢|what sould i do to install rasa|install_rasa|install_rasa|100.0%|✅|
|3155|🟢|What are the differences?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|3156|🟢|what are the differences?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|3157|🟢|I don’t understand entity recognition|nlu_info|nlu_info|100.0%|✅|
|3158|🟢|What time have we got?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|3159|🟢|can u teach me|how_to_get_started|how_to_get_started|100.0%|✅|
|3160|🟢|Did you know about Rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|3161|🟢|What kinds of events do you host here?|ask_which_events|ask_which_events|100.0%|✅|
|3162|🟢|is there an event in Montreal|ask_which_events|ask_which_events|100.0%|✅|
|3163|🟢|install Rasa X|install_rasa|install_rasa|100.0%|✅|
|3164|🟢|i want the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|3165|🟢|Yes I am new|how_to_get_started|how_to_get_started|100.0%|✅|
|3166|🟢|i want newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|3167|🟢|what's rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|3168|🟢|Can I create a chat bot and set it up on a web page?|faq/channels|faq/channels|100.0%|✅|
|3169|🟢|You are great|react_positive|react_positive|100.0%|✅|
|3170|🟢|can you pint me to a good how-to online about Rasa|faq/tutorials|faq/tutorials|100.0%|✅|
|3171|🟢|how do i build a bot|how_to_get_started|how_to_get_started|100.0%|✅|
|3172|🟢|how do i build a bot?|how_to_get_started|how_to_get_started|100.0%|✅|
|3173|🟢|contact|contact_sales|contact_sales|100.0%|✅|
|3174|🟢|Ofcourse|affirm|affirm|100.0%|✅|
|3175|🟢|heeey|greet|greet|100.0%|✅|
|3176|🟢|install Rasa on Linux|install_rasa|install_rasa|100.0%|✅|
|3177|🟢|rasa-core error|technical_question|technical_question|100.0%|✅|
|3178|🟢|please provide information on your enterprise package|faq/ee|faq/ee|100.0%|✅|
|3179|🟢|I checked the documentation on entity recognition but I still don’t understand it|nlu_info|nlu_info|100.0%|✅|
|3180|🟢|I want know about Rasa Core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|3181|🟢|hey|greet|greet|100.0%|✅|
|3182|🟢|when will the next community event be?|ask_which_events|ask_which_events|100.0%|✅|
|3183|🟢|what's the difference?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|3184|🟢|HAHA|react_positive|react_positive|100.0%|✅|
|3185|🟢|please give me a human|human_handoff|human_handoff|100.0%|✅|
|3186|🟢|please send me the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|3187|🟢|you are great|react_positive|react_positive|100.0%|✅|
|3188|🟢|Heya|greet|greet|100.0%|✅|
|3189|🟢|Time?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|3190|🟢|sales please|contact_sales|contact_sales|100.0%|✅|
|3191|🟢|time|enter_data|chitchat/ask_time|100.0%|❌|
|3192|🟢|I don’t understand intent classification|nlu_info|nlu_info|100.0%|✅|
|3193|🟢|Heylo|greet|greet|100.0%|✅|
|3194|🟢|is rasa core able to run standalone?|technical_question|technical_question|100.0%|✅|
|3195|🟢|i am looking for a core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|3196|🟢|I also want to subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|3197|🟢|i would like to join the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|3198|🟢|is Rasa Playground separate from Rasa?|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|3199|🟢|of course|affirm|affirm|100.0%|✅|
|3200|🟢|wrong i want to speak to a human|human_handoff|human_handoff|100.0%|✅|
|3201|🟢|Hi|greet|greet|100.0%|✅|
|3202|🟢|Hi!|greet|greet|100.0%|✅|
|3203|🟢|Hi'|greet|greet|100.0%|✅|
|3204|🟢|Hi,|greet|greet|100.0%|✅|
|3205|🟢|what do you think slots are?|faq/slots|faq/slots|100.0%|✅|
|3206|🟢|I want to create chatbot using Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|3207|🟢|bye for now|bye|bye|100.0%|✅|
|3208|🟢|I have a few questions|need_help_broad|need_help_broad|100.0%|✅|
|3209|🟢|what are the events for China?|ask_which_events|ask_which_events|100.0%|✅|
|3210|🟢|When is the next event scheduled?|ask_which_events|ask_which_events|100.0%|✅|
|3211|🟢|core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|3212|🟢|any tutorials on using rasa?|faq/tutorials|faq/tutorials|100.0%|✅|
|3213|🟢|chào|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|3214|🟢|im a freelancer|enter_data|enter_data|100.0%|✅|
|3215|🟢|tell me about dialogue management|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|3216|🟢|how to use rasa caht in react application|faq/channels|faq/channels|100.0%|✅|
|3217|🟢|please send newsletter to Robert@yahoo.com|signup_newsletter|signup_newsletter|100.0%|✅|
|3218|🟢|Great information|react_positive|react_positive|100.0%|✅|
|3219|🟢|can i talk to a real person?|human_handoff|human_handoff|100.0%|✅|
|3220|🟢|yeah sure|affirm|affirm|100.0%|✅|
|3221|🟢|Is there an event in Montreal?|ask_which_events|ask_which_events|100.0%|✅|
|3222|🟢|intent|nlu_info|nlu_info|100.0%|✅|
|3223|🟢|i think I want to talk to your sales folks|contact_sales|contact_sales|100.0%|✅|
|3224|🟢|Rasa Playground|enter_data|enter_data|100.0%|✅|
|3225|🟢|how to programe rasa|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|3226|🟢|is there anything specific to be done in this forum|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|3227|🟢|tell me something you can do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3228|🟢|um what now|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3229|🟢|how do I install rasa?|install_rasa|install_rasa|100.0%|✅|
|3230|🟢|What do I do with slots?|faq/slots|faq/slots|100.0%|✅|
|3231|🟢|when is the next group event going to be?|ask_which_events|ask_which_events|100.0%|✅|
|3232|🟢|sounds good!|affirm|affirm|100.0%|✅|
|3233|🟢|can i please speak to a human?|human_handoff|human_handoff|100.0%|✅|
|3234|🟢|i want to build a health bot|enter_data|enter_data|100.0%|✅|
|3235|🟢|so what next?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3236|🟢|where did you spend your youth?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|3237|🟢|Which python version should I install to run Rasa example?|faq/python_version|faq/python_version|100.0%|✅|
|3238|🟢|i want ti booking about booking sales|contact_sales|contact_sales|100.0%|✅|
|3239|🟢|how this Rasa works|how_to_get_started|how_to_get_started|100.0%|✅|
|3240|🟢|how do I use rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|3241|🟢|How about hindi?|faq/languages|faq/languages|100.0%|✅|
|3242|🟢|please show me a core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|3243|🟢|bye udo|bye|bye|100.0%|✅|
|3244|🟢|how to start|how_to_get_started|how_to_get_started|100.0%|✅|
|3245|🟢|How to get starter?|how_to_get_started|how_to_get_started|100.0%|✅|
|3246|🟢|How many languages does Spacy support?|technical_question|technical_question|100.0%|✅|
|3247|🟢|which python?|faq/python_version|faq/python_version|100.0%|✅|
|3248|🟢|You live around here?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|3249|🟢|Help me install rasa x|install_rasa|install_rasa|100.0%|✅|
|3250|🟢|talk with a human|human_handoff|human_handoff|100.0%|✅|
|3251|🟢|i want to receive the newsletter from now on|signup_newsletter|signup_newsletter|100.0%|✅|
|3252|🟢|I have decided on Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|3253|🟢|What is on the calendar for this month?|ask_which_events|ask_which_events|100.0%|✅|
|3254|🟢|connect to the sales team|contact_sales|contact_sales|100.0%|✅|
|3255|🟢|are you rasa bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|3256|🟢|sorry tell me about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3257|🟢|real bot then?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|3258|🟢|What can rasa do?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3259|🟢|hi what is your name?|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|3260|🟢|I have a question|need_help_broad|need_help_broad|100.0%|✅|
|3261|🟢|I have a question.|need_help_broad|need_help_broad|100.0%|✅|
|3262|🟢|I have a question?|need_help_broad|need_help_broad|100.0%|✅|
|3263|🟢|you are cool man|react_positive|react_positive|100.0%|✅|
|3264|🟢|Please tell me how I can start?|how_to_get_started|how_to_get_started|100.0%|✅|
|3265|🟢|how do I install Rasa|install_rasa|install_rasa|100.0%|✅|
|3266|🟢|i don't want either of those|deny|deny|100.0%|✅|
|3267|🟢|request a call|contact_sales|contact_sales|100.0%|✅|
|3268|🟢|yes, give me information, please|affirm|affirm|100.0%|✅|
|3269|🟢|thats funny|react_positive|react_positive|100.0%|✅|
|3270|🟢|I need Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|3271|🟢|I need Rasa Stack.|install_rasa|install_rasa|100.0%|✅|
|3272|🟢|i want to call|contact_sales|contact_sales|100.0%|✅|
|3273|🟢|k|affirm|affirm|100.0%|✅|
|3274|🟢|Can I talk to a human|human_handoff|human_handoff|100.0%|✅|
|3275|🟢|What area are you from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|3276|🟢|how rasa works ?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3277|🟢|how works rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3278|🟢|i want subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|3279|🟢|no go|deny|deny|100.0%|✅|
|3280|🟢|Is next community event held in 2019?|ask_which_events|ask_which_events|100.0%|✅|
|3281|🟢|Where were you at before you were here?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|3282|🟢|HEY|greet|greet|100.0%|✅|
|3283|🟢|Where is next community event held?|ask_which_events|ask_which_events|100.0%|✅|
|3284|🟢|I want info on installing Rasa|install_rasa|install_rasa|100.0%|✅|
|3285|🟢|I'd like to install Rasa NLU|install_rasa|install_rasa|100.0%|✅|
|3286|🟢|can i speak to human|human_handoff|human_handoff|100.0%|✅|
|3287|🟢|You originated through what means?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|3288|🟢|I want an offer for your platform|contact_sales|contact_sales|100.0%|✅|
|3289|🟢|i wanna get started|how_to_get_started|how_to_get_started|100.0%|✅|
|3290|🟢|Tell me about rasa x|faq/rasax|faq/rasax|100.0%|✅|
|3291|🟢|php code|technical_question|technical_question|100.0%|✅|
|3292|🟢|Neither|deny|deny|100.0%|✅|
|3293|🟢|When is it scheduled the next community event?|ask_which_events|ask_which_events|100.0%|✅|
|3294|🟢|book a sales|contact_sales|contact_sales|100.0%|✅|
|3295|🟢|how long|enter_data|enter_data|100.0%|✅|
|3296|🟢|can i install on may mac|technical_question|technical_question|100.0%|✅|
|3297|🟢|i would like to subscribe to your newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|3298|🟢|rasa enterprise please|faq/ee|faq/ee|100.0%|✅|
|3299|🟢|What else do people call me?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|3300|🟢|If there is an upcoming event when is it?|ask_which_events|ask_which_events|100.0%|✅|
|3301|🟢|What are the events now?|ask_which_events|ask_which_events|100.0%|✅|
|3302|🟢|yow are you|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|3303|🟢|hey ther|greet|greet|100.0%|✅|
|3304|🟢|can you explain to me how entity recognition works?|nlu_info|nlu_info|100.0%|✅|
|3305|🟢|Say my name.|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|3306|🟢|considering|affirm|affirm|100.0%|✅|
|3307|🟢|bye :P|bye|bye|100.0%|✅|
|3308|🟢|no thank you|deny|deny|100.0%|✅|
|3309|🟢|no, thank you|deny|deny|100.0%|✅|
|3310|🟢|intent please|nlu_info|nlu_info|100.0%|✅|
|3311|🟢|Tell me when the next community event is happening;|ask_which_events|ask_which_events|100.0%|✅|
|3312|🟢|can i speak to a human|human_handoff|human_handoff|100.0%|✅|
|3313|🟢|ok cool|affirm|affirm|100.0%|✅|
|3314|🟢|so now what|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3315|🟢|What kinds of events are happening here?|ask_which_events|ask_which_events|100.0%|✅|
|3316|🟢|I want to do a Rasa Stack installation|install_rasa|install_rasa|100.0%|✅|
|3317|🟢|i need to download rasa|install_rasa|install_rasa|100.0%|✅|
|3318|🟢|I want to learn more about the pricing|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|3319|🟢|nope|deny|deny|100.0%|✅|
|3320|🟢|nope!|deny|deny|100.0%|✅|
|3321|🟢|What kinds of events are on your schedule?|ask_which_events|ask_which_events|100.0%|✅|
|3322|🟢|sign me up for that newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|3323|🟢|tell me your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|3324|🟢|no way|deny|deny|100.0%|✅|
|3325|🟢|Hi there|greet|greet|100.0%|✅|
|3326|🟢|i need a rasa nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|3327|🟢|goodnight|bye|bye|100.0%|✅|
|3328|🟢|i want to talk to a person|human_handoff|human_handoff|100.0%|✅|
|3329|🟢|tensorflow 1.10.0 has requirement numpy<=1.14.5,>=1.13.3, but you'll have numpy 1.16.0 which is incompatible.|technical_question|technical_question|100.0%|✅|
|3330|🟢|a great one|enter_data|enter_data|100.0%|✅|
|3331|🟢|how to build assistant with rasa?|how_to_get_started|how_to_get_started|100.0%|✅|
|3332|🟢|What is the Similarities between core and nlu?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|3333|🟢|i want to  suscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|3334|🟢|can i run rasa on my computer?|install_rasa|install_rasa|100.0%|✅|
|3335|🟢|which are the slots?|faq/slots|faq/slots|100.0%|✅|
|3336|🟢|how does entity recognition work?|nlu_info|nlu_info|100.0%|✅|
|3337|🟢|what is rasaplayground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|3338|🟢|What is the next event for paris?|ask_which_events|ask_which_events|100.0%|✅|
|3339|🟢|Can you tell me what I am called?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|3340|🟢|Hey is there a tutorial on how to train an intent cassification model in Python_|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|3341|🟢|i want to learn something about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3342|🟢|Which events do you have?|ask_which_events|ask_which_events|100.0%|✅|
|3343|🟢|technical question|technical_question|technical_question|100.0%|✅|
|3344|🟢|please tell me more about rasa x|faq/rasax|faq/rasax|100.0%|✅|
|3345|🟢|you are doin great|react_positive|react_positive|100.0%|✅|
|3346|🟢|Give me more information about Rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3347|🟢|I'm using it|affirm|affirm|100.0%|✅|
|3348|🟢|Hola|greet|greet|100.0%|✅|
|3349|🟢|describe the word slot please|faq/slots|faq/slots|100.0%|✅|
|3350|🟢|why should I switch to rasa?|why_rasa|why_rasa|100.0%|✅|
|3351|🟢|please show me a nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|3352|🟢|never mind|deny|deny|100.0%|✅|
|3353|🟢|hell yeah|affirm|affirm|100.0%|✅|
|3354|🟢|tell me some languages you know?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|3355|🟢|heya|greet|greet|100.0%|✅|
|3356|🟢|response selector?|technical_question|technical_question|100.0%|✅|
|3357|🟢|hey bot|greet|greet|100.0%|✅|
|3358|🟢|hey bot!|greet|greet|100.0%|✅|
|3359|🟢|how do i build a chatbot?|how_to_get_started|how_to_get_started|100.0%|✅|
|3360|🟢|I want information about rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|3361|🟢|Hello|greet|greet|100.0%|✅|
|3362|🟢|Hello!|greet|greet|100.0%|✅|
|3363|🟢|What is the next event in san francisco?|ask_which_events|ask_which_events|100.0%|✅|
|3364|🟢|i got error while installing rasa|need_help_broad|need_help_broad|100.0%|✅|
|3365|🟢|sign me up, my email is Elizabeth@yahoo.com|contact_sales|contact_sales|100.0%|✅|
|3366|🟢|when is the next event?|ask_which_events|ask_which_events|100.0%|✅|
|3367|🟢|can you add Edward@Paul.com to the newsletter list?|signup_newsletter|signup_newsletter|100.0%|✅|
|3368|🟢|i cannot find tutorial for rasa|faq/tutorials|faq/tutorials|100.0%|✅|
|3369|🟢|What do I call myself?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|3370|🟢|hey hey|greet|greet|100.0%|✅|
|3371|🟢|I require Rasa Stack?|install_rasa|install_rasa|100.0%|✅|
|3372|🟢|what's your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|3373|🟢|What's your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|3374|🟢|i want to learn about rasa core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|3375|🟢|In Rasa, what are slots used for?|faq/slots|faq/slots|100.0%|✅|
|3376|🟢|what's the purpose of Rasa Playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|3377|🟢|you are so smart|react_positive|react_positive|100.0%|✅|
|3378|🟢|request call|contact_sales|contact_sales|100.0%|✅|
|3379|🟢|what community events are there?|ask_which_events|ask_which_events|100.0%|✅|
|3380|🟢|ça va ?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|3381|🟢|您好|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|3382|🟢|Ok let's start|affirm|affirm|100.0%|✅|
|3383|🟢|language = chinese|enter_data|enter_data|100.0%|✅|
|3384|🟢|language: chinese|enter_data|enter_data|100.0%|✅|
|3385|🟢|cr|out_of_scope/other|out_of_scope/other|100.0%|✅|
|3386|🟢|I bet you can tell me all about slots.|faq/slots|faq/slots|100.0%|✅|
|3387|🟢|HI|greet|greet|100.0%|✅|
|3388|🟢|Did you have an tutorial.|faq/tutorials|faq/tutorials|100.0%|✅|
|3389|🟢|how to build a bot|how_to_get_started|how_to_get_started|100.0%|✅|
|3390|🟢|how to build a bot?|how_to_get_started|how_to_get_started|100.0%|✅|
|3391|🟢|tell me what is rasa x|faq/rasax|faq/rasax|100.0%|✅|
|3392|🟢|When is the next user group meetup|ask_which_events|ask_which_events|100.0%|✅|
|3393|🟢|heyho|greet|greet|100.0%|✅|
|3394|🟢|I want to talk with sales about our project|contact_sales|contact_sales|100.0%|✅|
|3395|🟢|ok quick question here do i download this api|technical_question|technical_question|100.0%|✅|
|3396|🟢|At which date the next community event will take place?|ask_which_events|ask_which_events|100.0%|✅|
|3397|🟢|i want a tutorial on core|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|3398|🟢|I'm getting Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|3399|🟢|why is rasa a good nlp libarary|why_rasa|why_rasa|100.0%|✅|
|3400|🟢|Hey bot|greet|greet|100.0%|✅|
|3401|🟢|Which community events do you have|ask_which_events|ask_which_events|100.0%|✅|
|3402|🟢|Are u developed in rasa|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|3403|🟢|more about nlu|faq/nlu|faq/nlu|100.0%|✅|
|3404|🟢|no I dont want|deny|deny|100.0%|✅|
|3405|🟢|Rasa Stack is what I will be installing|install_rasa|install_rasa|100.0%|✅|
|3406|🟢|i need a tutorial on how to use rasa core|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|3407|🟢|what can I ask ?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3408|🟢|tell me about nlu|faq/nlu|faq/nlu|100.0%|✅|
|3409|🟢|Does Rasa host any events?|ask_which_events|ask_which_events|100.0%|✅|
|3410|🟢|hi|greet|greet|100.0%|✅|
|3411|🟢|hi !|greet|greet|100.0%|✅|
|3412|🟢|hi!|greet|greet|100.0%|✅|
|3413|🟢|hi.........................................................|greet|greet|100.0%|✅|
|3414|🟢|hi?|greet|greet|100.0%|✅|
|3415|🟢|what kind of events will be held?|ask_which_events|ask_which_events|100.0%|✅|
|3416|🟢|umm|out_of_scope/other|out_of_scope/other|100.0%|✅|
|3417|🟢|yes i have built a bot before|affirm|affirm|100.0%|✅|
|3418|🟢|crappy joke|react_negative|react_negative|100.0%|✅|
|3419|🟢|What kinds of events are on your calendar?|ask_which_events|ask_which_events|100.0%|✅|
|3420|🟢|hello I have a question|need_help_broad|need_help_broad|100.0%|✅|
|3421|🟢|no, thankyou|deny|deny|100.0%|✅|
|3422|🟢|I'd like to subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|3423|🟢|that is funny|react_positive|react_positive|100.0%|✅|
|3424|🟢|What does everyone call me?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|3425|🟢|ye splease|affirm|affirm|100.0%|✅|
|3426|🟢|when will the community event take place?|ask_which_events|ask_which_events|100.0%|✅|
|3427|🟢|where to intents?|nlu_info|nlu_info|100.0%|✅|
|3428|🟢|What is your origin?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|3429|🟢|user can talk to my bot in german|enter_data|enter_data|100.0%|✅|
|3430|🟢|tensorflow|technical_question|technical_question|100.0%|✅|
|3431|🟢|no thanks|deny|deny|100.0%|✅|
|3432|🟢|no, thanks|deny|deny|100.0%|✅|
|3433|🟢|Are you built using rasa?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|3434|🟢|Where are you located?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|3435|🟢|it's 500000000|enter_data|enter_data|100.0%|✅|
|3436|🟢|then bye|bye|bye|100.0%|✅|
|3437|🟢|hi there|greet|greet|100.0%|✅|
|3438|🟢|NEIN|deny|deny|100.0%|✅|
|3439|🟢|add me as your subscriber|signup_newsletter|signup_newsletter|100.0%|✅|
|3440|🟢|How to start using Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|3441|🟢|how can I learn rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|3442|🟢|customer service automation|enter_data|enter_data|100.0%|✅|
|3443|🟢|let me speak to a real person|human_handoff|human_handoff|100.0%|✅|
|3444|🟢|i need a nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|3445|🟢|hell9o|greet|greet|100.0%|✅|
|3446|🟢|Hello Bot|greet|greet|100.0%|✅|
|3447|🟢|how do i learn rasa core|how_to_get_started|how_to_get_started|100.0%|✅|
|3448|🟢|Bye bye|bye|bye|100.0%|✅|
|3449|🟢|Can you communicate in any other languages?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|3450|🟢|no sir|deny|deny|100.0%|✅|
|3451|🟢|you are funny|react_positive|react_positive|100.0%|✅|
|3452|🟢|Do you know my name?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|3453|🟢|i am facing a particular error,could u help me?|need_help_broad|need_help_broad|100.0%|✅|
|3454|🟢|how do i install rasa?|install_rasa|install_rasa|100.0%|✅|
|3455|🟢|happy|react_positive|react_positive|100.0%|✅|
|3456|🟢|You're cute.|react_positive|react_positive|100.0%|✅|
|3457|🟢|let me talk to a real person|human_handoff|human_handoff|100.0%|✅|
|3458|🟢|Tell me about rasa playgrounds|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|3459|🟢|where should i start from|how_to_get_started|how_to_get_started|100.0%|✅|
|3460|🟢|can you tell me how to build a bot?|how_to_get_started|how_to_get_started|100.0%|✅|
|3461|🟢|How do I build a bot|how_to_get_started|how_to_get_started|100.0%|✅|
|3462|🟢|helo|greet|greet|100.0%|✅|
|3463|🟢|what date is the next community event?|ask_which_events|ask_which_events|100.0%|✅|
|3464|🟢|no i can't|deny|deny|100.0%|✅|
|3465|🟢|i have errors in installaition|need_help_broad|need_help_broad|100.0%|✅|
|3466|🟢|how does dialogue management work?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|3467|🟢|book an appointment|contact_sales|contact_sales|100.0%|✅|
|3468|🟢|How did they make you?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|3469|🟢|How many different languages are you fluent in?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|3470|🟢|what are you ding|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3471|🟢|no, i hate it|deny|deny|100.0%|✅|
|3472|🟢|When is it planned the next event in Montreal?|ask_which_events|ask_which_events|100.0%|✅|
|3473|🟢|i want to be in touch with sales|contact_sales|contact_sales|100.0%|✅|
|3474|🟢|what time do you have?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|3475|🟢|im a dev|enter_data|enter_data|100.0%|✅|
|3476|🟢|talk to me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3477|🟢|talk to me!|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3478|🟢|i want to know more about NLU|faq/nlu|faq/nlu|100.0%|✅|
|3479|🟢|I want to know more about NLU|faq/nlu|faq/nlu|100.0%|✅|
|3480|🟢|how can I add new language to rasa core|faq/languages|faq/languages|100.0%|✅|
|3481|🟢|How did you come to be?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|3482|🟢|I'm installing Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|3483|🟢|Can I speak to anyone who can really help me?|human_handoff|human_handoff|100.0%|✅|
|3484|🟢|Ok I want to talk to your sales team immediately|contact_sales|contact_sales|100.0%|✅|
|3485|🟢|What does rasa do exactly?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3486|🟢|What events are there?|ask_which_events|ask_which_events|100.0%|✅|
|3487|🟢|cya|bye|bye|100.0%|✅|
|3488|🟢|heelio|greet|greet|100.0%|✅|
|3489|🟢|where is the api for rasa x|technical_question|technical_question|100.0%|✅|
|3490|🟢|what is playground ?|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|3491|🟢|amayzing|affirm|affirm|100.0%|✅|
|3492|🟢|When will the next event occur in the community?|ask_which_events|ask_which_events|100.0%|✅|
|3493|🟢|yeah go on explaining what rasa is|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3494|🟢|Is there a Rasa event in San Francisco|ask_which_events|ask_which_events|100.0%|✅|
|3495|🟢|Is rasa community big?|faq/community_size|faq/community_size|100.0%|✅|
|3496|🟢|how to start RASA|how_to_get_started|how_to_get_started|100.0%|✅|
|3497|🟢|how does rasa dialogue management work?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|3498|🟢|Hi man|greet|greet|100.0%|✅|
|3499|🟢|how can I contribute?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|3500|🟢|Hi, how can i get started with rasa x|how_to_get_started|how_to_get_started|100.0%|✅|
|3501|🟢|language = english|enter_data|enter_data|100.0%|✅|
|3502|🟢|language: english|enter_data|enter_data|100.0%|✅|
|3503|🟢|How to install Rasa Core?|install_rasa|install_rasa|100.0%|✅|
|3504|🟢|can you forward me to your team|human_handoff|human_handoff|100.0%|✅|
|3505|🟢|No thank you|deny|deny|100.0%|✅|
|3506|🟢|No, thank you|deny|deny|100.0%|✅|
|3507|🟢|good.|affirm|affirm|100.0%|✅|
|3508|🟢|whats rasaplayground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|3509|🟢|hey sara|greet|greet|100.0%|✅|
|3510|🟢|hey, sara!|greet|greet|100.0%|✅|
|3511|🟢|NO DON"T WANT THIS!|deny|deny|100.0%|✅|
|3512|🟢|halo|greet|greet|100.0%|✅|
|3513|🟢|i want to book a appointment|contact_sales|contact_sales|100.0%|✅|
|3514|🟢|what is you name and where are you from|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|3515|🟢|Explain my name to me.|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|3516|🟢|nein|deny|deny|100.0%|✅|
|3517|🟢|I'm new in Rasa, help me!|how_to_get_started|how_to_get_started|100.0%|✅|
|3518|🟢|Can you get me Rasa Core?|install_rasa|install_rasa|100.0%|✅|
|3519|🟢|WHo am I|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|3520|🟢|Who am I?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|3521|🟢|who am i|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|3522|🟢|what sort of social events are we throwing?|ask_which_events|ask_which_events|100.0%|✅|
|3523|🟢|why only rasa|why_rasa|why_rasa|100.0%|✅|
|3524|🟢|why is rasa interesting|why_rasa|why_rasa|100.0%|✅|
|3525|🟢|How i install|install_rasa|install_rasa|100.0%|✅|
|3526|🟢|i would just like to have the link for the community|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|3527|🟢|hahah|react_positive|react_positive|100.0%|✅|
|3528|🟢|rasa components|faq/rasa_components|faq/rasa_components|100.0%|✅|
|3529|🟢|how can I meet eh community?|ask_which_events|ask_which_events|100.0%|✅|
|3530|🟢|neither|deny|deny|100.0%|✅|
|3531|🟢|What am I called?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|3532|🟢|hi there it's me|greet|greet|100.0%|✅|
|3533|🟢|how to install the rasa stack|install_rasa|install_rasa|100.0%|✅|
|3534|🟢|i'd rather speak with a real rasa employee|human_handoff|human_handoff|100.0%|✅|
|3535|🟢|we don't have one|enter_data|enter_data|100.0%|✅|
|3536|🟢|how to start rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|3537|🟢|I want to talk to the founders|human_handoff|human_handoff|100.0%|✅|
|3538|🟢|Thats so rude|react_negative|react_negative|100.0%|✅|
|3539|🟢|What is the next event in Paris?|ask_which_events|ask_which_events|100.0%|✅|
|3540|🟢|see you . bye|bye|bye|100.0%|✅|
|3541|🟢|i need the call request|contact_sales|contact_sales|100.0%|✅|
|3542|🟢|give me your age?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|3543|🟢|no. u r idiot|deny|deny|100.0%|✅|
|3544|🟢|What is the next event for Seattle?|ask_which_events|ask_which_events|100.0%|✅|
|3545|🟢|hi pal!|greet|greet|100.0%|✅|
|3546|🟢|ok then you cant help me|canthelp|canthelp|100.0%|✅|
|3547|🟢|NO|deny|deny|100.0%|✅|
|3548|🟢|no|deny|deny|100.0%|✅|
|3549|🟢|no :(|deny|deny|100.0%|✅|
|3550|🟢|no!!!!|deny|deny|100.0%|✅|
|3551|🟢|why use rasa|why_rasa|why_rasa|100.0%|✅|
|3552|🟢|who the hell are you?|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|3553|🟢|let me speak to a real person please|human_handoff|human_handoff|100.0%|✅|
|3554|🟢|Can I speak to a human?|human_handoff|human_handoff|100.0%|✅|
|3555|🟢|Yep that's fine|affirm|affirm|100.0%|✅|
|3556|🟢|Hi bot|greet|greet|100.0%|✅|
|3557|🟢|Hi, bot|greet|greet|100.0%|✅|
|3558|🟢|speak to a real person|human_handoff|human_handoff|100.0%|✅|
|3559|🟢|do you have a core tutorial i can follow|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|3560|🟢|Why choose rasa?|why_rasa|why_rasa|100.0%|✅|
|3561|🟢|i need a tutorial on how to use rasa nlu|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|3562|🟢|hi i am not able install rasa demo in my machine|install_rasa|install_rasa|100.0%|✅|
|3563|🟢|a call|contact_sales|contact_sales|100.0%|✅|
|3564|🟢|when is the next community event gonna be?|ask_which_events|ask_which_events|100.0%|✅|
|3565|🟢|how do i build a rasa chatbot?|how_to_get_started|how_to_get_started|100.0%|✅|
|3566|🟢|talk to human|human_handoff|human_handoff|100.0%|✅|
|3567|🟢|Find me a place to eat|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|3568|🟢|no you did it wrong|deny|deny|100.0%|✅|
|3569|🟢|I need a real person|human_handoff|human_handoff|100.0%|✅|
|3570|🟢|When is the next event in Berlin|ask_which_events|ask_which_events|100.0%|✅|
|3571|🟢|how is intent classification managed in rasa?|nlu_info|nlu_info|100.0%|✅|
|3572|🟢|no ma'am|deny|deny|100.0%|✅|
|3573|🟢|I have a few questions on my pay check|need_help_broad|need_help_broad|100.0%|✅|
|3574|🟢|how big is your community|faq/community_size|faq/community_size|100.0%|✅|
|3575|🟢|i want a tutorial on rasa nlu|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|3576|🟢|do you know how to set up a chatbot?|how_to_get_started|how_to_get_started|100.0%|✅|
|3577|🟢|no, i want to talk to human|human_handoff|human_handoff|100.0%|✅|
|3578|🟢|migration from LUIS|switch|switch|100.0%|✅|
|3579|🟢|which language is rasa programmed in|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|3580|🟢|jojojo|greet|greet|100.0%|✅|
|3581|🟢|nö|deny|deny|100.0%|✅|
|3582|🟢|i am happy|react_positive|react_positive|100.0%|✅|
|3583|🟢|ayyyy whaddup|greet|greet|100.0%|✅|
|3584|🟢|explain integrations|faq/channels|faq/channels|100.0%|✅|
|3585|🟢|cool|react_positive|react_positive|100.0%|✅|
|3586|🟢|cool :)|react_positive|react_positive|100.0%|✅|
|3587|🟢|cool!|react_positive|react_positive|100.0%|✅|
|3588|🟢|Is there a meetup|ask_which_events|ask_which_events|100.0%|✅|
|3589|🟢|i want to learn about rasa nlu|faq/nlu|faq/nlu|100.0%|✅|
|3590|🟢|human handoff|human_handoff|human_handoff|100.0%|✅|
|3591|🟢|how does rasa x stack up against rasa|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|3592|🟢|thats fine|affirm|affirm|100.0%|✅|
|3593|🟢|how to install rasa_nlu|install_rasa|install_rasa|100.0%|✅|
|3594|🟢|goodbye|bye|bye|100.0%|✅|
|3595|🟢|goodbye.|bye|bye|100.0%|✅|
|3596|🟢|Hallo|greet|greet|100.0%|✅|
|3597|🟢|Can you tell me who I am?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|3598|🟢|Can you tell me who am I?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|3599|🟢|can you tell me who I am?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|3600|🟢|user can communicate with the bot in spanish|enter_data|enter_data|100.0%|✅|
|3601|🟢|when will our next group event be?|ask_which_events|ask_which_events|100.0%|✅|
|3602|🟢|i will leave|react_negative|react_negative|100.0%|✅|
|3603|🟢|i want a tutorial on nlu|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|3604|🟢|Looks nice|react_positive|react_positive|100.0%|✅|
|3605|🟢|diffrence between rasa core and rasa nlu|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|3606|🟢|hi mrs rasa|greet|greet|100.0%|✅|
|3607|🟢|i want to know how to start with Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|3608|🟢|no and no again|deny|deny|100.0%|✅|
|3609|🟢|I still don’t get how entity recognition works|nlu_info|nlu_info|100.0%|✅|
|3610|🟢|hhola|greet|greet|100.0%|✅|
|3611|🟢|where to start the development of rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|3612|🟢|i don't have it|enter_data|enter_data|100.0%|✅|
|3613|🟢|can you show me a core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|3614|🟢|no i dont want to|deny|deny|100.0%|✅|
|3615|🟢|How can i contact the team ?|contact_sales|contact_sales|100.0%|✅|
|3616|🟢|connect to sales|contact_sales|contact_sales|100.0%|✅|
|3617|🟢|What do people call me?|chitchat/ask_whatismyname|chitchat/ask_whatismyname|100.0%|✅|
|3618|🟢|heyo|greet|greet|100.0%|✅|
|3619|🟢|boring|react_negative|react_negative|100.0%|✅|
|3620|🟢|HEllo|greet|greet|100.0%|✅|
|3621|🟢|hey there|greet|greet|100.0%|✅|
|3622|🟢|hey there..|greet|greet|100.0%|✅|
|3623|🟢|chinese|enter_data|enter_data|100.0%|✅|
|3624|🟢|i want to speak to customer service|human_handoff|human_handoff|100.0%|✅|
|3625|🟢|nothing|enter_data|enter_data|100.0%|✅|
|3626|🟢|Tell me the events you have|ask_which_events|ask_which_events|100.0%|✅|
|3627|🟢|how old are u|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|3628|🟢|i want to subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|3629|🟢|name what a slot is|faq/slots|faq/slots|100.0%|✅|
|3630|🟢|PLEASE|affirm|affirm|100.0%|✅|
|3631|🟢|no i don't accept|deny|deny|100.0%|✅|
|3632|🟢|Could I talk to Tyrone King?|human_handoff|human_handoff|100.0%|✅|
|3633|🟢|hi friends|greet|greet|100.0%|✅|
|3634|🟢|how to build a chatbot|how_to_get_started|how_to_get_started|100.0%|✅|
|3635|🟢|why not use watson?|why_rasa|why_rasa|100.0%|✅|
|3636|🟢|why switch?|why_rasa|why_rasa|100.0%|✅|
|3637|🟢|how to create a basic chat bot|how_to_get_started|how_to_get_started|100.0%|✅|
|3638|🟢|what is a component in rasa?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|3639|🟢|deny|deny|deny|100.0%|✅|
|3640|🟢|can i speak to the sales team|contact_sales|contact_sales|100.0%|✅|
|3641|🟢|good night|bye|bye|100.0%|✅|
|3642|🟢|is Rasa available in java ?|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|3643|🟢|when can you tell me what a slot is ?|faq/slots|faq/slots|100.0%|✅|
|3644|🟢|hi friend|greet|greet|100.0%|✅|
|3645|🟢|What's new?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|3646|🟢|tell me more about NLU|faq/nlu|faq/nlu|100.0%|✅|
|3647|🟢|can you explain what the events are?|ask_which_events|ask_which_events|100.0%|✅|
|3648|🟢|Good|affirm|affirm|100.0%|✅|
|3649|🟢|I want to get in touch with your sales guys|contact_sales|contact_sales|100.0%|✅|
|3650|🟢|Tell me who I am.|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|3651|🟢|Tell me who I am?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|3652|🟢|Tell me who am I?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|3653|🟢|tell me who I am?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|3654|🟢|how can i get data from a database and use them as a response to a question?|technical_question|technical_question|100.0%|✅|
|3655|🟢|Sign up.|signup_newsletter|signup_newsletter|100.0%|✅|
|3656|🟢|hai|greet|greet|100.0%|✅|
|3657|🟢|hey dude|greet|greet|100.0%|✅|
|3658|🟢|sales sales sales|contact_sales|contact_sales|100.0%|✅|
|3659|🟢|what version of python|faq/python_version|faq/python_version|100.0%|✅|
|3660|🟢|hello|greet|greet|100.0%|✅|
|3661|🟢|hello?|greet|greet|100.0%|✅|
|3662|🟢|hello]|greet|greet|100.0%|✅|
|3663|🟢|I want to install Rasa X|install_rasa|install_rasa|100.0%|✅|
|3664|🟢|What events are scheduled for today?|ask_which_events|ask_which_events|100.0%|✅|
|3665|🟢|How to migrate from Luis?|switch|switch|100.0%|✅|
|3666|🟢|i need a rasa core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|3667|🟢|can I speak to a person?|human_handoff|human_handoff|100.0%|✅|
|3668|🟢|tell me more about rasa nlu|faq/nlu|faq/nlu|100.0%|✅|
|3669|🟢|nop|deny|deny|100.0%|✅|
|3670|🟢|HELLO|greet|greet|100.0%|✅|
|3671|🟢|it sucks|deny|deny|100.0%|✅|
|3672|🟢|Why switch to Rasa?|why_rasa|why_rasa|100.0%|✅|
|3673|🟢|What is the date of the next community event?|ask_which_events|ask_which_events|100.0%|✅|
|3674|🟢|can I install this on a mac?|technical_question|technical_question|100.0%|✅|
|3675|🟢|thats great|affirm|affirm|100.0%|✅|
|3676|🟢|how do I start|how_to_get_started|how_to_get_started|100.0%|✅|
|3677|🟢|I have a specific question regarding installation|install_rasa|install_rasa|100.0%|✅|
|3678|🟢|please|affirm|affirm|100.0%|✅|
|3679|🟢|how do I build a bot?|how_to_get_started|how_to_get_started|100.0%|✅|
|3680|🟢|Could you tell me more about Rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3681|🟢|could you tell me more about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3682|🟢|i sad|react_negative|react_negative|100.0%|✅|
|3683|🟢|tell me something about core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|3684|🟢|never|deny|deny|100.0%|✅|
|3685|🟢|You're nice.|react_positive|react_positive|100.0%|✅|
|3686|🟢|why should I migrate to rasa?|why_rasa|why_rasa|100.0%|✅|
|3687|🟢|halloo|greet|greet|100.0%|✅|
|3688|🟢|Cool|react_positive|react_positive|100.0%|✅|
|3689|🟢|im moving luis|switch|switch|100.0%|✅|
|3690|🟢|such a great demo|react_positive|react_positive|100.0%|✅|
|3691|🟢|nah I'm good|deny|deny|100.0%|✅|
|3692|🟢|yeah, why not|affirm|affirm|100.0%|✅|
|3693|🟢|what rasa_nlu|faq/nlu|faq/nlu|100.0%|✅|
|3694|🟢|Can you tell me more about NLU?|faq/nlu|faq/nlu|100.0%|✅|
|3695|🟢|i'm sad|react_negative|react_negative|100.0%|✅|
|3696|🟢|how do i sstart|how_to_get_started|how_to_get_started|100.0%|✅|
|3697|🟢|can you explain rasa playground to me|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|3698|🟢|none of them|deny|deny|100.0%|✅|
|3699|🟢|half a million|enter_data|enter_data|100.0%|✅|
|3700|🟢|i guess it means - no|deny|deny|100.0%|✅|
|3701|🟢|hey rasa|greet|greet|100.0%|✅|
|3702|🟢|Can I have a call?|contact_sales|contact_sales|100.0%|✅|
|3703|🟢|its an chinese bot|enter_data|enter_data|100.0%|✅|
|3704|🟢|hello hi|greet|greet|100.0%|✅|
|3705|🟢|hallo|greet|greet|100.0%|✅|
|3706|🟢|By chance do you know the date of next community event?|ask_which_events|ask_which_events|100.0%|✅|
|3707|🟢|see you|bye|bye|100.0%|✅|
|3708|🟢|I need to get Rasa Stack up and running.|install_rasa|install_rasa|100.0%|✅|
|3709|🟢|konichiwa|greet|greet|100.0%|✅|
|3710|🟢|hi hi|greet|greet|100.0%|✅|
|3711|🟢|more information on components in rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|3712|🟢|how do i train rasa nlu|how_to_get_started|how_to_get_started|100.0%|✅|
|3713|🟢|How to migrate from DialogFlwo|switch|switch|100.0%|✅|
|3714|🟢|rasa playground|enter_data|enter_data|100.0%|✅|
|3715|🟢|id like to talk to a real rasa employee|human_handoff|human_handoff|100.0%|✅|
|3716|🟢|yeah how about the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|3717|🟢|iam not feeling good|react_negative|react_negative|100.0%|✅|
|3718|🟢|rasa core quickstart|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|3719|🟢|i am!|affirm|affirm|100.0%|✅|
|3720|🟢|how about your age|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|3721|🟢|more about NLU|faq/nlu|faq/nlu|100.0%|✅|
|3722|🟢|More about NLU|faq/nlu|faq/nlu|100.0%|✅|
|3723|🟢|gotta go|bye|bye|100.0%|✅|
|3724|🟢|Do you understand spanish?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|3725|🟢|i want to learn more about Rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|3726|🟢|nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|3727|🟢|Yeah sure|affirm|affirm|100.0%|✅|
|3728|🟢|Can i talk to a human instead|human_handoff|human_handoff|100.0%|✅|
|3729|🟢|What's the next community event|ask_which_events|ask_which_events|100.0%|✅|
|3730|🟢|What are all of the events you have?|ask_which_events|ask_which_events|100.0%|✅|
|3731|🟢|tell me about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3732|🟢|Where were you born?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|3733|🟢|hola|greet|greet|100.0%|✅|
|3734|🟢|help with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|3735|🟢|is rasa core paid?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|3736|🟢|When is the next event in california?|ask_which_events|ask_which_events|100.0%|✅|
|3737|🟢|subscrime me|signup_newsletter|signup_newsletter|100.0%|✅|
|3738|🟢|pip|enter_data|enter_data|100.0%|✅|
|3739|🟢|farewell|bye|bye|100.0%|✅|
|3740|🟢|Time, please!|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|3741|🟢|tell me what's your skill|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3742|🟢|yes that's what i want|affirm|affirm|100.0%|✅|
|3743|🟢|I think I want to install Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|3744|🟢|sadly|react_negative|react_negative|100.0%|✅|
|3745|🟢|i want on that dope newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|3746|🟢|How do I ask a question on the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|3747|🟢|Tell me all of the events you have.|ask_which_events|ask_which_events|100.0%|✅|
|3748|🟢|toodle-oo|bye|bye|100.0%|✅|
|3749|🟢|can i speak to your human|human_handoff|human_handoff|100.0%|✅|
|3750|🟢|merhaba|greet|greet|100.0%|✅|
|3751|🟢|book|contact_sales|contact_sales|100.0%|✅|
|3752|🟢|how do i train rasa core|how_to_get_started|how_to_get_started|100.0%|✅|
|3753|🟢|what you talk about?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|3754|🟢|On what day is the next event scheduled?|ask_which_events|ask_which_events|100.0%|✅|
|3755|🟢|decline|deny|deny|100.0%|✅|
|3756|🟢|id like to subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|3757|🟢|salut|greet|greet|100.0%|✅|
|3758|🟢|hi again|greet|greet|100.0%|✅|
|3759|🟢|hi sara|greet|greet|100.0%|✅|
|3760|🟢|nah, i'm good|deny|deny|100.0%|✅|
|3761|🟢|How to migrate from DialogFlow to Rasa?|switch|switch|100.0%|✅|
|3762|🟢|ssup?|greet|greet|100.0%|✅|
|3763|🟢|see u later|bye|bye|100.0%|✅|
|3764|🟢|When does the upcoming event occur?|ask_which_events|ask_which_events|100.0%|✅|
|3765|🟢|how about nlu|faq/nlu|faq/nlu|100.0%|✅|
|3766|🟢|python version|faq/python_version|faq/python_version|100.0%|✅|
|3767|🟢|python version?|faq/python_version|faq/python_version|100.0%|✅|
|3768|🟢|does the community have meet ups?|ask_which_events|ask_which_events|100.0%|✅|
|3769|🟢|How to make a bot|how_to_get_started|how_to_get_started|100.0%|✅|
|3770|🟢|Any other event like rasa meetup in future?|ask_which_events|ask_which_events|100.0%|✅|
|3771|🟢|Hi sara|greet|greet|100.0%|✅|
|3772|🟢|Hi sara..|greet|greet|100.0%|✅|
|3773|🟢|Hieee|greet|greet|100.0%|✅|
|3774|🟢|Is there a connector for skype?|faq/channels|faq/channels|100.0%|✅|
|3775|🟢|When is the next event in detroit?|ask_which_events|ask_which_events|100.0%|✅|
|3776|🟢|can we converse in french?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|3777|🟢|What's a good place to eat nearby|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|3778|🟢|nah not for me|deny|deny|100.0%|✅|
|3779|🟢|no bots at all|deny|deny|100.0%|✅|
|3780|🟢|operations|enter_data|enter_data|100.0%|✅|
|3781|🟢|temperature?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|3782|🟢|hello there|greet|greet|100.0%|✅|
|3783|🟢|I get errors while installation|need_help_broad|need_help_broad|100.0%|✅|
|3784|🟢|where can I find out what a slot is?|faq/slots|faq/slots|100.0%|✅|
|3785|🟢|see playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|3786|🟢|How do I start|how_to_get_started|how_to_get_started|100.0%|✅|
|3787|🟢|what is Rasa X ?|faq/rasax|faq/rasax|100.0%|✅|
|3788|🟢|can i get emails from you|signup_newsletter|signup_newsletter|100.0%|✅|
|3789|🟢|how have you been built?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|3790|🟢|What is your root?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|3791|🟢|hello friend|greet|greet|100.0%|✅|
|3792|🟢|i want to build bots|enter_data|enter_data|100.0%|✅|
|3793|🟢|Can you tell me what kinds of events you have?|ask_which_events|ask_which_events|100.0%|✅|
|3794|🟢|that was a great interaction|react_positive|react_positive|100.0%|✅|
|3795|🟢|na|deny|deny|100.0%|✅|
|3796|🟢|nehi|deny|deny|100.0%|✅|
|3797|🟢|where can I see a calendar of community events?|ask_which_events|ask_which_events|100.0%|✅|
|3798|🟢|how to restart the rasa|technical_question|technical_question|100.0%|✅|
|3799|🟢|from where I should start?|how_to_get_started|how_to_get_started|100.0%|✅|
|3800|🟢|Hello sara|greet|greet|100.0%|✅|
|3801|🟢|i want to get started|how_to_get_started|how_to_get_started|100.0%|✅|
|3802|🟢|user can talk to my bot in portuguese|enter_data|enter_data|100.0%|✅|
|3803|🟢|give me a human now|human_handoff|human_handoff|100.0%|✅|
|3804|🟢|let me speak with a real person please|human_handoff|human_handoff|100.0%|✅|
|3805|🟢|Tell me about rasa x ee|faq/ee|faq/ee|100.0%|✅|
|3806|🟢|tell me about rasa x EE|faq/ee|faq/ee|100.0%|✅|
|3807|🟢|hello world|greet|greet|100.0%|✅|
|3808|🟢|How can I assist the cause?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|3809|🟢|install|install_rasa|install_rasa|100.0%|✅|
|3810|🟢|see ya|bye|bye|100.0%|✅|
|3811|🟢|do you know how old you are?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|3812|🟢|Can I assist?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|3813|🟢|no thank s|deny|deny|100.0%|✅|
|3814|🟢|I don't wanna talk to a bot|human_handoff|human_handoff|100.0%|✅|
|3815|🟢|why rasa|why_rasa|why_rasa|100.0%|✅|
|3816|🟢|Hey Sara|greet|greet|100.0%|✅|
|3817|🟢|When is the next event for India?|ask_which_events|ask_which_events|100.0%|✅|
|3818|🟢|i feel sad|react_negative|react_negative|100.0%|✅|
|3819|🟢|i am feel sad|react_negative|react_negative|100.0%|✅|
|3820|🟢|catch you later|bye|bye|100.0%|✅|
|3821|🟢|Nopes|deny|deny|100.0%|✅|
|3822|🟢|Hello Sara|greet|greet|100.0%|✅|
|3823|🟢|i'd like to build a transformer|enter_data|enter_data|100.0%|✅|
|3824|🟢|n|deny|deny|100.0%|✅|
|3825|🟢|come stai?|out_of_scope/non_english|out_of_scope/non_english|100.0%|✅|
|3826|🟢|i would like to subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|3827|🟢|wow|react_positive|react_positive|100.0%|✅|
|3828|🟢|rasa nlu tutorial|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|3829|🟢|how to get start|how_to_get_started|how_to_get_started|100.0%|✅|
|3830|🟢|i want to receive your nl|signup_newsletter|signup_newsletter|100.0%|✅|
|3831|🟢|hm ok then i want to talk to the sales dude|contact_sales|contact_sales|100.0%|✅|
|3832|🟢|k byyye #slay|bye|bye|100.0%|✅|
|3833|🟢|hi i'm Sandra Hernandez|greet|greet|100.0%|✅|
|3834|🟢|Yeah please help me out|how_to_get_started|how_to_get_started|100.0%|✅|
|3835|🟢|where do i start?|how_to_get_started|how_to_get_started|100.0%|✅|
|3836|🟢|what is rasa nlu?|faq/nlu|faq/nlu|100.0%|✅|
|3837|🟢|Tell me about the entity recognition|nlu_info|nlu_info|100.0%|✅|
|3838|🟢|no i dont want to accept :P lol|deny|deny|100.0%|✅|
|3839|🟢|can someone help me with infos about rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|3840|🟢|What messaging systems are supported by rasa?|faq/channels|faq/channels|100.0%|✅|
|3841|🟢|how do you do?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|3842|🟢|tell me about core please|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|3843|🟢|I'm sad|react_negative|react_negative|100.0%|✅|
|3844|🟢|Nah|deny|deny|100.0%|✅|
|3845|🟢|so sad|react_negative|react_negative|100.0%|✅|
|3846|🟢|so sad :(|react_negative|react_negative|100.0%|✅|
|3847|🟢|hieee|greet|greet|100.0%|✅|
|3848|🟢|Close this talk|bye|bye|100.0%|✅|
|3849|🟢|I would like to talk to someone from your sales team|contact_sales|contact_sales|100.0%|✅|
|3850|🟢|i want to signup|signup_newsletter|signup_newsletter|100.0%|✅|
|3851|🟢|hello sara|greet|greet|100.0%|✅|
|3852|🟢|yo|greet|greet|100.0%|✅|
|3853|🟢|hello is anybody there|greet|greet|100.0%|✅|
|3854|🟢|why should i choose rasa|why_rasa|why_rasa|100.0%|✅|
|3855|🟢|Assuming that there is an upcoming event, when is that event?|ask_which_events|ask_which_events|100.0%|✅|
|3856|🟢|How were you conceived?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|3857|🟢|can i took with a real person|human_handoff|human_handoff|100.0%|✅|
|3858|🟢|it is in german|enter_data|enter_data|100.0%|✅|
|3859|🟢|this is a really frustrating experience|react_negative|react_negative|100.0%|✅|
|3860|🟢|i would like to speak to a person|human_handoff|human_handoff|100.0%|✅|
|3861|🟢|how to build assistant?|how_to_get_started|how_to_get_started|100.0%|✅|
|3862|🟢|how to install rasa core?|install_rasa|install_rasa|100.0%|✅|
|3863|🟢|uh-huh|affirm|affirm|100.0%|✅|
|3864|🟢|what does rasa mean|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3865|🟢|How can I be more involved?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|3866|🟢|rasa core tutorial|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|3867|🟢|I like you|react_positive|react_positive|100.0%|✅|
|3868|🟢|how do i migrate from dialogflow|switch|switch|100.0%|✅|
|3869|🟢|why should i use rasa instead of IBM watson ?|why_rasa|why_rasa|100.0%|✅|
|3870|🟢|what events are there going to be?|ask_which_events|ask_which_events|100.0%|✅|
|3871|🟢|I'm super sad|react_negative|react_negative|100.0%|✅|
|3872|🟢|i need help with rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|3873|🟢|I said, helllllloooooO!!!!|greet|greet|100.0%|✅|
|3874|🟢|When is the next event for Detroit?|ask_which_events|ask_which_events|100.0%|✅|
|3875|🟢|i guess you can't help me then|canthelp|canthelp|100.0%|✅|
|3876|🟢|whats popping|greet|greet|100.0%|✅|
|3877|🟢|any open source GUI rasa have?|technical_question|technical_question|100.0%|✅|
|3878|🟢|hello Sara|greet|greet|100.0%|✅|
|3879|🟢|rasa core agent information|technical_question|technical_question|100.0%|✅|
|3880|🟢|How can I be helpful?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|3881|🟢|what is rasax|faq/rasax|faq/rasax|100.0%|✅|
|3882|🟢|which user interface can I use?|faq/channels|faq/channels|100.0%|✅|
|3883|🟢|Can i use NLU on its own|technical_question|technical_question|100.0%|✅|
|3884|🟢|hi im Amanda Anderson|greet|greet|100.0%|✅|
|3885|🟢|custom ner|nlu_info|nlu_info|100.0%|✅|
|3886|🟢|i get error when initializing a project|need_help_broad|need_help_broad|100.0%|✅|
|3887|🟢|definitely not|deny|deny|100.0%|✅|
|3888|🟢|I am trying to build a bot using rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|3889|🟢|Give me the events you have.|ask_which_events|ask_which_events|100.0%|✅|
|3890|🟢|adios|bye|bye|100.0%|✅|
|3891|🟢|adios?|bye|bye|100.0%|✅|
|3892|🟢|nah|deny|deny|100.0%|✅|
|3893|🟢|ok, but that doesnt help me|canthelp|canthelp|100.0%|✅|
|3894|🟢|Please connect me to someone from sales|contact_sales|contact_sales|100.0%|✅|
|3895|🟢|alexa|faq/voice|faq/voice|100.0%|✅|
|3896|🟢|how can i migrate from dialogflow?|switch|switch|100.0%|✅|
|3897|🟢|howdy|greet|greet|100.0%|✅|
|3898|🟢|start rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|3899|🟢|what is nlu|faq/nlu|faq/nlu|100.0%|✅|
|3900|🟢|How to get start|how_to_get_started|how_to_get_started|100.0%|✅|
|3901|🟢|okay cool|affirm|affirm|100.0%|✅|
|3902|🟢|is rasa free|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|3903|🟢|give me a human|human_handoff|human_handoff|100.0%|✅|
|3904|🟢|Why rasa?|why_rasa|why_rasa|100.0%|✅|
|3905|🟢|do u know Alexa?|faq/voice|faq/voice|100.0%|✅|
|3906|🟢|when is the event within the community gonna happen?|ask_which_events|ask_which_events|100.0%|✅|
|3907|🟢|Country names|enter_data|enter_data|100.0%|✅|
|3908|🟢|How can I be a contributor?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|3909|🟢|Tell me how I can contribute|ask_how_contribute|ask_how_contribute|100.0%|✅|
|3910|🟢|what chat services do you support|faq/channels|faq/channels|100.0%|✅|
|3911|🟢|Hi Sara|greet|greet|100.0%|✅|
|3912|🟢|Hi Sara!|greet|greet|100.0%|✅|
|3913|🟢|I have chosen Rasa Stack|install_rasa|install_rasa|100.0%|✅|
|3914|🟢|Do you have rasa forum?|faq/what_is_forum|faq/what_is_forum|100.0%|✅|
|3915|🟢|ola sara|greet|greet|100.0%|✅|
|3916|🟢|Shall i know who am i?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|3917|🟢|How to migrate to DialogFlow?|switch|switch|100.0%|✅|
|3918|🟢|are you a rasa bot?|chitchat/ask_isbot|chitchat/ask_isbot|100.0%|✅|
|3919|🟢|I am happy|react_positive|react_positive|100.0%|✅|
|3920|🟢|what can I do with Rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3921|🟢|what can i do with rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|3922|🟢|yes i wanna know more about rasa nlu|faq/nlu|faq/nlu|100.0%|✅|
|3923|🟢|Do you have a user group|ask_which_events|ask_which_events|100.0%|✅|
|3924|🟢|installation of tensorflow-text|technical_question|technical_question|100.0%|✅|
|3925|🟢|more about NLU please|faq/nlu|faq/nlu|100.0%|✅|
|3926|🟢|i need a good tutorial for rasa|faq/tutorials|faq/tutorials|100.0%|✅|
|3927|🟢|i want to talk to someone else|human_handoff|human_handoff|100.0%|✅|
|3928|🟢|why would you opt for rasa|why_rasa|why_rasa|100.0%|✅|
|3929|🟢|How can one contribute?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|3930|🟢|How can one contribute to this cause?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|3931|🟢|I need to know about Rasa playground|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|3932|🟢|just NLU|enter_data|enter_data|100.0%|✅|
|3933|🟢|i am angry over you|react_negative|react_negative|100.0%|✅|
|3934|🟢|How did they create you?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|3935|🟢|can i migrate my luis bot to raza|switch|switch|100.0%|✅|
|3936|🟢|Nevermind|deny|deny|100.0%|✅|
|3937|🟢|jop|greet|greet|100.0%|✅|
|3938|🟢|Well hello there ;)|greet|greet|100.0%|✅|
|3939|🟢|i decline|deny|deny|100.0%|✅|
|3940|🟢|ciao|bye|bye|100.0%|✅|
|3941|🟢|hellooo|greet|greet|100.0%|✅|
|3942|🟢|x|enter_data|enter_data|100.0%|✅|
|3943|🟢|rasa basics|how_to_get_started|how_to_get_started|100.0%|✅|
|3944|🟢|How do i write a forum question?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|3945|🟢|how is entity recognition managed in rasa?|nlu_info|nlu_info|100.0%|✅|
|3946|🟢|go|affirm|affirm|100.0%|✅|
|3947|🟢|Can i have a deno|book_demo|book_demo|100.0%|✅|
|3948|🟢|getting some error|technical_question|technical_question|100.0%|✅|
|3949|🟢|on that will get me promoted|enter_data|enter_data|100.0%|✅|
|3950|🟢|can you help me with the rasa core ?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|3951|🟢|what is the difference?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|3952|🟢|HI Sara|greet|greet|100.0%|✅|
|3953|🟢|Bonjour|greet|greet|100.0%|✅|
|3954|🟢|super sad|react_negative|react_negative|100.0%|✅|
|3955|🟢|what's rasa nlu|faq/nlu|faq/nlu|100.0%|✅|
|3956|🟢|How many people are here?|faq/community_size|faq/community_size|100.0%|✅|
|3957|🟢|are you multilingual?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|3958|🟢|Do you know when is the next event in Montreal?|ask_which_events|ask_which_events|100.0%|✅|
|3959|🟢|components in rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|3960|🟢|halo sara|greet|greet|100.0%|✅|
|3961|🟢|why should I switch|why_rasa|why_rasa|100.0%|✅|
|3962|🟢|Do you know the exact date for the next community event?|ask_which_events|ask_which_events|100.0%|✅|
|3963|🟢|Can we stop at the forum so I can ask a question|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|3964|🟢|rasa core is open source?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|3965|🟢|why should I switch from luis|why_rasa|why_rasa|100.0%|✅|
|3966|🟢|Super! I love Rasa|react_positive|react_positive|100.0%|✅|
|3967|🟢|what is the difference between the two?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|3968|🟢|when is our next group event going to take place?|ask_which_events|ask_which_events|100.0%|✅|
|3969|🟢|I want to help improve Rasa|ask_how_contribute|ask_how_contribute|100.0%|✅|
|3970|🟢|do you use duckling|nlu_info|nlu_info|100.0%|✅|
|3971|🟢|I want to ask a question in the forum|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|3972|🟢|why should i use rasa instead of google dialogflow|why_rasa|why_rasa|100.0%|✅|
|3973|🟢|it is showing error while installing|need_help_broad|need_help_broad|100.0%|✅|
|3974|🟢|luis|switch|switch|100.0%|✅|
|3975|🟢|how can I help improve your code|ask_how_contribute|ask_how_contribute|100.0%|✅|
|3976|🟢|how can I help improve your code?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|3977|🟢|How to I post a question on the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|3978|🟢|hello, my name is Charles Pfeffer|greet|greet|100.0%|✅|
|3979|🟢|yes I would like to subscribe|signup_newsletter|signup_newsletter|100.0%|✅|
|3980|🟢|you're rather dull|react_negative|react_negative|100.0%|✅|
|3981|🟢|that's annoying I'd like to speak to someone real|human_handoff|human_handoff|100.0%|✅|
|3982|🟢|elaborate on rasa x|faq/rasax|faq/rasax|100.0%|✅|
|3983|🟢|Okay cool|affirm|affirm|100.0%|✅|
|3984|🟢|thats not helping, can i talk to human?|human_handoff|human_handoff|100.0%|✅|
|3985|🟢|why not use ibm watson|why_rasa|why_rasa|100.0%|✅|
|3986|🟢|i want to learn more about Rasa X EE|faq/ee|faq/ee|100.0%|✅|
|3987|🟢|what is rasa x ?|faq/rasax|faq/rasax|100.0%|✅|
|3988|🟢|Wow|react_positive|react_positive|100.0%|✅|
|3989|🟢|and that's it?|canthelp|canthelp|100.0%|✅|
|3990|🟢|What time do we have?|chitchat/ask_time|chitchat/ask_time|100.0%|✅|
|3991|🟢|No|deny|deny|100.0%|✅|
|3992|🟢|No.|deny|deny|100.0%|✅|
|3993|🟢|what is this nlu thing?|faq/nlu|faq/nlu|100.0%|✅|
|3994|🟢|get started pls|how_to_get_started|how_to_get_started|100.0%|✅|
|3995|🟢|let's make a subscribtion|signup_newsletter|signup_newsletter|100.0%|✅|
|3996|🟢|migration from dialogflow|switch|switch|100.0%|✅|
|3997|🟢|how do i install|install_rasa|install_rasa|100.0%|✅|
|3998|🟢|chatfuel|switch|switch|100.0%|✅|
|3999|🟢|i am sad|react_negative|react_negative|100.0%|✅|
|4000|🟢|In what ways can I help?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4001|🟢|Never|deny|deny|100.0%|✅|
|4002|🟢|am struck with installation of rasa nlu and core in my mac book|install_rasa|install_rasa|100.0%|✅|
|4003|🟢|i'm migrating from LUIS|switch|switch|100.0%|✅|
|4004|🟢|do the newsletter then|signup_newsletter|signup_newsletter|100.0%|✅|
|4005|🟢|lead generation|enter_data|enter_data|100.0%|✅|
|4006|🟢|I'm not giving you my email address|deny|deny|100.0%|✅|
|4007|🟢|I need to ask a question in the forum.|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4008|🟢|what do you guys do at rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4009|🟢|does it support AI|technical_question|technical_question|100.0%|✅|
|4010|🟢|How to install Rasa|install_rasa|install_rasa|100.0%|✅|
|4011|🟢|How to install Rasa?|install_rasa|install_rasa|100.0%|✅|
|4012|🟢|i want one platform please|contact_sales|contact_sales|100.0%|✅|
|4013|🟢|do you have a rasa tutorial|faq/tutorials|faq/tutorials|100.0%|✅|
|4014|🟢|i want to know about RASA Nlu|faq/nlu|faq/nlu|100.0%|✅|
|4015|🟢|i'd like to build sentient glibber or glitter|enter_data|enter_data|100.0%|✅|
|4016|🟢|hello everybody|greet|greet|100.0%|✅|
|4017|🟢|e commerce bot|enter_data|enter_data|100.0%|✅|
|4018|🟢|why to use rasa|why_rasa|why_rasa|100.0%|✅|
|4019|🟢|What can I do to help?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4020|🟢|hello robot|greet|greet|100.0%|✅|
|4021|🟢|no idea|enter_data|enter_data|100.0%|✅|
|4022|🟢|okay Rasabot, you're cool|react_positive|react_positive|100.0%|✅|
|4023|🟢|How to migrate from DialogFlow?|switch|switch|100.0%|✅|
|4024|🟢|non|deny|deny|100.0%|✅|
|4025|🟢|in what year were you born?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|4026|🟢|i need source code|source_code|source_code|100.0%|✅|
|4027|🟢|I am super sad|react_negative|react_negative|100.0%|✅|
|4028|🟢|how do I run rasa on windows|install_rasa|install_rasa|100.0%|✅|
|4029|🟢|tell me about core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|4030|🟢|hii|greet|greet|100.0%|✅|
|4031|🟢|i want to chat with human|human_handoff|human_handoff|100.0%|✅|
|4032|🟢|this sucks|deny|deny|100.0%|✅|
|4033|🟢|i would like more explanation on RASA Core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|4034|🟢|I am sad|react_negative|react_negative|100.0%|✅|
|4035|🟢|how old?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|4036|🟢|can you explain rasa x to me|faq/rasax|faq/rasax|100.0%|✅|
|4037|🟢|I need help to make rasa in java|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|4038|🟢|At what time is the next event scheduled?|ask_which_events|ask_which_events|100.0%|✅|
|4039|🟢|yes subscribe me|signup_newsletter|signup_newsletter|100.0%|✅|
|4040|🟢|Lets go to the forum so I can ask my question.|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4041|🟢|i want a tutorial on rasa core|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|4042|🟢|Hi rasa|greet|greet|100.0%|✅|
|4043|🟢|yoo|greet|greet|100.0%|✅|
|4044|🟢|hi Mister|greet|greet|100.0%|✅|
|4045|🟢|tlak to you later|bye|bye|100.0%|✅|
|4046|🟢|please can you book call for me|contact_sales|contact_sales|100.0%|✅|
|4047|🟢|it is going pretty badly|deny|deny|100.0%|✅|
|4048|🟢|When is it that the next event occurs?|ask_which_events|ask_which_events|100.0%|✅|
|4049|🟢|what can i build with rasa core?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|4050|🟢|no I haven't decided yet if I want to sign up|deny|deny|100.0%|✅|
|4051|🟢|How to build a bot in rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|4052|🟢|socket io|faq/channels|faq/channels|100.0%|✅|
|4053|🟢|hallo sara|greet|greet|100.0%|✅|
|4054|🟢|sad|react_negative|react_negative|100.0%|✅|
|4055|🟢|LUIS|switch|switch|100.0%|✅|
|4056|🟢|Hello Rasa|greet|greet|100.0%|✅|
|4057|🟢|add me to the subscription list|signup_newsletter|signup_newsletter|100.0%|✅|
|4058|🟢|how about the newsletter|signup_newsletter|signup_newsletter|100.0%|✅|
|4059|🟢|why RASA?|why_rasa|why_rasa|100.0%|✅|
|4060|🟢|Where can I ask a question on the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4061|🟢|Take me to the forum help section.|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4062|🟢|Can you tell me what Rasa does?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4063|🟢|I need to know about Rasa X|faq/rasax|faq/rasax|100.0%|✅|
|4064|🟢|How do I talk to a human|human_handoff|human_handoff|100.0%|✅|
|4065|🟢|how to add in my website|technical_question|technical_question|100.0%|✅|
|4066|🟢|what does nlu stands for|nlu_info|nlu_info|100.0%|✅|
|4067|🟢|what does rasa dialogue management do?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|4068|🟢|How to install rasa|install_rasa|install_rasa|100.0%|✅|
|4069|🟢|What are the events that you have?|ask_which_events|ask_which_events|100.0%|✅|
|4070|🟢|technical side of things?|technical_question|technical_question|100.0%|✅|
|4071|🟢|luis bot can migrate to raza bot ?|switch|switch|100.0%|✅|
|4072|🟢|gimme a proper human|human_handoff|human_handoff|100.0%|✅|
|4073|🟢|i dont wanna talk to a bot|human_handoff|human_handoff|100.0%|✅|
|4074|🟢|nah, first time|deny|deny|100.0%|✅|
|4075|🟢|hlo|greet|greet|100.0%|✅|
|4076|🟢|how to install on window|install_rasa|install_rasa|100.0%|✅|
|4077|🟢|it is ok|affirm|affirm|100.0%|✅|
|4078|🟢|how can I help?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4079|🟢|how to restart rasa|technical_question|technical_question|100.0%|✅|
|4080|🟢|how to restart rasa?|technical_question|technical_question|100.0%|✅|
|4081|🟢|wit|switch|switch|100.0%|✅|
|4082|🟢|Can rasa do calculations?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|4083|🟢|how to build chatbot using rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|4084|🟢|what are the componensts of RASA|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4085|🟢|I need to know if I can use Rasa to build an application?|how_to_get_started|how_to_get_started|100.0%|✅|
|4086|🟢|it is in spanish|enter_data|enter_data|100.0%|✅|
|4087|🟢|can you put me in touch with a human?|human_handoff|human_handoff|100.0%|✅|
|4088|🟢|you cant help me|canthelp|canthelp|100.0%|✅|
|4089|🟢|contact any sales person|contact_sales|contact_sales|100.0%|✅|
|4090|🟢|sign up|signup_newsletter|signup_newsletter|100.0%|✅|
|4091|🟢|why should I use rasa?|why_rasa|why_rasa|100.0%|✅|
|4092|🟢|it sux|deny|deny|100.0%|✅|
|4093|🟢|service agent|human_handoff|human_handoff|100.0%|✅|
|4094|🟢|Now I'm sad|react_negative|react_negative|100.0%|✅|
|4095|🟢|are you cool|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|4096|🟢|yaah|affirm|affirm|100.0%|✅|
|4097|🟢|how to restart rasax|technical_question|technical_question|100.0%|✅|
|4098|🟢|Which events you got?|ask_which_events|ask_which_events|100.0%|✅|
|4099|🟢|What languages can a program like rasa handle?|faq/languages|faq/languages|100.0%|✅|
|4100|🟢|I got stuck with the installation|need_help_broad|need_help_broad|100.0%|✅|
|4101|🟢|what is rasa x ee?|faq/ee|faq/ee|100.0%|✅|
|4102|🟢|how can i start with rasa core?|how_to_get_started|how_to_get_started|100.0%|✅|
|4103|🟢|hello sweatheart|greet|greet|100.0%|✅|
|4104|🟢|hellio|greet|greet|100.0%|✅|
|4105|🟢|Yes, I have a question|need_help_broad|need_help_broad|100.0%|✅|
|4106|🟢|newletter|signup_newsletter|signup_newsletter|100.0%|✅|
|4107|🟢|i am very sad|react_negative|react_negative|100.0%|✅|
|4108|🟢|what technologies did u use to create more mature chatbot?|technical_question|technical_question|100.0%|✅|
|4109|🟢|are there some nlu tutorials i could look at|faq/tutorial_nlu|faq/tutorial_nlu|100.0%|✅|
|4110|🟢|how to build bot with rasa x|how_to_get_started|how_to_get_started|100.0%|✅|
|4111|🟢|How is Rasa X different from Rasa?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|4112|🟢|I don’t understand how you handle intent classification at Rasa|nlu_info|nlu_info|100.0%|✅|
|4113|🟢|WOW|react_positive|react_positive|100.0%|✅|
|4114|🟢|source code|source_code|source_code|100.0%|✅|
|4115|🟢|Installing rasa|install_rasa|install_rasa|100.0%|✅|
|4116|🟢|how many ages?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|4117|🟢|I want to learn about entity recognition|nlu_info|nlu_info|100.0%|✅|
|4118|🟢|what is rasa core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|4119|🟢|what is rasa core?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|4120|🟢|What's the name of the place you came from?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|4121|🟢|get started|how_to_get_started|how_to_get_started|100.0%|✅|
|4122|🟢|can you please connect me to a real rasa employee?|human_handoff|human_handoff|100.0%|✅|
|4123|🟢|hi folks|greet|greet|100.0%|✅|
|4124|🟢|how have you been|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|4125|🟢|do you have an event in Berlin|ask_which_events|ask_which_events|100.0%|✅|
|4126|🟢|rasa core vs rasa nlu|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|4127|🟢|Why should I contribute to your code?|ask_why_contribute|ask_why_contribute|100.0%|✅|
|4128|🟢|thanks but no thanks|deny|deny|100.0%|✅|
|4129|🟢|rasa php|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|4130|🟢|How old are you?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|4131|🟢|how old are you|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|4132|🟢|how old are you?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|4133|🟢|what is the best place to get started?|how_to_get_started|how_to_get_started|100.0%|✅|
|4134|🟢|I'm interested in server installation|enter_data|enter_data|100.0%|✅|
|4135|🟢|i want to speak to a manager|human_handoff|human_handoff|100.0%|✅|
|4136|🟢|I am using it|affirm|affirm|100.0%|✅|
|4137|🟢|I am seeing an error|need_help_broad|need_help_broad|100.0%|✅|
|4138|🟢|What do you do at Rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4139|🟢|whats new|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|4140|🟢|hiihihi|greet|greet|100.0%|✅|
|4141|🟢|how can I improve Rasa|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4142|🟢|I have error during the installation|need_help_broad|need_help_broad|100.0%|✅|
|4143|🟢|sup|greet|greet|100.0%|✅|
|4144|🟢|why is rasa so good?|why_rasa|why_rasa|100.0%|✅|
|4145|🟢|how nice!|affirm|affirm|100.0%|✅|
|4146|🟢|i am so worry|react_negative|react_negative|100.0%|✅|
|4147|🟢|Guten Morgen|greet|greet|100.0%|✅|
|4148|🟢|Please schedule a sales call|contact_sales|contact_sales|100.0%|✅|
|4149|🟢|Get started|how_to_get_started|how_to_get_started|100.0%|✅|
|4150|🟢|I'm sure I will!|affirm|affirm|100.0%|✅|
|4151|🟢|try out online|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|4152|🟢|what is EE?|faq/ee|faq/ee|100.0%|✅|
|4153|🟢|DialogFlow|switch|switch|100.0%|✅|
|4154|🟢|hello sweet boy|greet|greet|100.0%|✅|
|4155|🟢|a bot|enter_data|enter_data|100.0%|✅|
|4156|🟢|how can i install python|install_rasa|install_rasa|100.0%|✅|
|4157|🟢|my computer|enter_data|enter_data|100.0%|✅|
|4158|🟢|no i won't|deny|deny|100.0%|✅|
|4159|🟢|nope. i am good|deny|deny|100.0%|✅|
|4160|🟢|anything els|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|4161|🟢|Could you please list the kinds of events that you have?|ask_which_events|ask_which_events|100.0%|✅|
|4162|🟢|user can communicate with the bot in chinese|enter_data|enter_data|100.0%|✅|
|4163|🟢|Where did you grow up?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|4164|🟢|where did you grow up?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|4165|🟢|how much is it|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|4166|🟢|greetings|greet|greet|100.0%|✅|
|4167|🟢|Can you shw me some information about intallation?|install_rasa|install_rasa|100.0%|✅|
|4168|🟢|How do I post my question on the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4169|🟢|Do you  help to  integrate Facebook|faq/channels|faq/channels|100.0%|✅|
|4170|🟢|Yes, I want to know more about NLU|faq/nlu|faq/nlu|100.0%|✅|
|4171|🟢|what is X ?|faq/rasax|faq/rasax|100.0%|✅|
|4172|🟢|hey let's talk|greet|greet|100.0%|✅|
|4173|🟢|hey, let's talk|greet|greet|100.0%|✅|
|4174|🟢|why is rasa good|why_rasa|why_rasa|100.0%|✅|
|4175|🟢|bye was nice talking to you|bye|bye|100.0%|✅|
|4176|🟢|in what ways can I help out?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4177|🟢|how can I train data|technical_question|technical_question|100.0%|✅|
|4178|🟢|i am switching from luis|switch|switch|100.0%|✅|
|4179|🟢|I want to change from dialogflow to rasa|switch|switch|100.0%|✅|
|4180|🟢|compnnent of rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|4181|🟢|how does rasa playground relate to rasa core|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|4182|🟢|Please, I need Rasa Core.|install_rasa|install_rasa|100.0%|✅|
|4183|🟢|rasa os|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4184|🟢|You're really cool|react_positive|react_positive|100.0%|✅|
|4185|🟢|why to use RASA|why_rasa|why_rasa|100.0%|✅|
|4186|🟢|Rasa X features|faq/rasax|faq/rasax|100.0%|✅|
|4187|🟢|switching from DialogFlow|switch|switch|100.0%|✅|
|4188|🟢|In what way can I contribute.|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4189|🟢|language = italian|enter_data|enter_data|100.0%|✅|
|4190|🟢|language: italian|enter_data|enter_data|100.0%|✅|
|4191|🟢|can I migrate to rasa from another tool?|switch|switch|100.0%|✅|
|4192|🟢|different parts of Rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|4193|🟢|where to start?|how_to_get_started|how_to_get_started|100.0%|✅|
|4194|🟢|what i have to do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|4195|🟢|Rasa Is?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4196|🟢|What should I do fo this project?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4197|🟢|how to install rasa?|install_rasa|install_rasa|100.0%|✅|
|4198|🟢|greet|greet|greet|100.0%|✅|
|4199|🟢|nlu part|enter_data|enter_data|100.0%|✅|
|4200|🟢|oh awesome!|affirm|affirm|100.0%|✅|
|4201|🟢|funny bot|enter_data|enter_data|100.0%|✅|
|4202|🟢|talking to a bot is stupid|human_handoff|human_handoff|100.0%|✅|
|4203|🟢|What do you do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|4204|🟢|what do you do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|4205|🟢|what do you do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|4206|🟢|How to install rasa X?|install_rasa|install_rasa|100.0%|✅|
|4207|🟢|yes, I have a question|need_help_broad|need_help_broad|100.0%|✅|
|4208|🟢|how to learn rasa core|how_to_get_started|how_to_get_started|100.0%|✅|
|4209|🟢|Why should I contribute|ask_why_contribute|ask_why_contribute|100.0%|✅|
|4210|🟢|i want to talk to someone who is smarter than you|human_handoff|human_handoff|100.0%|✅|
|4211|🟢|Is it better to use rasa or luis?|why_rasa|why_rasa|100.0%|✅|
|4212|🟢|how to integrate RASA with customer data?|technical_question|technical_question|100.0%|✅|
|4213|🟢|where do i download rasa|install_rasa|install_rasa|100.0%|✅|
|4214|🟢|How to migrate a bot from DialogFlow to Rasa?|switch|switch|100.0%|✅|
|4215|🟢|what's the purpose of Rasa X|faq/rasax|faq/rasax|100.0%|✅|
|4216|🟢|bonjour|greet|greet|100.0%|✅|
|4217|🟢|hi. Sara what do you do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|4218|🟢|tell me about Rasa Core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|4219|🟢|what should I do when I want to use a binary slot|technical_question|technical_question|100.0%|✅|
|4220|🟢|how to use|how_to_get_started|how_to_get_started|100.0%|✅|
|4221|🟢|Where should I ask my question on the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4222|🟢|now what?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|4223|🟢|Why aid your opportunity?|ask_why_contribute|ask_why_contribute|100.0%|✅|
|4224|🟢|Yes, I do need Rasa Stack.|install_rasa|install_rasa|100.0%|✅|
|4225|🟢|Hey I want to ask a question in the forum|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4226|🟢|i need to speak to your sales team|contact_sales|contact_sales|100.0%|✅|
|4227|🟢|halloooo|greet|greet|100.0%|✅|
|4228|🟢|WHAT MESSAGING PORTALS DOES RASA SUPPORT?|faq/channels|faq/channels|100.0%|✅|
|4229|🟢|I wanna have a subscription for your product|contact_sales|contact_sales|100.0%|✅|
|4230|🟢|no sorry|deny|deny|100.0%|✅|
|4231|🟢|Can you brief me about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4232|🟢|Hieeeeeeeeeeeee|greet|greet|100.0%|✅|
|4233|🟢|rasa hello|greet|greet|100.0%|✅|
|4234|🟢|need to understand dialogue management|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|4235|🟢|You are rude|react_negative|react_negative|100.0%|✅|
|4236|🟢|ey boss|greet|greet|100.0%|✅|
|4237|🟢|i want to built a chatbot please help me|how_to_get_started|how_to_get_started|100.0%|✅|
|4238|🟢|I dont like to talk to a machine|human_handoff|human_handoff|100.0%|✅|
|4239|🟢|I am feeling bad|react_negative|react_negative|100.0%|✅|
|4240|🟢|i don't know what i want|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|4241|🟢|What does Rasa cost?|faq/opensource_cost|faq/opensource_cost|100.0%|✅|
|4242|🟢|how do I access the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4243|🟢|why should I use Rasa|why_rasa|why_rasa|100.0%|✅|
|4244|🟢|I want to meet Rasa|ask_which_events|ask_which_events|100.0%|✅|
|4245|🟢|and you|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|4246|🟢|I will|affirm|affirm|100.0%|✅|
|4247|🟢|i got some error during installation|need_help_broad|need_help_broad|100.0%|✅|
|4248|🟢|whats rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4249|🟢|That's awesome.|react_positive|react_positive|100.0%|✅|
|4250|🟢|can I develop using java|faq/is_programming_required|faq/is_programming_required|100.0%|✅|
|4251|🟢|really|affirm|affirm|100.0%|✅|
|4252|🟢|sales team connection|contact_sales|contact_sales|100.0%|✅|
|4253|🟢|what are all the things you understand?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|4254|🟢|Thanks|thank|thank|100.0%|✅|
|4255|🟢|Thanks!|thank|thank|100.0%|✅|
|4256|🟢|I have a question for you|need_help_broad|need_help_broad|100.0%|✅|
|4257|🟢|i can migrate microsoft luis bot to raza?|switch|switch|100.0%|✅|
|4258|🟢|Show me learning resources about Rasa|how_to_get_started|how_to_get_started|100.0%|✅|
|4259|🟢|What are the two components that make up Rasa Open Source?|faq/rasa_components|faq/rasa_components|100.0%|✅|
|4260|🟢|I would like to know more about RASA NLU|faq/nlu|faq/nlu|100.0%|✅|
|4261|🟢|Where can I meet Rasas|ask_which_events|ask_which_events|100.0%|✅|
|4262|🟢|take care|bye|bye|100.0%|✅|
|4263|🟢|what version does python needs|faq/python_version|faq/python_version|100.0%|✅|
|4264|🟢|hello it is me again|greet|greet|100.0%|✅|
|4265|🟢|rasa can use which different messaging channels?|faq/channels|faq/channels|100.0%|✅|
|4266|🟢|can i just test features without having to deal with your predefined conversation|how_to_get_started|how_to_get_started|100.0%|✅|
|4267|🟢|how start|how_to_get_started|how_to_get_started|100.0%|✅|
|4268|🟢|I think you cant help me|canthelp|canthelp|100.0%|✅|
|4269|🟢|im migrating from dialogflow|switch|switch|100.0%|✅|
|4270|🟢|great lets do that|affirm|affirm|100.0%|✅|
|4271|🟢|I want to switch from dialog flow|switch|switch|100.0%|✅|
|4272|🟢|get me the sales team|contact_sales|contact_sales|100.0%|✅|
|4273|🟢|how enttity extrcation works|nlu_info|nlu_info|100.0%|✅|
|4274|🟢|i dont like bots|react_negative|react_negative|100.0%|✅|
|4275|🟢|tell me more about your company|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4276|🟢|Yes I want to switch from LUIS to rasa|switch|switch|100.0%|✅|
|4277|🟢|can someone call me please?|contact_sales|contact_sales|100.0%|✅|
|4278|🟢|Thank's!|thank|thank|100.0%|✅|
|4279|🟢|oki doki|affirm|affirm|100.0%|✅|
|4280|🟢|What's new in Rasa X compared to Rasa?|faq/differencerasarasax|faq/differencerasarasax|100.0%|✅|
|4281|🟢|how does Rasa Playground work?|faq/rasa_playground|faq/rasa_playground|100.0%|✅|
|4282|🟢|can you help me to build a bot|how_to_get_started|how_to_get_started|100.0%|✅|
|4283|🟢|are there ways I can contribute?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4284|🟢|how can I leave a query in the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4285|🟢|i want human :(|human_handoff|human_handoff|100.0%|✅|
|4286|🟢|hey there boy|greet|greet|100.0%|✅|
|4287|🟢|give me some information on nlu|faq/nlu|faq/nlu|100.0%|✅|
|4288|🟢|Why should I add to your code|ask_why_contribute|ask_why_contribute|100.0%|✅|
|4289|🟢|there is error|technical_question|technical_question|100.0%|✅|
|4290|🟢|nevermind.... you're not human ... I need to talk to a live person|human_handoff|human_handoff|100.0%|✅|
|4291|🟢|how does Rasa X work?|faq/rasax|faq/rasax|100.0%|✅|
|4292|🟢|I meant why you over competitors ?|why_rasa|why_rasa|100.0%|✅|
|4293|🟢|I currently use LUIS|switch|switch|100.0%|✅|
|4294|🟢|whats up|greet|greet|100.0%|✅|
|4295|🟢|no stop|deny|deny|100.0%|✅|
|4296|🟢|please tell steps for installing chatbot|install_rasa|install_rasa|100.0%|✅|
|4297|🟢|thx|thank|thank|100.0%|✅|
|4298|🟢|hi sara, i get the following error when trying to install rasa on my macbook|need_help_broad|need_help_broad|100.0%|✅|
|4299|🟢|ok i guess you can't help me|canthelp|canthelp|100.0%|✅|
|4300|🟢|What's the next rasa event|ask_which_events|ask_which_events|100.0%|✅|
|4301|🟢|:D|react_positive|react_positive|100.0%|✅|
|4302|🟢|sorry not right now|deny|deny|100.0%|✅|
|4303|🟢|helloooo|greet|greet|100.0%|✅|
|4304|🟢|can you explain rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4305|🟢|hm, i'd like that|affirm|affirm|100.0%|✅|
|4306|🟢|is Rasa X separate from Rasa?|faq/rasax|faq/rasax|100.0%|✅|
|4307|🟢|I use DialogFlow|switch|switch|100.0%|✅|
|4308|🟢|what's rasa x|faq/rasax|faq/rasax|100.0%|✅|
|4309|🟢|what's rasa core?|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|4310|🟢|Is there a Rasa meetup|ask_which_events|ask_which_events|100.0%|✅|
|4311|🟢|get starte|how_to_get_started|how_to_get_started|100.0%|✅|
|4312|🟢|I get it|affirm|affirm|100.0%|✅|
|4313|🟢|demo bot source code|source_code|source_code|100.0%|✅|
|4314|🟢|Is there some way I can help improve your code?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4315|🟢|how to get the source code|source_code|source_code|100.0%|✅|
|4316|🟢|i wanna try rasa nlu|how_to_get_started|how_to_get_started|100.0%|✅|
|4317|🟢|Where do I post questions in the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4318|🟢|I have an inquiry for the forum|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4319|🟢|when you were bon|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|4320|🟢|thanks f|thank|thank|100.0%|✅|
|4321|🟢|Whats up|greet|greet|100.0%|✅|
|4322|🟢|Whats up?|greet|greet|100.0%|✅|
|4323|🟢|i want to extract predefined entity from user query|technical_question|technical_question|100.0%|✅|
|4324|🟢|How do I download rasa ?|install_rasa|install_rasa|100.0%|✅|
|4325|🟢|What's difference between these?|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|4326|🟢|ARE YOU SPANISH|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|4327|🟢|What do I Need for Rasa implementation?|how_to_get_started|how_to_get_started|100.0%|✅|
|4328|🟢|I do not know yet|enter_data|enter_data|100.0%|✅|
|4329|🟢|how can i start|how_to_get_started|how_to_get_started|100.0%|✅|
|4330|🟢|is it hot ?|chitchat/ask_weather|chitchat/ask_weather|100.0%|✅|
|4331|🟢|I want to talk to someone about your pricing system|contact_sales|contact_sales|100.0%|✅|
|4332|🟢|I want to know about rsa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4333|🟢|pipeline recommendation|pipeline_recommendation|pipeline_recommendation|100.0%|✅|
|4334|🟢|this is leading to nothing|canthelp|canthelp|100.0%|✅|
|4335|🟢|Only NLU|enter_data|enter_data|100.0%|✅|
|4336|🟢|How do I create a thread on the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4337|🟢|I am getting some error|technical_question|technical_question|100.0%|✅|
|4338|🟢|What even is coming up next and when is it please?|ask_which_events|ask_which_events|100.0%|✅|
|4339|🟢|How can I develop a bot?|how_to_get_started|how_to_get_started|100.0%|✅|
|4340|🟢|Surely you're not so smart lik i thought|react_negative|react_negative|100.0%|✅|
|4341|🟢|Are you ok?|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|4342|🟢|are you ok|chitchat/ask_howdoing|chitchat/ask_howdoing|100.0%|✅|
|4343|🟢|how to export dialogflow data to rasa|switch|switch|100.0%|✅|
|4344|🟢|I don’t understand how you handle entity recognition at Rasa|nlu_info|nlu_info|100.0%|✅|
|4345|🟢|what is the different|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|100.0%|✅|
|4346|🟢|thnks|thank|thank|100.0%|✅|
|4347|🟢|can you explain rasa core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|4348|🟢|Is there some way I can help?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4349|🟢|do you have tutorials about core|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|4350|🟢|bot framework|switch|switch|100.0%|✅|
|4351|🟢|amazing, thanks|thank|thank|100.0%|✅|
|4352|🟢|What does Rasa make?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4353|🟢|how can i contribute to it|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4354|🟢|Is rasa better than google dialogflow?|why_rasa|why_rasa|100.0%|✅|
|4355|🟢|i will!|affirm|affirm|100.0%|✅|
|4356|🟢|error message when installing rasa|need_help_broad|need_help_broad|100.0%|✅|
|4357|🟢|Is there any way I can contribute?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4358|🟢|i need more info for rasa core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|4359|🟢|no i get a error while installing|need_help_broad|need_help_broad|100.0%|✅|
|4360|🟢|A customer service bot|enter_data|enter_data|100.0%|✅|
|4361|🟢|You have rasa meetups?|ask_which_events|ask_which_events|100.0%|✅|
|4362|🟢|language = portuguese|enter_data|enter_data|100.0%|✅|
|4363|🟢|language: portuguese|enter_data|enter_data|100.0%|✅|
|4364|🟢|Sure, give me the basics|how_to_get_started|how_to_get_started|100.0%|✅|
|4365|🟢|i want that|affirm|affirm|100.0%|✅|
|4366|🟢|Okay who am I?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|4367|🟢|lots of errors|need_help_broad|need_help_broad|100.0%|✅|
|4368|🟢|how do I install it?|install_rasa|install_rasa|100.0%|✅|
|4369|🟢|whats rasax|faq/rasax|faq/rasax|100.0%|✅|
|4370|🟢|i'm afraid not|deny|deny|100.0%|✅|
|4371|🟢|Do you know who I am?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|4372|🟢|Do you know who am I?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|4373|🟢|Who could I be?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|4374|🟢|parts of rasa|faq/rasa_components|faq/rasa_components|100.0%|✅|
|4375|🟢|I want to switch from dialogflow to rasa|switch|switch|100.0%|✅|
|4376|🟢|What do you do as a company?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4377|🟢|i am Karen Mease|greet|greet|100.0%|✅|
|4378|🟢|can i switch from luis to rasa?|switch|switch|100.0%|✅|
|4379|🟢|i am stuck|need_help_broad|need_help_broad|100.0%|✅|
|4380|🟢|What's rasa?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4381|🟢|Thank you in advance for suggesting I install Rasa NLU.|install_rasa|install_rasa|100.0%|✅|
|4382|🟢|In what manner can one contribute?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4383|🟢|who are u|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|4384|🟢|i want to build a bot about me|enter_data|enter_data|100.0%|✅|
|4385|🟢|quit|canthelp|canthelp|100.0%|✅|
|4386|🟢|What is the benefit of contributing to your code|ask_why_contribute|ask_why_contribute|100.0%|✅|
|4387|🟢|good bye rasa bot!|bye|bye|100.0%|✅|
|4388|🟢|how to build a pipelin|pipeline_recommendation|pipeline_recommendation|100.0%|✅|
|4389|🟢|i require more nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|100.0%|✅|
|4390|🟢|recognition|nlu_info|nlu_info|100.0%|✅|
|4391|🟢|thanks|thank|thank|100.0%|✅|
|4392|🟢|thanks!|thank|thank|100.0%|✅|
|4393|🟢|What city are you in?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|4394|🟢|wasssup|greet|greet|100.0%|✅|
|4395|🟢|wasssup!|greet|greet|100.0%|✅|
|4396|🟢|thank you anyways|thank|thank|100.0%|✅|
|4397|🟢|I want to help the cause.|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4398|🟢|I am using dialogflow - how can I migrate|switch|switch|100.0%|✅|
|4399|🟢|are you bilingual?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|4400|🟢|i use chinese|enter_data|enter_data|100.0%|✅|
|4401|🟢|where to train intents in rasa?|nlu_info|nlu_info|100.0%|✅|
|4402|🟢|i want to talk to someone at rasa|human_handoff|human_handoff|100.0%|✅|
|4403|🟢|i need smalltalk.md file|source_code|source_code|100.0%|✅|
|4404|🟢|I want to convert my dialog flow bot to rasa|switch|switch|100.0%|✅|
|4405|🟢|migrate to rasa|switch|switch|100.0%|✅|
|4406|🟢|how can I post a question in the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4407|🟢|switch from dilogueflow|switch|switch|100.0%|✅|
|4408|🟢|Is there a way I can assist?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4409|🟢|Where did you originate?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|100.0%|✅|
|4410|🟢|How were you set up?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|100.0%|✅|
|4411|🟢|What are you able to do?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|4412|🟢|user can talk to my bot in chinese|enter_data|enter_data|100.0%|✅|
|4413|🟢|i want to use pip to install sara|install_rasa|install_rasa|100.0%|✅|
|4414|🟢|how can i restart conversation on chatbot|technical_question|technical_question|100.0%|✅|
|4415|🟢|Rasa playgrounds isn't working for me|broken|broken|100.0%|✅|
|4416|🟢|DOES RASA SUPPORT MESSENGER?|faq/channels|faq/channels|100.0%|✅|
|4417|🟢|where do i find instructions|how_to_get_started|how_to_get_started|100.0%|✅|
|4418|🟢|like u|react_positive|react_positive|100.0%|✅|
|4419|🟢|How can be of assistance?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4420|🟢|Where should I go for dinner?|chitchat/ask_restaurant|chitchat/ask_restaurant|100.0%|✅|
|4421|🟢|migrate to rasa from another tool|switch|switch|100.0%|✅|
|4422|🟢|hm i don't think you can do what i want|canthelp|canthelp|100.0%|✅|
|4423|🟢|how can i contribute to Rasa|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4424|🟢|get the latest news from Rasa|signup_newsletter|signup_newsletter|100.0%|✅|
|4425|🟢|awesome|affirm|affirm|100.0%|✅|
|4426|🟢|awesome!|affirm|affirm|100.0%|✅|
|4427|🟢|are there some core tutorials i could look at|faq/tutorial_dialogue_management|faq/tutorial_dialogue_management|100.0%|✅|
|4428|🟢|How do I identify myself?|chitchat/ask_whoami|chitchat/ask_whoami|100.0%|✅|
|4429|🟢|how do you switch from dialogflow|switch|switch|100.0%|✅|
|4430|🟢|absolutely not|deny|deny|100.0%|✅|
|4431|🟢|i need more nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|100.0%|✅|
|4432|🟢|how can i build a chatbot|how_to_get_started|how_to_get_started|100.0%|✅|
|4433|🟢|I want to offer assistance|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4434|🟢|can you help me with installation of rasa nlu and train my first bot|install_rasa|install_rasa|100.0%|✅|
|4435|🟢|I want to see a demonstration of rasa enterprise|book_demo|book_demo|100.0%|✅|
|4436|🟢|explain that|explain|explain|100.0%|✅|
|4437|🟢|nlu|enter_data|enter_data|100.0%|✅|
|4438|🟢|I'm ready to help.|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4439|🟢|Hellllooooooo|greet|greet|100.0%|✅|
|4440|🟢|I wonder if the forum can answer my question.|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4441|🟢|great thanks|thank|thank|100.0%|✅|
|4442|🟢|Is the forum the right place to ask questions?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4443|🟢|I am a driver|enter_data|enter_data|100.0%|✅|
|4444|🟢|Which events are available?|ask_which_events|ask_which_events|100.0%|✅|
|4445|🟢|What can you tell me?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|4446|🟢|what can you tell me|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|4447|🟢|Why should I devote time to your code|ask_why_contribute|ask_why_contribute|100.0%|✅|
|4448|🟢|why should I switch to rasa from dialogflow|why_rasa|why_rasa|100.0%|✅|
|4449|🟢|what sets rasa apart?|why_rasa|why_rasa|100.0%|✅|
|4450|🟢|I have a question about Rasa NLU|need_help_broad|need_help_broad|100.0%|✅|
|4451|🟢|what about signing up for the newsletter?|signup_newsletter|signup_newsletter|100.0%|✅|
|4452|🟢|How do I find the forum?|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4453|🟢|can you tell me about rasa x ee?|faq/ee|faq/ee|100.0%|✅|
|4454|🟢|good moring|greet|greet|100.0%|✅|
|4455|🟢|it's pretty cool|react_positive|react_positive|100.0%|✅|
|4456|🟢|a customer service support system|enter_data|enter_data|100.0%|✅|
|4457|🟢|how do I contribute?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4458|🟢|What could I do to be helpful?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4459|🟢|alright, cool|affirm|affirm|100.0%|✅|
|4460|🟢|connect me to a real person|human_handoff|human_handoff|100.0%|✅|
|4461|🟢|Is there a live demo of rasa somewhere ?|book_demo|book_demo|100.0%|✅|
|4462|🟢|what is your birthday?|chitchat/ask_howold|chitchat/ask_howold|100.0%|✅|
|4463|🟢|this conversation is not really helpful|canthelp|canthelp|100.0%|✅|
|4464|🟢|i have an error on install|need_help_broad|need_help_broad|100.0%|✅|
|4465|🟢|what is you name|chitchat/ask_whoisit|chitchat/ask_whoisit|100.0%|✅|
|4466|🟢|Whats up my bot|greet|greet|100.0%|✅|
|4467|🟢|that is cool|affirm|affirm|100.0%|✅|
|4468|🟢|I want to speak with sales|contact_sales|contact_sales|100.0%|✅|
|4469|🟢|hèhè|react_positive|react_positive|100.0%|✅|
|4470|🟢|where is your source code|source_code|source_code|100.0%|✅|
|4471|🟢|give me a reason to use Rasa|why_rasa|why_rasa|100.0%|✅|
|4472|🟢|I need to ask the forum something|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4473|🟢|Why help Rasa's organization?|ask_why_contribute|ask_why_contribute|100.0%|✅|
|4474|🟢|between 100 to 200.000|enter_data|enter_data|100.0%|✅|
|4475|🟢|DOES RASA SUPPORT SMS?|faq/channels|faq/channels|100.0%|✅|
|4476|🟢|Awesome!|affirm|affirm|100.0%|✅|
|4477|🟢|i am very happy with your response|react_positive|react_positive|100.0%|✅|
|4478|🟢|how to you exit the server|technical_question|technical_question|100.0%|✅|
|4479|🟢|tell me bout rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|100.0%|✅|
|4480|🟢|you good|react_positive|react_positive|100.0%|✅|
|4481|🟢|get a subscription|signup_newsletter|signup_newsletter|100.0%|✅|
|4482|🟢|You are mad|react_negative|react_negative|100.0%|✅|
|4483|🟢|to make a subscribtion|signup_newsletter|signup_newsletter|100.0%|✅|
|4484|🟢|Help me to find the forum.|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4485|🟢|I need to ask something of the forum|ask_question_in_forum|ask_question_in_forum|100.0%|✅|
|4486|🟢|thanks a bunch for everything|thank|thank|100.0%|✅|
|4487|🟢|About Core|faq/dialogue_management|faq/dialogue_management|100.0%|✅|
|4488|🟢|bad boy|react_negative|react_negative|100.0%|✅|
|4489|🟢|not going well at all|deny|deny|100.0%|✅|
|4490|🟢|a cool bot|enter_data|enter_data|100.0%|✅|
|4491|🟢|need more data for nlu|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|100.0%|✅|
|4492|🟢|you know French|chitchat/ask_languagesbot|chitchat/ask_languagesbot|100.0%|✅|
|4493|🟢|what is a intent?|nlu_info|nlu_info|100.0%|✅|
|4494|🟢|im stuck|need_help_broad|need_help_broad|100.0%|✅|
|4495|🟢|Great, thanks|thank|thank|100.0%|✅|
|4496|🟢|What ways are there to contribute?|ask_how_contribute|ask_how_contribute|100.0%|✅|
|4497|🟢|language = spanish|enter_data|enter_data|100.0%|✅|
|4498|🟢|language: spanish|enter_data|enter_data|100.0%|✅|
|4499|🟢|what is your source code|source_code|source_code|100.0%|✅|
|4500|🟢|rasa is awesome|react_positive|react_positive|100.0%|✅|
|4501|🟢|what can I do with Sara?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|100.0%|✅|
|4502|🟢|How do I download RASA|install_rasa|install_rasa|100.0%|✅|
|4503|🟢|What are the events available?|ask_which_events|ask_which_events|100.0%|✅|
|4504|🟢|i want to make intelligence chatbot|how_to_get_started|how_to_get_started|100.0%|✅|
|4505|🟢|i have to less nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|100.0%|✅|
|4506|🟢|how many forum members do you have|faq/community_size|faq/community_size|99.9%|✅|
|4507|🟢|i want to know more about nlu and why is it better than watson or luis|why_rasa|why_rasa|99.9%|✅|
|4508|🟢|Where do I post my question?|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|4509|🟢|i need help setting up|install_rasa|install_rasa|99.9%|✅|
|4510|🟢|I would like to have a demo scheduled|book_demo|book_demo|99.9%|✅|
|4511|🟢|can you help me build a chatbot|how_to_get_started|how_to_get_started|99.9%|✅|
|4512|🟢|do you know chinese|chitchat/ask_languagesbot|chitchat/ask_languagesbot|99.9%|✅|
|4513|🟢|Where can i find the source code|source_code|source_code|99.9%|✅|
|4514|🟢|NLU data  generation|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.9%|✅|
|4515|🟢|why to use rasa over other available platform|why_rasa|why_rasa|99.9%|✅|
|4516|🟢|Why should I contribute to Rasa|ask_why_contribute|ask_why_contribute|99.9%|✅|
|4517|🟢|i am feeling happy|react_positive|react_positive|99.9%|✅|
|4518|🟢|helleo|greet|greet|99.9%|✅|
|4519|🟢|your code|source_code|source_code|99.9%|✅|
|4520|🟢|How many languages do you have knowledge of?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|99.9%|✅|
|4521|🟢|what are you made of|chitchat/ask_howbuilt|chitchat/ask_howbuilt|99.9%|✅|
|4522|🟢|Migration please|switch|switch|99.9%|✅|
|4523|🟢|I want to ask the forum for an answer|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|4524|🟢|are you real|chitchat/ask_isbot|chitchat/ask_isbot|99.9%|✅|
|4525|🟢|That would be great|affirm|affirm|99.9%|✅|
|4526|🟢|switch to rasa from another platform|switch|switch|99.9%|✅|
|4527|🟢|can you tell me what my identity is?|chitchat/ask_whoami|chitchat/ask_whoami|99.9%|✅|
|4528|🟢|restart this conversation|restart|restart|99.9%|✅|
|4529|🟢|thanks this is great news|thank|thank|99.9%|✅|
|4530|🟢|noooooooooooooooooooooooooooooooooooooooo|deny|deny|99.9%|✅|
|4531|🟢|want to build a chatbot|faq/rasa_components|faq/rasa_components|99.9%|✅|
|4532|🟢|cool thanks|thank|thank|99.9%|✅|
|4533|🟢|cool, thanks|thank|thank|99.9%|✅|
|4534|🟢|how can i get the code for the demo bot?|source_code|source_code|99.9%|✅|
|4535|🟢|I want to get help in the forum|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|4536|🟢|What do you speak?|chitchat/ask_languagesbot|chitchat/ask_languagesbot|99.9%|✅|
|4537|🟢|rasa core|enter_data|enter_data|99.9%|✅|
|4538|🟢|that does not help|canthelp|canthelp|99.9%|✅|
|4539|🟢|Good Morning|greet|greet|99.9%|✅|
|4540|🟢|i want to know how can buld my own bot|how_to_get_started|how_to_get_started|99.9%|✅|
|4541|🟢|how can i use you|chitchat/ask_whatspossible|chitchat/ask_whatspossible|99.9%|✅|
|4542|🟢|I want to build a sales bot|enter_data|enter_data|99.9%|✅|
|4543|🟢|Not really|deny|deny|99.9%|✅|
|4544|🟢|I think it's broken|broken|broken|99.9%|✅|
|4545|🟢|please give me instructions for pip|enter_data|enter_data|99.9%|✅|
|4546|🟢|help me can you fix it|broken|broken|99.9%|✅|
|4547|🟢|can i see your code|source_code|source_code|99.9%|✅|
|4548|🟢|Why should I devote effort to working on your code|ask_why_contribute|ask_why_contribute|99.9%|✅|
|4549|🟢|where is the source code?|source_code|source_code|99.9%|✅|
|4550|🟢|why is rasa better?|why_rasa|why_rasa|99.9%|✅|
|4551|🟢|why migrate?|why_rasa|why_rasa|99.9%|✅|
|4552|🟢|i need the source code to this bot|source_code|source_code|99.9%|✅|
|4553|🟢|Cool. Thanks|thank|thank|99.9%|✅|
|4554|🟢|cool thank you|thank|thank|99.9%|✅|
|4555|🟢|how can I get help in the forum|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|4556|🟢|what I can call you|chitchat/ask_whoisit|chitchat/ask_whoisit|99.9%|✅|
|4557|🟢|Rasa X isn't working for me|broken|broken|99.9%|✅|
|4558|🟢|your name?|chitchat/ask_whoisit|chitchat/ask_whoisit|99.9%|✅|
|4559|🟢|try rasa online|faq/rasa_playground|faq/rasa_playground|99.9%|✅|
|4560|🟢|i want to switch from luis to rasa|switch|switch|99.9%|✅|
|4561|🟢|i want to try it online|faq/rasa_playground|faq/rasa_playground|99.9%|✅|
|4562|🟢|hi can you help e build a chatbot|how_to_get_started|how_to_get_started|99.9%|✅|
|4563|🟢|give me someone who can explain your business model|contact_sales|contact_sales|99.9%|✅|
|4564|🟢|yes with your source code|source_code|source_code|99.9%|✅|
|4565|🟢|Rasa core|enter_data|enter_data|99.9%|✅|
|4566|🟢|to the forum|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|4567|🟢|Although I understand your still in development, I feel a little bit disappointed.|react_negative|react_negative|99.9%|✅|
|4568|🟢|I'm a student|enter_data|enter_data|99.9%|✅|
|4569|🟢|i am sad about that|react_negative|react_negative|99.9%|✅|
|4570|🟢|purchase rasa enterprise|contact_sales|contact_sales|99.9%|✅|
|4571|🟢|are you okay|chitchat/ask_howdoing|chitchat/ask_howdoing|99.9%|✅|
|4572|🟢|Why be a part of your mission?|ask_why_contribute|ask_why_contribute|99.9%|✅|
|4573|🟢|that ok|affirm|affirm|99.9%|✅|
|4574|🟢|bots are bad|react_negative|react_negative|99.9%|✅|
|4575|🟢|dialogflow and implementation from scratch|switch|switch|99.9%|✅|
|4576|🟢|can i know your source code ?|source_code|source_code|99.9%|✅|
|4577|🟢|thankyou|thank|thank|99.9%|✅|
|4578|🟢|i want someone to call me|contact_sales|contact_sales|99.9%|✅|
|4579|🟢|I need someone in the forum to help me|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|4580|🟢|how to setup rasax on slack|faq/channels|faq/channels|99.9%|✅|
|4581|🟢|i need information from posters in the forum|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|4582|🟢|I need to get information from the forum|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|4583|🟢|who may i ?|chitchat/ask_whoami|chitchat/ask_whoami|99.9%|✅|
|4584|🟢|Can I help improve your code at all?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|4585|🟢|join that newsletter|signup_newsletter|signup_newsletter|99.9%|✅|
|4586|🟢|I would like to know more about your product|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|99.9%|✅|
|4587|🟢|thank you|thank|thank|99.9%|✅|
|4588|🟢|What and when is the next event?|ask_which_events|ask_which_events|99.9%|✅|
|4589|🟢|cool story bro|affirm|affirm|99.9%|✅|
|4590|🟢|NLU|enter_data|enter_data|99.9%|✅|
|4591|🟢|pipeline|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|4592|🟢|I use luis|switch|switch|99.9%|✅|
|4593|🟢|give me a reason to switch to Rasa from luis|why_rasa|why_rasa|99.9%|✅|
|4594|🟢|and your REST API doesn't work|technical_question|technical_question|99.9%|✅|
|4595|🟢|I don’t know which pipeline to use|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|4596|🟢|how many people are using Rasa|faq/community_size|faq/community_size|99.9%|✅|
|4597|🟢|Channels|faq/channels|faq/channels|99.9%|✅|
|4598|🟢|recommend pipeline|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|4599|🟢|i want to develop a chatbot|how_to_get_started|how_to_get_started|99.9%|✅|
|4600|🟢|i don't know|enter_data|enter_data|99.9%|✅|
|4601|🟢|how to migrate my bot to rasa|switch|switch|99.9%|✅|
|4602|🟢|what is core|faq/dialogue_management|faq/dialogue_management|99.9%|✅|
|4603|🟢|which python is rasa using?|faq/python_version|faq/python_version|99.9%|✅|
|4604|🟢|how do you restart a story?|technical_question|technical_question|99.9%|✅|
|4605|🟢|it won't train|broken|broken|99.9%|✅|
|4606|🟢|What does Rasa build?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|99.9%|✅|
|4607|🟢|Where can I find the forum|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|4608|🟢|who r u|chitchat/ask_whoisit|chitchat/ask_whoisit|99.9%|✅|
|4609|🟢|That tool here isnt good|react_negative|react_negative|99.9%|✅|
|4610|🟢|just Rasa NLU|enter_data|enter_data|99.9%|✅|
|4611|🟢|I want to move from [LUIS.ai](current_api) to Rasa|switch|switch|99.9%|✅|
|4612|🟢|Why do I want to help with your code|ask_why_contribute|ask_why_contribute|99.9%|✅|
|4613|🟢|Great|affirm|affirm|99.9%|✅|
|4614|🟢|i  am stuck with an erorr|need_help_broad|need_help_broad|99.9%|✅|
|4615|🟢|DOES RASA SUPPORT THE WHATS APP?|faq/channels|faq/channels|99.9%|✅|
|4616|🟢|Thank you|thank|thank|99.9%|✅|
|4617|🟢|restart ps|restart|restart|99.9%|✅|
|4618|🟢|Can I build a FAQ robot with Rasa?|how_to_get_started|how_to_get_started|99.9%|✅|
|4619|🟢|what are your features ?|faq/rasa_components|faq/rasa_components|99.9%|✅|
|4620|🟢|switching|switch|switch|99.9%|✅|
|4621|🟢|there is an issue during installation|need_help_broad|need_help_broad|99.9%|✅|
|4622|🟢|going super well|affirm|affirm|99.9%|✅|
|4623|🟢|how is rasa's NLU better than watson 's|why_rasa|why_rasa|99.9%|✅|
|4624|🟢|are you build with rasa ?|chitchat/ask_howbuilt|chitchat/ask_howbuilt|99.9%|✅|
|4625|🟢|so how does it all work?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|99.9%|✅|
|4626|🟢|thanks a lot|thank|thank|99.9%|✅|
|4627|🟢|that's not what i want|canthelp|canthelp|99.9%|✅|
|4628|🟢|stop go back|canthelp|canthelp|99.9%|✅|
|4629|🟢|i want to restart|restart|restart|99.9%|✅|
|4630|🟢|you cannot help me with what I want|canthelp|canthelp|99.9%|✅|
|4631|🟢|i don't want to run rasa, i want to restart it|technical_question|technical_question|99.9%|✅|
|4632|🟢|just gimme a call|contact_sales|contact_sales|99.9%|✅|
|4633|🟢|restart session pls|restart|restart|99.9%|✅|
|4634|🟢|why should I help?|ask_why_contribute|ask_why_contribute|99.9%|✅|
|4635|🟢|do u give me the code|source_code|source_code|99.9%|✅|
|4636|🟢|I would like to know about rasa|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|99.9%|✅|
|4637|🟢|How can I help with the code?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|4638|🟢|you can't help me|canthelp|canthelp|99.9%|✅|
|4639|🟢|noooooooooo|deny|deny|99.9%|✅|
|4640|🟢|How can I add code to Rasa|ask_how_contribute|ask_how_contribute|99.9%|✅|
|4641|🟢|can you elaborate|explain|explain|99.9%|✅|
|4642|🟢|how to improve Rasa|ask_how_contribute|ask_how_contribute|99.9%|✅|
|4643|🟢|Good mourning|greet|greet|99.9%|✅|
|4644|🟢|How can I contribute to your code|ask_how_contribute|ask_how_contribute|99.9%|✅|
|4645|🟢|are there simpler ways to create nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.9%|✅|
|4646|🟢|bookin|book_demo|book_demo|99.9%|✅|
|4647|🟢|Where can I find your source code?|source_code|source_code|99.9%|✅|
|4648|🟢|perfect thank you|thank|thank|99.9%|✅|
|4649|🟢|thank u|thank|thank|99.9%|✅|
|4650|🟢|Thanks for that|thank|thank|99.9%|✅|
|4651|🟢|it's not working|broken|broken|99.9%|✅|
|4652|🟢|Thanks bot|thank|thank|99.9%|✅|
|4653|🟢|hey can you provide me the code of yours|source_code|source_code|99.9%|✅|
|4654|🟢|today was a nice day|react_positive|react_positive|99.9%|✅|
|4655|🟢|I'm getting an error while installing Rasa|need_help_broad|need_help_broad|99.9%|✅|
|4656|🟢|can you help me build my bot?|how_to_get_started|how_to_get_started|99.9%|✅|
|4657|🟢|I'm not going to give it to you|deny|deny|99.9%|✅|
|4658|🟢|your code please|source_code|source_code|99.9%|✅|
|4659|🟢|hey, you promised to contact me, but nobody did, I really need to finish that car insurance bot!!!!|canthelp|canthelp|99.9%|✅|
|4660|🟢|a little|affirm|affirm|99.9%|✅|
|4661|🟢|why people go for Rasa chatbot?|why_rasa|why_rasa|99.9%|✅|
|4662|🟢|it's not training|broken|broken|99.9%|✅|
|4663|🟢|i'd like to talk to a sales person|contact_sales|contact_sales|99.9%|✅|
|4664|🟢|I want to build a cool bot|enter_data|enter_data|99.9%|✅|
|4665|🟢|Why contribute to Rasa?|ask_why_contribute|ask_why_contribute|99.9%|✅|
|4666|🟢|hi can you speak ?|greet|greet|99.9%|✅|
|4667|🟢|Will the forum take my question?|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|4668|🟢|i want to buy the enterprise edition|contact_sales|contact_sales|99.9%|✅|
|4669|🟢|not right now|deny|deny|99.9%|✅|
|4670|🟢|what's your source code?|source_code|source_code|99.9%|✅|
|4671|🟢|Thank you so much|thank|thank|99.9%|✅|
|4672|🟢|it's broken|broken|broken|99.9%|✅|
|4673|🟢|great|affirm|affirm|99.9%|✅|
|4674|🟢|great!|affirm|affirm|99.9%|✅|
|4675|🟢|that sounds fine|affirm|affirm|99.9%|✅|
|4676|🟢|how to build a pipeline for the bot|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|4677|🟢|hindi|enter_data|enter_data|99.9%|✅|
|4678|🟢|bot?|chitchat/ask_isbot|chitchat/ask_isbot|99.9%|✅|
|4679|🟢|I dont want to tell|deny|deny|99.9%|✅|
|4680|🟢|How does one go about making their contribution?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|4681|🟢|Bom dia|greet|greet|99.9%|✅|
|4682|🟢|i need to know how i can book support|contact_sales|contact_sales|99.9%|✅|
|4683|🟢|amounts|enter_data|enter_data|99.9%|✅|
|4684|🟢|what are the channels Rasa NLU supports|faq/channels|faq/channels|99.9%|✅|
|4685|🟢|can you help me with installation|install_rasa|install_rasa|99.9%|✅|
|4686|🟢|are there different packages customers can book?|contact_sales|contact_sales|99.9%|✅|
|4687|🟢|rasa init error|need_help_broad|need_help_broad|99.9%|✅|
|4688|🟢|what ui can I use|faq/channels|faq/channels|99.9%|✅|
|4689|🟢|i am stuck with error|need_help_broad|need_help_broad|99.9%|✅|
|4690|🟢|i m stuck while importing data|need_help_broad|need_help_broad|99.9%|✅|
|4691|🟢|are there also humans working for your company?|human_handoff|human_handoff|99.9%|✅|
|4692|🟢|you can't help me with what i need|canthelp|canthelp|99.9%|✅|
|4693|🟢|HOW CAN i connect to rasa|how_to_get_started|how_to_get_started|99.9%|✅|
|4694|🟢|do you have human support ?|human_handoff|human_handoff|99.9%|✅|
|4695|🟢|can i look at your source code|source_code|source_code|99.9%|✅|
|4696|🟢|How did rasa works?|technical_question|technical_question|99.9%|✅|
|4697|🟢|What ways can one make a contribution?|ask_how_contribute|ask_how_contribute|99.9%|✅|
|4698|🟢|its an german bot|enter_data|enter_data|99.9%|✅|
|4699|🟢|This is bad|react_negative|react_negative|99.9%|✅|
|4700|🟢|a pizza bot|enter_data|enter_data|99.9%|✅|
|4701|🟢|hey, i said restart|restart|restart|99.9%|✅|
|4702|🟢|you are cool|react_positive|react_positive|99.9%|✅|
|4703|🟢|Rasa X|enter_data|enter_data|99.9%|✅|
|4704|🟢|Can I use your open source code on my website?|faq/channels|faq/channels|99.9%|✅|
|4705|🟢|cheers|thank|thank|99.9%|✅|
|4706|🟢|how to work with nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.9%|✅|
|4707|🟢|you make me sad|react_negative|react_negative|99.9%|✅|
|4708|🟢|you are bad bot|react_negative|react_negative|99.9%|✅|
|4709|🟢|Please restart this chat/|restart|restart|99.9%|✅|
|4710|🟢|ok send me to the forum|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|4711|🟢|I have a question about the functioning of the device|need_help_broad|need_help_broad|99.9%|✅|
|4712|🟢|I am stuck with fallback|need_help_broad|need_help_broad|99.9%|✅|
|4713|🟢|what pipeline should I start with?|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|4714|🟢|recommend me some nlu tools|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.9%|✅|
|4715|🟢|danke|thank|thank|99.9%|✅|
|4716|🟢|I want to make a forum post.|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|4717|🟢|u broke my heart|react_negative|react_negative|99.9%|✅|
|4718|🟢|You are quite bad|react_negative|react_negative|99.9%|✅|
|4719|🟢|Good morning|greet|greet|99.9%|✅|
|4720|🟢|Where do I ask questions?|ask_question_in_forum|ask_question_in_forum|99.9%|✅|
|4721|🟢|Can you get a human to assist me?|human_handoff|human_handoff|99.9%|✅|
|4722|🟢|I changed my mind. I want to accept it|affirm|affirm|99.9%|✅|
|4723|🟢|Tell me about the entity extraction|nlu_info|nlu_info|99.9%|✅|
|4724|🟢|how to using you|how_to_get_started|how_to_get_started|99.9%|✅|
|4725|🟢|tell me more about how to use rasa|how_to_get_started|how_to_get_started|99.9%|✅|
|4726|🟢|good morning|greet|greet|99.9%|✅|
|4727|🟢|help me build a bot|how_to_get_started|how_to_get_started|99.9%|✅|
|4728|🟢|should I better start with the tensorflow pipeline or spacy?|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|4729|🟢|just rasa nlu|enter_data|enter_data|99.9%|✅|
|4730|🟢|how does rasa x relate to rasa core|faq/rasax|faq/rasax|99.9%|✅|
|4731|🟢|how can I get nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.9%|✅|
|4732|🟢|not really|deny|deny|99.9%|✅|
|4733|🟢|that was shit, you're not helping|canthelp|canthelp|99.9%|✅|
|4734|🟢|what can you?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|99.9%|✅|
|4735|🟢|what you can|chitchat/ask_whatspossible|chitchat/ask_whatspossible|99.9%|✅|
|4736|🟢|id like to talk to someone who can explain me what i can do with rasa|contact_sales|contact_sales|99.9%|✅|
|4737|🟢|please restart the bot|restart|restart|99.9%|✅|
|4738|🟢|good evening|greet|greet|99.9%|✅|
|4739|🟢|I want to use Rasa Stack|install_rasa|install_rasa|99.9%|✅|
|4740|🟢|what up|greet|greet|99.9%|✅|
|4741|🟢|what I a good pipeline to start with?|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|4742|🟢|who are you|chitchat/ask_whoisit|chitchat/ask_whoisit|99.9%|✅|
|4743|🟢|who are you?|chitchat/ask_whoisit|chitchat/ask_whoisit|99.9%|✅|
|4744|🟢|I am responsible for our innovation department|enter_data|enter_data|99.9%|✅|
|4745|🟢|why help out?|ask_why_contribute|ask_why_contribute|99.9%|✅|
|4746|🟢|i want to use your source code|source_code|source_code|99.9%|✅|
|4747|🟢|where can i learn to build a chatbot|how_to_get_started|how_to_get_started|99.9%|✅|
|4748|🟢|thanks you|thank|thank|99.9%|✅|
|4749|🟢|Sure. I have a question for you|need_help_broad|need_help_broad|99.9%|✅|
|4750|🟢|Why should I help to improve Rasa|ask_why_contribute|ask_why_contribute|99.9%|✅|
|4751|🟢|you are bad|react_negative|react_negative|99.9%|✅|
|4752|🟢|how can I install rasa open source?|install_rasa|install_rasa|99.9%|✅|
|4753|🟢|what does the nlu pipeline do|technical_question|technical_question|99.9%|✅|
|4754|🟢|why offer my assistance?|ask_why_contribute|ask_why_contribute|99.9%|✅|
|4755|🟢|create chatbot steps|how_to_get_started|how_to_get_started|99.9%|✅|
|4756|🟢|ok sales|contact_sales|contact_sales|99.9%|✅|
|4757|🟢|Where should I eat?|chitchat/ask_restaurant|chitchat/ask_restaurant|99.9%|✅|
|4758|🟢|the playground is not training|broken|broken|99.9%|✅|
|4759|🟢|are there tools to create nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.9%|✅|
|4760|🟢|nlu pipeline|pipeline_recommendation|pipeline_recommendation|99.9%|✅|
|4761|🟢|tell me your name|chitchat/ask_whoisit|chitchat/ask_whoisit|99.9%|✅|
|4762|🟢|not yet|deny|deny|99.9%|✅|
|4763|🟢|Rasa installation error|need_help_broad|need_help_broad|99.9%|✅|
|4764|🟢|why do I need rasa|why_rasa|why_rasa|99.9%|✅|
|4765|🟢|is your code available?|source_code|source_code|99.9%|✅|
|4766|🟢|Can u tell where is ur code|source_code|source_code|99.9%|✅|
|4767|🟢|cheers bro|thank|thank|99.9%|✅|
|4768|🟢|i want a recommendation for an nlu data generation tool|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.9%|✅|
|4769|🟢|thanks for your information|thank|thank|99.8%|✅|
|4770|🟢|I wanna talk to your sales guy|contact_sales|contact_sales|99.8%|✅|
|4771|🟢|what pipeline is better?|pipeline_recommendation|pipeline_recommendation|99.8%|✅|
|4772|🟢|nothing else?|canthelp|canthelp|99.8%|✅|
|4773|🟢|what is different|faq/difference_dialogue_management_nlu|faq/difference_dialogue_management_nlu|99.8%|✅|
|4774|🟢|pip is fine|enter_data|enter_data|99.8%|✅|
|4775|🟢|and you call yourself bot company? pff|canthelp|canthelp|99.8%|✅|
|4776|🟢|I am stuck with action|need_help_broad|need_help_broad|99.8%|✅|
|4777|🟢|How do I post on the forum?|ask_question_in_forum|ask_question_in_forum|99.8%|✅|
|4778|🟢|How can I help you?|ask_how_contribute|ask_how_contribute|99.8%|✅|
|4779|🟢|Where can I post on the forum?|ask_question_in_forum|ask_question_in_forum|99.8%|✅|
|4780|🟢|What can I bring to help your code|ask_why_contribute|ask_why_contribute|99.8%|✅|
|4781|🟢|how does this work?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|99.8%|✅|
|4782|🟢|how does your pricing work?|contact_sales|contact_sales|99.8%|✅|
|4783|🟢|I like Rasa|react_positive|react_positive|99.8%|✅|
|4784|🟢|what's my identity?|chitchat/ask_whoami|chitchat/ask_whoami|99.8%|✅|
|4785|🟢|I don't wanna tell the name of my company|deny|deny|99.8%|✅|
|4786|🟢|I want to implement rasa|how_to_get_started|how_to_get_started|99.8%|✅|
|4787|🟢|spacy or tensorflow, what is better to start?|pipeline_recommendation|pipeline_recommendation|99.8%|✅|
|4788|🟢|where can I download the source code?|source_code|source_code|99.8%|✅|
|4789|🟢|Rasa Core|enter_data|enter_data|99.8%|✅|
|4790|🟢|help me please it's not working|broken|broken|99.8%|✅|
|4791|🟢|how to migrate to dialogueflow|switch|switch|99.8%|✅|
|4792|🟢|give me more details|explain|explain|99.8%|✅|
|4793|🟢|why do I get errors using rasa?|technical_question|technical_question|99.8%|✅|
|4794|🟢|i dont want to accept :P lol|deny|deny|99.8%|✅|
|4795|🟢|switch to rasa|switch|switch|99.8%|✅|
|4796|🟢|what do you mean|explain|explain|99.8%|✅|
|4797|🟢|i wanna build a bot|how_to_get_started|how_to_get_started|99.8%|✅|
|4798|🟢|when were you born?|chitchat/ask_howold|chitchat/ask_howold|99.8%|✅|
|4799|🟢|am struck with installation|install_rasa|install_rasa|99.8%|✅|
|4800|🟢|can you tell me what I am?|chitchat/ask_whoami|chitchat/ask_whoami|99.8%|✅|
|4801|🟢|I like to build a bot|how_to_get_started|how_to_get_started|99.8%|✅|
|4802|🟢|How to download?|how_to_get_started|how_to_get_started|99.8%|✅|
|4803|🟢|what are you good at?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|99.8%|✅|
|4804|🟢|why switch from dialogflow?|why_rasa|why_rasa|99.8%|✅|
|4805|🟢|can you point me to a good manual about Rasa|faq/tutorials|faq/tutorials|99.8%|✅|
|4806|🟢|I am stuck and I need help|need_help_broad|need_help_broad|99.8%|✅|
|4807|🟢|and why i should not use Tenserflow?|why_rasa|why_rasa|99.8%|✅|
|4808|🟢|i want to use nlu|how_to_get_started|how_to_get_started|99.8%|✅|
|4809|🟢|tell me what my identity is?|chitchat/ask_whoami|chitchat/ask_whoami|99.8%|✅|
|4810|🟢|can you hand a conversation over to a human?|human_handoff|human_handoff|99.8%|✅|
|4811|🟢|yep you can restart|restart|restart|99.8%|✅|
|4812|🟢|Why add to your business?|ask_why_contribute|ask_why_contribute|99.8%|✅|
|4813|🟢|what nlu pipeline would you recommend?|pipeline_recommendation|pipeline_recommendation|99.8%|✅|
|4814|🟢|Is there a way to contribute?|ask_how_contribute|ask_how_contribute|99.8%|✅|
|4815|🟢|How can I try out Rasa?|how_to_get_started|how_to_get_started|99.8%|✅|
|4816|🟢|where can i get data for the nlu|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.8%|✅|
|4817|🟢|github link?|source_code|source_code|99.8%|✅|
|4818|🟢|what is it for?|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|99.8%|✅|
|4819|🟢|sweet|react_positive|react_positive|99.8%|✅|
|4820|🟢|what's good|chitchat/ask_howdoing|chitchat/ask_howdoing|99.8%|✅|
|4821|🟢|still dont want to tell|deny|deny|99.8%|✅|
|4822|🟢|where can i find this code|source_code|source_code|99.8%|✅|
|4823|🟢|stop this conversation|canthelp|canthelp|99.8%|✅|
|4824|🟢|what do I get if I contribute|ask_why_contribute|ask_why_contribute|99.8%|✅|
|4825|🟢|which pipeline is better?|pipeline_recommendation|pipeline_recommendation|99.8%|✅|
|4826|🟢|rasa is not working|broken|broken|99.8%|✅|
|4827|🟢|For some reason, Rasa X never loads and I don't know why|broken|broken|99.8%|✅|
|4828|🟢|stop|canthelp|canthelp|99.8%|✅|
|4829|🟢|could you explain why you need that|explain|explain|99.8%|✅|
|4830|🟢|that's great|affirm|affirm|99.8%|✅|
|4831|🟢|i don not like this|deny|deny|99.8%|✅|
|4832|🟢|what pipeline should i use?|pipeline_recommendation|pipeline_recommendation|99.8%|✅|
|4833|🟢|can someone show me the forum?|ask_question_in_forum|ask_question_in_forum|99.8%|✅|
|4834|🟢|tell me who you are|chitchat/ask_whoisit|chitchat/ask_whoisit|99.8%|✅|
|4835|🟢|ok restart please|restart|restart|99.7%|✅|
|4836|🟢|what age are you|chitchat/ask_howold|chitchat/ask_howold|99.7%|✅|
|4837|🟢|Where is the forum|ask_question_in_forum|ask_question_in_forum|99.7%|✅|
|4838|🟢|can i try it out|how_to_get_started|how_to_get_started|99.7%|✅|
|4839|🟢|how do u work?|source_code|source_code|99.7%|✅|
|4840|🟢|how to install|install_rasa|install_rasa|99.7%|✅|
|4841|🟢|exit now|canthelp|canthelp|99.7%|✅|
|4842|🟢|start|how_to_get_started|how_to_get_started|99.7%|✅|
|4843|🟢|why would i use your product|why_rasa|why_rasa|99.7%|✅|
|4844|🟢|what about your day|chitchat/ask_howdoing|chitchat/ask_howdoing|99.7%|✅|
|4845|🟢|how much money|enter_data|enter_data|99.7%|✅|
|4846|🟢|ok thanks sara|thank|thank|99.7%|✅|
|4847|🟢|documentation of rasa is very bad|react_negative|react_negative|99.7%|✅|
|4848|🟢|why don't you restart????|restart|restart|99.7%|✅|
|4849|🟢|will this work on windows server|technical_question|technical_question|99.7%|✅|
|4850|🟢|source|source_code|source_code|99.7%|✅|
|4851|🟢|which tools can I use to create nlu data|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.7%|✅|
|4852|🟢|does rasa support python|faq/is_programming_required|faq/is_programming_required|99.7%|✅|
|4853|🟢|pip please|enter_data|enter_data|99.7%|✅|
|4854|🟢|what are the benefits of helping|ask_why_contribute|ask_why_contribute|99.7%|✅|
|4855|🟢|need help on chatbot|need_help_broad|need_help_broad|99.7%|✅|
|4856|🟢|i dont want to|deny|deny|99.7%|✅|
|4857|🟢|what is this bot for|chitchat/ask_whatspossible|chitchat/ask_whatspossible|99.7%|✅|
|4858|🟢|how contribute to Rasa|ask_how_contribute|ask_how_contribute|99.7%|✅|
|4859|🟢|how it works?|source_code|source_code|99.7%|✅|
|4860|🟢|Do you have any tutorials how to migrate from dialogflow?|switch|switch|99.7%|✅|
|4861|🟢|how do you build a bot|how_to_get_started|how_to_get_started|99.7%|✅|
|4862|🟢|very very sad|react_negative|react_negative|99.7%|✅|
|4863|🟢|bad|react_negative|react_negative|99.7%|✅|
|4864|🟢|I do not need help installing|deny|deny|99.7%|✅|
|4865|🟢|i would like to know why you need that|explain|explain|99.7%|✅|
|4866|🟢|I don't want to|deny|deny|99.7%|✅|
|4867|🟢|someone from customer care|human_handoff|human_handoff|99.7%|✅|
|4868|🟢|from which tools can I migrate to rasa?|switch|switch|99.7%|✅|
|4869|🟢|how can I build a chatbot|how_to_get_started|how_to_get_started|99.6%|✅|
|4870|🟢|what does NLU server do?|nlu_info|nlu_info|99.6%|✅|
|4871|🟢|How to generate NLU using frontend.|nlu_generation_tool_recommendation|nlu_generation_tool_recommendation|99.6%|✅|
|4872|🟢|and rasa nlu?|enter_data|enter_data|99.6%|✅|
|4873|🟢|I use [wit.ai](current_api)|switch|switch|99.6%|✅|
|4874|🟢|what pipeline is better for what i want?|pipeline_recommendation|pipeline_recommendation|99.6%|✅|
|4875|🟢|Do you have a great day?|chitchat/ask_howdoing|chitchat/ask_howdoing|99.6%|✅|
|4876|🟢|we started working with rasa but now we need support|contact_sales|contact_sales|99.6%|✅|
|4877|🟢|do you get anything?|canthelp|canthelp|99.6%|✅|
|4878|🟢|thanks for forum link, I'll check it out|thank|thank|99.6%|✅|
|4879|🟢|I wanted to build a bot my product customer support|how_to_get_started|how_to_get_started|99.6%|✅|
|4880|🟢|download|install_rasa|install_rasa|99.6%|✅|
|4881|🟢|the bot like you|enter_data|enter_data|99.6%|✅|
|4882|🟢|How to download rasa|install_rasa|install_rasa|99.6%|✅|
|4883|🟢|what you doing?|chitchat/ask_whatspossible|chitchat/ask_whatspossible|99.6%|✅|
|4884|🟢|I don't want to give it to you|deny|deny|99.6%|✅|
|4885|🟢|Thank you Sara|thank|thank|99.6%|✅|
|4886|🟢|i want to install|install_rasa|install_rasa|99.6%|✅|
|4887|🟢|ok thanks|thank|thank|99.6%|✅|
|4888|🟢|ok thanks!|thank|thank|99.6%|✅|
|4889|🟢|i want to use rasa to build my chatbot|how_to_get_started|how_to_get_started|99.6%|✅|
|4890|🟢|Help me get Rasa Core.|install_rasa|install_rasa|99.6%|✅|
|4891|🟢|I have something to ask about at the forum.|ask_question_in_forum|ask_question_in_forum|99.6%|✅|
|4892|🟢|rasa is bad|react_negative|react_negative|99.5%|✅|
|4893|🟢|I want to learn more about your pricing|contact_sales|contact_sales|99.5%|✅|
|4894|🟢|i don't care!!!!|react_negative|react_negative|99.5%|✅|
|4895|🟢|the bot won't train|broken|broken|99.5%|✅|
|4896|🟢|i want to know restart action|technical_question|technical_question|99.5%|✅|
|4897|🟢|i don't want to|deny|deny|99.5%|✅|
|4898|🟢|how help Rasa|ask_how_contribute|ask_how_contribute|99.5%|✅|
|4899|🟢|language = german|enter_data|enter_data|99.5%|✅|
|4900|🟢|language: german|enter_data|enter_data|99.5%|✅|
|4901|🟢|I'm ready to contribute.|ask_how_contribute|ask_how_contribute|99.5%|✅|
|4902|🟢|Sweet|affirm|react_positive|99.5%|❌|
|4903|🟢|How can I try out rasa enterprise|book_demo|book_demo|99.5%|✅|
|4904|🟢|I currently use dialog flow|switch|switch|99.5%|✅|
|4905|🟢|explain it to me|explain|explain|99.5%|✅|
|4906|🟢|what does that mean|explain|explain|99.4%|✅|
|4907|🟢|What does the NLU pipeline do|technical_question|technical_question|99.4%|✅|
|4908|🟢|I want to put some of my effort in.|ask_how_contribute|ask_how_contribute|99.4%|✅|
|4909|🟢|Rasa bot|enter_data|enter_data|99.4%|✅|
|4910|🟢|i want more information|explain|explain|99.4%|✅|
|4911|🟢|i need nlu.md file|source_code|source_code|99.4%|✅|
|4912|🟢|how about building chatbot|how_to_get_started|how_to_get_started|99.4%|✅|
|4913|🟢|[luis.ai](current_api)|switch|switch|99.4%|✅|
|4914|🟢|i don't think so|deny|deny|99.3%|✅|
|4915|🟢|can you explain how can i make chatbot like you|how_to_get_started|how_to_get_started|99.3%|✅|
|4916|🟢|what is your github link|source_code|source_code|99.3%|✅|
|4917|🟢|Where are you?|chitchat/ask_wherefrom|chitchat/ask_wherefrom|99.3%|✅|
|4918|🟢|what's so great about using Rasa?|why_rasa|why_rasa|99.3%|✅|
|4919|🟢|who is this|chitchat/ask_whoisit|chitchat/ask_whoisit|99.3%|✅|
|4920|🟢|WHAT IS IT|chitchat/ask_whatisrasa|chitchat/ask_whatisrasa|99.2%|✅|
|4921|🟢|not good|react_negative|react_negative|99.2%|✅|
|4922|🟢|what will i get for the contribution?|ask_why_contribute|ask_why_contribute|99.2%|✅|
|4923|🟢|What is up?|greet|greet|99.2%|✅|
|4924|🟢|please elaborate|explain|explain|99.2%|✅|
|4925|🟢|got it|enter_data|enter_data|99.1%|✅|
|4926|🟢|i'm not sure|deny|deny|99.1%|✅|
|4927|🟢|why do you need to know that|explain|explain|99.1%|✅|
|4928|🟢|I don't want to say|deny|deny|99.1%|✅|
|4929|🟢|what can I do?|ask_how_contribute|ask_how_contribute|99.0%|✅|
|4930|🟢|Playground is broken|broken|broken|99.0%|✅|
|4931|🟢|what is the right pipeline to choose?|pipeline_recommendation|pipeline_recommendation|99.0%|✅|
|4932|🟢|i don't want to give you my email|deny|deny|98.9%|✅|
|4933|🟢|give me a recommendation|pipeline_recommendation|pipeline_recommendation|98.8%|✅|
|4934|🟢|how come?|explain|explain|98.8%|✅|
|4935|🟢|What should I work on?|ask_how_contribute|ask_how_contribute|98.8%|✅|
|4936|🟢|There must be a way I can put forth my ideas to the situation.|ask_how_contribute|chitchat/ask_weather|98.7%|❌|
|4937|🟢|r u real?|chitchat/ask_ishuman|chitchat/ask_ishuman|98.7%|✅|
|4938|🟢|what are you?|chitchat/ask_whoisit|chitchat/ask_whoisit|98.6%|✅|
|4939|🟢|I would like to contribute.|ask_how_contribute|ask_how_contribute|98.6%|✅|
|4940|🟢|chatbot|enter_data|enter_data|98.5%|✅|
|4941|🟢|could you tell me more|explain|explain|98.5%|✅|
|4942|🟢|can you tell me how to create a new rasa project|how_to_get_started|how_to_get_started|98.5%|✅|
|4943|🟢|getting some errors|need_help_broad|need_help_broad|98.3%|✅|
|4944|🟢|rasa nlu|enter_data|enter_data|98.1%|✅|
|4945|🟢|What can I do?|chitchat/ask_whatspossible|ask_how_contribute|98.1%|❌|
|4946|🟢|what you do|chitchat/ask_whatspossible|chitchat/ask_whatspossible|98.0%|✅|
|4947|🟢|not sure yet|enter_data|enter_data|98.0%|✅|
|4948|🟢|I don't agree|deny|deny|98.0%|✅|
|4949|🟢|who are I ?|chitchat/ask_whoami|chitchat/ask_whoami|97.9%|✅|
|4950|🟢|custom entity|enter_data|enter_data|97.8%|✅|
|4951|🟢|buy rasa enterprise|contact_sales|contact_sales|97.7%|✅|
|4952|🟢|we want to have full code of rasa chatbot|source_code|source_code|97.5%|✅|
|4953|🟢|What could I do to contribute?|ask_how_contribute|ask_how_contribute|97.5%|✅|
|4954|🟢|you got me, I accept, if you want me to|affirm|affirm|97.5%|✅|
|4955|🟢|I want to make Rasa better|ask_how_contribute|ask_how_contribute|97.4%|✅|
|4956|🟢|I want to build a chatbot|how_to_get_started|how_to_get_started|97.3%|✅|
|4957|🟢|hiii|greet|greet|97.2%|✅|
|4958|🟢|can you help me with the pipeline?|pipeline_recommendation|pipeline_recommendation|97.1%|✅|
|4959|🟢|very much|affirm|affirm|97.0%|✅|
|4960|🟢|i need your data source|contact_sales|contact_sales|96.9%|✅|
|4961|🟢|where can I find the rasa source code?|source_code|source_code|96.6%|✅|
|4962|🟢|RASA NLU|enter_data|enter_data|96.5%|✅|
|4963|🟢|what are you doing|chitchat/ask_whatspossible|chitchat/ask_whatspossible|96.3%|✅|
|4964|🟢|Exit|bye|bye|96.0%|✅|
|4965|🟢|thanks for the help|thank|thank|95.9%|✅|
|4966|🟢|installation error|technical_question|technical_question|95.0%|✅|
|4967|🟢|Where to get Rasa Stack?|install_rasa|install_rasa|94.5%|✅|
|4968|🟢|not bad|affirm|affirm|94.4%|✅|
|4969|🟢|lets get started|how_to_get_started|how_to_get_started|94.3%|✅|
|4970|🟢|why|explain|explain|94.0%|✅|
|4971|🟢|restart server|technical_question|technical_question|94.0%|✅|
|4972|🟢|I want to build a bot|how_to_get_started|how_to_get_started|93.8%|✅|
|4973|🟢|Rasa Open Source is not training at all|broken|broken|93.1%|✅|
|4974|🟢|stop it, i do not care!!!|deny|deny|92.4%|✅|
|4975|🟢|please explain|explain|explain|92.1%|✅|
|4976|🟢|very bad|deny|deny|91.9%|✅|
|4977|🟡|how do i get rasa nlu|install_rasa|how_to_get_started|87.5%|❌|
|4978|🟡|Rasa NLU|enter_data|enter_data|87.1%|✅|
|4979|🟡|Rasa|enter_data|enter_data|83.7%|✅|
|4980|🟡|i would like rasa enterprise|contact_sales|contact_sales|83.4%|✅|
|4981|🟡|yes thanks|thank|thank|81.0%|✅|
|4982|🟡|how do i get rasa core|install_rasa|how_to_get_started|80.6%|❌|
|4983|🟡|exit|canthelp|canthelp|77.2%|✅|
|4984|🟡|Got it|react_positive|react_positive|76.4%|✅|
|4985|🟡|Rasa NLu|nlu_info|enter_data|73.6%|❌|
|4986|🟡|:)|react_positive|react_positive|71.7%|✅|
|4987|🟡|can you guide me know to create knowledge base chatbot|how_to_get_started|how_to_get_started|71.4%|✅|
|4988|🟡|4 + 2 = ?|out_of_scope/other|enter_data|71.2%|❌|
|4989|🟡|how do I get rasa core|install_rasa|how_to_get_started|70.6%|❌|
|4990|🟠|RASA?|chitchat/ask_whatisrasa|chitchat|67.1%|❌|
|4991|🟠|Where can I get the source code of Rasa?|technical_question|technical_question|63.0%|❌|
|4992|🟠|let's start|how_to_get_started|affirm|60.8%|❌|
|4993|🟠|customer service|enter_data|out_of_scope|60.6%|❌|
|4994|🟠|rasa|enter_data|enter_data|58.3%|❌|
|4995|🟠|i want to build a bot|enter_data|how_to_get_started|57.9%|❌|
|4996|🟠|how ?|chitchat/ask_howdoing|out_of_scope|54.3%|❌|
|4997|🟠|how|out_of_scope/other|out_of_scope|54.3%|❌|

### Sentences with problems
Table with the sentences that were not understood correctly by the model.

|#||Text|Intent|Predicted intent|Confidence|Understood|
|:-:|-|-|-|-|-|-|
|1|🟢|why is that necessary|explain|out_of_scope/other|100.0%|❌|
|2|🟢|german|enter_data|out_of_scope/other|100.0%|❌|
|3|🟢|time|enter_data|chitchat/ask_time|100.0%|❌|
|4|🟢|Sweet|affirm|react_positive|99.5%|❌|
|5|🟢|There must be a way I can put forth my ideas to the situation.|ask_how_contribute|chitchat/ask_weather|98.7%|❌|
|6|🟢|What can I do?|chitchat/ask_whatspossible|ask_how_contribute|98.1%|❌|
|7|🟡|how do i get rasa nlu|install_rasa|how_to_get_started|87.5%|❌|
|8|🟡|how do i get rasa core|install_rasa|how_to_get_started|80.6%|❌|
|9|🟡|Rasa NLu|nlu_info|enter_data|73.6%|❌|
|10|🟡|4 + 2 = ?|out_of_scope/other|enter_data|71.2%|❌|
|11|🟡|how do I get rasa core|install_rasa|how_to_get_started|70.6%|❌|
|12|🟠|RASA?|chitchat/ask_whatisrasa|chitchat|67.1%|❌|
|13|🟠|Where can I get the source code of Rasa?|technical_question|technical_question|63.0%|❌|
|14|🟠|let's start|how_to_get_started|affirm|60.8%|❌|
|15|🟠|customer service|enter_data|out_of_scope|60.6%|❌|
|16|🟠|rasa|enter_data|enter_data|58.3%|❌|
|17|🟠|i want to build a bot|enter_data|how_to_get_started|57.9%|❌|
|18|🟠|how ?|chitchat/ask_howdoing|out_of_scope|54.3%|❌|
|19|🟠|how|out_of_scope/other|out_of_scope|54.3%|❌|

## Core <a name='core'></a>
Section that discusses metrics about bot responses and actions.

### Metrics
Table with bot core metrics.

|#||Response|Precision|Recall|F1 Score|Number of occurrences|
|:-:|-|-|-|-|-|-|
|1|🟢|utter_explain_core|100.0%|100.0%|100.0%|5|
|2|🟢|action_submit_subscribe_newsletter_form|100.0%|100.0%|100.0%|2|
|3|🟢|utter_can_do|100.0%|100.0%|100.0%|2|
|4|🟢|utter_why_rasa_research|100.0%|100.0%|100.0%|1|
|5|🟢|utter_ask_ready_to_build|100.0%|100.0%|100.0%|1|
|6|🟢|utter_ask_feedback|100.0%|100.0%|100.0%|3|
|7|🟢|utter_ask_more|100.0%|100.0%|100.0%|1|
|8|🟢|utter_direct_to_forum_for_help|100.0%|100.0%|100.0%|1|
|9|🟢|action_set_faq_slot|100.0%|100.0%|100.0%|5|
|10|🟢|utter_ask_explain_nlucorex|100.0%|100.0%|100.0%|2|
|11|🟢|utter_ask_continue_newsletter|100.0%|100.0%|100.0%|1|
|12|🟢|action_set_onboarding|100.0%|100.0%|100.0%|6|
|13|🟢|utter_ask_which_product|100.0%|100.0%|100.0%|6|
|14|🟢|utter_ask_playground_install_info|100.0%|100.0%|100.0%|7|
|15|🟢|utter_explain_nlu|100.0%|100.0%|100.0%|5|
|16|🟢|utter_out_of_scope|100.0%|100.0%|100.0%|1|
|17|🟢|utter_rasa_components_details|100.0%|100.0%|100.0%|2|
|18|🟢|utter_why_rasa_nlu|100.0%|100.0%|100.0%|1|
|19|🟢|utter_possibilities_to_contribute|100.0%|100.0%|100.0%|1|
|20|🟢|action_restart_with_button|100.0%|100.0%|100.0%|1|
|21|🟢|utter_ask_playground_help|100.0%|100.0%|100.0%|1|
|22|🟢|utter_getstarted_new|100.0%|100.0%|100.0%|1|
|23|🟢|action_explain_faq|100.0%|100.0%|100.0%|1|
|24|🟢|utter_docu|100.0%|100.0%|100.0%|3|
|25|🟢|action_store_problem_description|100.0%|100.0%|100.0%|1|
|26|🟢|utter_ask_continue_sales|100.0%|100.0%|100.0%|1|
|27|🟢|utter_ask_x_local_server|100.0%|100.0%|100.0%|2|
|28|🟢|action_trigger_response_selector|100.0%|100.0%|100.0%|5|
|29|🟢|utter_first_bot_with_rasa|100.0%|100.0%|100.0%|5|
|30|🟢|utter_great|100.0%|100.0%|100.0%|2|
|31|🟢|utter_also_explain_nlucore|100.0%|100.0%|100.0%|2|
|32|🟢|utter_playground_intro|100.0%|100.0%|100.0%|1|
|33|🟢|utter_moreinformation|100.0%|100.0%|100.0%|1|
|34|🟢|utter_installation_command|100.0%|100.0%|100.0%|1|
|35|🟢|utter_built_bot_before|100.0%|100.0%|100.0%|2|
|36|🟢|utter_link_to_forum|100.0%|100.0%|100.0%|1|
|37|🟢|utter_thumbsup|100.0%|100.0%|100.0%|3|
|38|🟢|action_get_community_events|100.0%|100.0%|100.0%|1|
|39|🟢|action_greet_user|100.0%|100.0%|100.0%|4|
|40|🟢|utter_contact_email|100.0%|100.0%|100.0%|1|
|41|🟢|action_submit_sales_form|100.0%|100.0%|100.0%|1|
|42|🟢|utter_why_rasa_os|100.0%|100.0%|100.0%|1|
|43|🟢|action_listen|100.0%|100.0%|100.0%|71|
|44|🟢|utter_chitchat|100.0%|100.0%|100.0%|4|
|45|🟢|utter_having_trouble_installing|100.0%|100.0%|100.0%|1|
|46|🟢|utter_anything_else|100.0%|100.0%|100.0%|3|
|47|🟢|utter_possibilities|100.0%|100.0%|100.0%|1|
|48|🟢|utter_ask_migration|100.0%|100.0%|100.0%|1|
|49|🟢|utter_greet|100.0%|100.0%|100.0%|2|
|50|🟢|utter_faq|100.0%|100.0%|100.0%|5|
|51|🟢|action_two_stage_fallback|100.0%|100.0%|100.0%|3|
|52|🟢|utter_run_rasa_init|100.0%|100.0%|100.0%|1|
|53|🟢|utter_explain_rasa_components|100.0%|100.0%|100.0%|2|
|54|🟢|utter_rasa_x_local_installation|100.0%|100.0%|100.0%|2|
|55|🟢|utter_why_rasa_dialogue|100.0%|100.0%|100.0%|1|
|56|🟢|utter_why_rasa_compliant|100.0%|100.0%|100.0%|1|
|57|🟢|utter_explain_x|100.0%|100.0%|100.0%|2|
|58|🟢|utter_why_rasa|100.0%|100.0%|100.0%|1|
|59|🟢|utter_reasons_to_contribute|100.0%|100.0%|100.0%|1|
### Confusion Matrix
![Confusion Matrix](results/story_confusion_matrix.png 'Confusion Matrix')

## E2E Coverage <a name='e2e'></a>
Section that shows data from intents and responses that aren't covered by end-to-end tests.

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

#### Actions
 - utter_also_explain_core
 - utter_also_explain_nlu
 - utter_awesome
 - utter_bye
 - utter_canthelp
 - utter_cantsignup
 - utter_change_mind
 - utter_chatbot_tutorial
 - utter_crf
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
 - utter_sales_contact
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
 - utter_what_help
 - utter_what_language
 - utter_x_tutorial

Total number of elements: 174

Total number of not covered elements: 83

Total number of excluded elements: 33

Coverage rate: 52.3% (🟠)


##### Generated by rasa-model-report v1.4.2b14, collaborative open-source project for Rasa projects. Github repository at this [link](https://github.com/brunohjs/rasa-model-report).
