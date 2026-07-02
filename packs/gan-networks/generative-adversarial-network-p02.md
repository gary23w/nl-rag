---
title: "Generative adversarial network (part 2/2)"
source: https://en.wikipedia.org/wiki/Generative_adversarial_network
domain: gan-networks
license: CC-BY-SA-4.0
tags: gan network, generative adversarial, discriminator generator, adversarial training, image synthesis
fetched: 2026-07-02
part: 2/2
---

## Applications

### Science

- Iteratively reconstruct astronomical images
- Simulate gravitational lensing for dark matter research.
- Model the distribution of dark matter in a particular direction in space and to predict the gravitational lensing that will occur.
- Model high energy jet formation and showers through calorimeters of high-energy physics experiments.
- Approximate bottlenecks in computationally expensive simulations of particle physics experiments. Applications in the context of present and proposed CERN experiments have demonstrated the potential of these methods for accelerating simulation and/or improving simulation fidelity.
- Reconstruct velocity and scalar fields in turbulent flows.

GAN-generated molecules were validated experimentally in mice.

### Medical

One of the major concerns in medical imaging is preserving patient privacy. Due to these reasons, researchers often face difficulties in obtaining medical images for their research purposes. GAN has been used for generating synthetic medical images, such as MRI and PET images to address this challenge.

GAN can be used to detect glaucomatous images helping the early diagnosis which is essential to avoid partial or total loss of vision.

GANs have been used to create forensic facial reconstructions of deceased historical figures.

### Malicious

Concerns have been raised about the potential use of GAN-based human image synthesis for sinister purposes, e.g., to produce fake, possibly incriminating, photographs and videos. GANs can be used to generate unique, realistic profile photos of people who do not exist, in order to automate creation of fake social media profiles.

In 2019 the state of California considered and passed on October 3, 2019, the bill AB-602, which bans the use of human image synthesis technologies to make fake pornography without the consent of the people depicted, and bill AB-730, which prohibits distribution of manipulated videos of a political candidate within 60 days of an election. Both bills were authored by Assembly member Marc Berman and signed by Governor Gavin Newsom. The laws went into effect in 2020.

DARPA's Media Forensics program studies ways to counteract fake media, including fake media produced using GANs.

### Fashion, art and advertising

GANs can be used to generate art; *The Verge* wrote in March 2019 that "The images created by GANs have become the defining look of contemporary AI art." GANs can also be used to

- inpaint photographs
- generate fashion models, shadows, photorealistic renders of interior design, industrial design, shoes, etc. Such networks were reported to be used by Facebook.

Some have worked with using GAN for artistic creativity, as "creative adversarial network". A GAN, trained on a set of 15,000 portraits from WikiArt from the 14th to the 19th century, created the 2018 painting *Edmond de Belamy,* which sold for US$432,500.

GANs were used by the video game modding community to up-scale low-resolution 2D textures in old video games by recreating them in 4k or higher resolutions via image training, and then down-sampling them to fit the game's native resolution (resembling supersampling anti-aliasing).

In 2020, Artbreeder was used to create the main antagonist in the sequel to the psychological web horror series *Ben Drowned*. The author would later go on to praise GAN applications for their ability to help generate assets for independent artists who are short on budget and manpower.

In May 2020, Nvidia researchers taught an AI system (termed "GameGAN") to recreate the game of *Pac-Man* simply by watching it being played.

In August 2019, a large dataset consisting of 12,197 MIDI songs each with paired lyrics and melody alignment was created for neural melody generation from lyrics using conditional GAN-LSTM (refer to sources at GitHub AI Melody Generation from Lyrics).

### Miscellaneous

GANs have been used to

- show how an individual's appearance might change with age.
- reconstruct 3D models of objects from images,
- generate novel objects as 3D point clouds,
- model patterns of motion in video.
- inpaint missing features in maps, transfer map styles in cartography or augment street view imagery.
- use feedback to generate images and replace image search systems.
- visualize the effect that climate change will have on specific houses.
- reconstruct an image of a person's face after listening to their voice.
- produces videos of a person speaking, given only a single photo of that person.
- recurrent sequence generation.


## History

In 1991, Juergen Schmidhuber published "artificial curiosity", neural networks in a zero-sum game. The first network is a generative model that models a probability distribution over output patterns. The second network learns by gradient descent to predict the reactions of the environment to these patterns. GANs can be regarded as a case where the environmental reaction is 1 or 0 depending on whether the first network's output is in a given set.

Other people had similar ideas but did not develop them similarly. An idea involving adversarial networks was published in a 2010 blog post by Olli Niemitalo. This idea was never implemented and did not involve stochasticity in the generator and thus was not a generative model. An idea similar to GANs was used to model animal behavior by Wei Li, Melvin Gauci and Roderich Gross in 2013.

Another inspiration for GANs was noise-contrastive estimation, which uses the same loss function as GANs and which Goodfellow studied during his PhD in 2010–2014.

Adversarial machine learning has other uses besides generative modeling and can be applied to models other than neural networks. In control theory, adversarial learning based on neural networks was used in 2006 to train robust controllers in a game theoretic sense, by alternating the iterations between a minimizer policy, the controller, and a maximizer policy, the disturbance.

In 2017, a GAN was used for image enhancement focusing on realistic textures rather than pixel-accuracy, producing a higher image quality at high magnification. In 2017, the first faces were generated. These were exhibited in February 2018 at the Grand Palais. Faces generated by StyleGAN in 2019 drew comparisons with Deepfakes.
