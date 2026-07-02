---
title: "Cold start (recommender systems)"
source: https://en.wikipedia.org/wiki/Cold_start_(recommender_systems)
domain: recommender-systems
license: CC-BY-SA-4.0
tags: recommender system, collaborative filtering, matrix factorization, personalization, cold start
fetched: 2026-07-02
---

# Cold start (recommender systems)

**Cold start** is a potential problem in computer-based information systems which involves a degree of automated data modelling. Specifically, it concerns the issue that the system cannot draw any inferences for users or items about which it has not yet gathered sufficient information.

## Systems affected

The cold start problem is a well known and well researched problem for recommender systems. Recommender systems form a specific type of information filtering (IF) technique that attempts to present information items (e-commerce, films, music, books, news, images, web pages) that are likely of interest to the user. Typically, a recommender system compares the user's profile to some reference characteristics. These characteristics may be related to item characteristics (content-based filtering) or the user's social environment and past behavior (collaborative filtering). Depending on the system, the user can be associated to various kinds of interactions: ratings, bookmarks, purchases, likes, number of page visits etc.

There are three cases of cold start:

1. **New community**: refers to the start-up of the recommender, when, although a catalogue of items might exist, almost no users are present and the lack of user interaction makes it very hard to provide reliable recommendations
2. **New item**: a new item is added to the system, it might have some content information but no interactions are present
3. **New user**: a new user registers and has not provided any interaction yet, therefore it is not possible to provide personalized recommendations

### New community

The new community problem, or systemic bootstrapping, refers to the startup of the system, when virtually no information the recommender can rely upon is present. This case presents the disadvantages of both the New user and the New item case, as all items and users are new. Due to this some of the techniques developed to deal with those two cases are not applicable to the system bootstrapping.

### New item

The item cold-start problem refers to when items added to the catalogue have either none or very little interactions. This constitutes a problem mainly for collaborative filtering algorithms due to the fact that they rely on the item's interactions to make recommendations. If no interactions are available then a pure collaborative algorithm cannot recommend the item. In case only a few interactions are available, although a collaborative algorithm will be able to recommend it, the quality of those recommendations will be poor. This raises another issue, which is not anymore related to new items, but rather to *unpopular items*. In some cases (e.g. movie recommendations) it might happen that a handful of items receive an extremely high number of interactions, while most of the items only receive a fraction of them. This is referred to as **popularity bias**.

In the context of cold-start items the popularity bias is important because it might happen that many items, even if they have been in the catalogue for months, received only a few interactions. This creates a negative loop in which unpopular items will be poorly recommended, therefore will receive much less visibility than popular ones, and will struggle to receive interactions. While it is expected that some items will be less popular than others, this issue specifically refers to the fact that the recommender has not enough collaborative information to recommend them in a meaningful and reliable way.

Content-based filtering algorithms, on the other hand, are in theory much less prone to the new item problem. Since content based recommenders choose which items to recommend based on the feature the items possess, even if no interaction for a new item exist, still its features will allow for a recommendation to be made. This of course assumes that a new item will be already described by its attributes, which is not always the case. Consider the case of so-called *editorial* features (e.g. director, cast, title, year), those are always known when the item, in this case movie, is added to the catalogue. However, other kinds of attributes might not be e.g. features extracted from user reviews and tags. Content-based algorithms relying on user provided features suffer from the cold-start item problem as well, since for new items if no (or very few) interactions exist, also no (or very few) user reviews and tags will be available.

### New user

The new user case refers to when a new user enrolls in the system and for a certain period of time the recommender has to provide recommendation without relying on the user's past interactions, since none has occurred yet. This problem is of particular importance when the recommender is part of the service offered to users, since a user who is faced with recommendations of poor quality might soon decide to stop using the system before providing enough interaction to allow the recommender to understand his/her interests. The main strategy in dealing with new users is to ask them to provide some preferences to build an initial user profile. A threshold has to be found between the length of the user registration process, which if too long might induce too many users to abandon it, and the amount of initial data required for the recommender to work properly.

Similarly to the new items case, not all recommender algorithms are affected in the same way. Item-item recommenders will be affected as they rely on user profile to weight how relevant other user's preferences are. Collaborative filtering algorithms are the most affected as without interactions no inference can be made about the user's preferences. User-user recommender algorithms behave slightly differently. A user-user content based algorithm will rely on user's features (e.g. age, gender, country) to find similar users and recommend the items they interacted with in a positive way, therefore being robust to the new user case. Note that all these information is acquired during the registration process, either by asking the user to input the data himself, or by leveraging data already available e.g. in his social media accounts.

## Mitigation strategies

Due to the high number of recommender algorithms available as well as system type and characteristics, many strategies to mitigate the cold-start problem have been developed. The main approach is to rely on hybrid recommenders, in order to mitigate the disadvantages of one category or model by combining it with another.

All three categories of cold-start (new community, new item, and new user) have in common the lack of user interactions and presents some commonalities in the strategies available to address them.

A common strategy when dealing with new items is to couple a collaborative filtering recommender, for warm items, with a content-based filtering recommender, for cold-items. While the two algorithms can be combined in different ways, the main drawback of this method is related to the poor recommendation quality often exhibited by content-based recommenders in scenarios where it is difficult to provide a comprehensive description of the item characteristics. In case of new users, if no demographic feature is present or their quality is too poor, a common strategy is to offer them non-personalized recommendations. This means that they could be recommended simply the most popular items either globally or for their specific geographical region or language.

### Profile completion

One of the available options when dealing with cold users or items is to rapidly acquire some preference data. There are various ways to do that depending on the amount of information required. These techniques are called preference elicitation strategies. This may be done either explicitly (by querying the user) or implicitly (by observing the user's behaviour). In both cases, the cold start problem would imply that the user has to dedicate an amount of effort using the system in its 'dumb' state – contributing to the construction of their user profile – before the system can start providing any intelligent recommendations.

For example MovieLens, a web-based recommender system for movies, asks the user to rate some movies as a part of the registration. While preference elicitation strategy are a simple and effective way to deal with new users, the additional requirements during the registration will make the process more time-consuming for the user. Moreover, the quality of the obtained preferences might not be ideal as the user could rate items they had seen months or years ago or the provided ratings could be almost random if the user provided them without paying attention just to complete the registration quickly.

The construction of the user's profile may also be automated by integrating information from other user activities, such as browsing histories or social media platforms. If, for example, a user has been reading information about a particular music artist from a media portal, then the associated recommender system would automatically propose that artist's releases when the user visits the music store.

A variation of the previous approach is to automatically assign ratings to new items, based on the ratings assigned by the community to other similar items. Item similarity would be determined according to the items' content-based characteristics.

It is also possible to create initial profile of a user based on the personality characteristics of the user and use such profile to generate personalized recommendation. Personality characteristics of the user can be identified using a personality model such as five factor model (FFM).

Another of the possible techniques is to apply active learning (machine learning). The main goal of active learning is to guide the user in the preference elicitation process in order to ask him to rate only the items that for the recommender point of view will be the most informative ones. This is done by analysing the available data and estimating the usefulness of the data points (e.g., ratings, interactions). As an example, say that we want to build two clusters from a certain cloud of points. As soon as we have identified two points each belonging to a different cluster, which is the next most informative point? If we take a point close to one we already know we can expect that it will likely belong to the same cluster. If we choose a point which is in between the two clusters, knowing which cluster it belongs to will help us in finding where the boundary is, allowing to classify many other points with just a few observations.

The cold start problem is also exhibited by interface agents. Since such an agent typically learns the user's preferences implicitly by observing patterns in the user's behaviour – "watching over the shoulder" – it would take time before the agent may perform any adaptations personalised to the user. Even then, its assistance would be limited to activities which it has formerly observed the user engaging in. The cold start problem may be overcome by introducing an element of collaboration amongst agents assisting various users. This way, novel situations may be handled by requesting other agents to share what they have already learnt from their respective users.

### Feature mapping

In recent years more advanced strategies have been proposed, they all rely on machine learning and attempt to merge the content and collaborative information in a single model. One example of this approaches is called *attribute to feature mapping* which is tailored to matrix factorization algorithms. The basic idea is the following. A matrix factorization model represents the user-item interactions as the product of two rectangular matrices whose content is learned using the known interactions via machine learning. Each user will be associated to a row of the first matrix and each item with a column of the second matrix. The row or column associated to a specific user or item is called *latent factors*. When a new item is added it has no associated latent factors and the lack of interactions does not allow to learn them, as it was done with other items. If each item is associated to some features (e.g. author, year, publisher, actors) it is possible to define an embedding function, which given the item features estimates the corresponding item latent factors. The embedding function can be designed in many ways and it is trained with the data already available from warm items. Alternatively, one could apply a group-specific method. A group-specific method further decomposes each latent factor into two additive parts: One part corresponds to each item (and/or each user), while the other part is shared among items within each item group (e.g., a group of movies could be movies of the same genre). Then once a new item arrives, we can assign a group label to it, and approximates its latent factor by the group-specific part (of the corresponding item group). Therefore, although the individual part of the new item is not available, the group-specific part provides an immediate and effective solution. The same applies for a new user, as if some information is available for them (e.g. age, nationality, gender) then his/her latent factors can be estimated via an embedding function or a group-specific latent factor.

### Hybrid feature weighting

Another recent approach which bears similarities with feature mapping is building a hybrid content-based filtering recommender in which features, either of the items or of the users, are weighted according to the user's perception of importance. In order to identify a movie that the user could like, different attributes (e.g. which are the actors, director, country, title) will have different importance. As an example consider the James Bond movie series, the main actor changed many times during the years, while some did not, like Lois Maxwell. Therefore, her presence will probably be a better identifier of that kind of movie than the presence of one of the various main actors. Although various techniques exist to apply feature weighting to user or item features in recommender systems, most of them are from the information retrieval domain like tf–idf, Okapi BM25, only a few have been developed specifically for recommenders.

Hybrid feature weighting techniques in particular are tailored for the recommender system domain. Some of them learn feature weight by exploiting directly the user's interactions with items, like FBSM. Others rely on an intermediate collaborative model trained on warm items and attempt to learn the content feature weights which will better approximate the collaborative model.

Many of the hybrid methods can be considered special cases of factorization machines.

### Differentiating regularization weights

The above methods rely on affiliated information from users or items. Recently, another approach mitigates the cold start problem by assigning lower constraints to the latent factors associated with the items or users that reveal more information (i.e., popular items and active users), and set higher constraints to the others (i.e., less popular items and inactive users). It is shown that various recommendation models benefit from this strategy. Differentiating regularization weights can be integrated with the other cold start mitigating strategies.
