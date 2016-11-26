# Site d'information de Nuit Debout Lyon

Ce repository contient les sources du site d'information du [site de Nuit
Debout à Lyon](https://nuitdeboutlyon.fr/).

## Architecture

### Site

Le site en lui-même est un site statique généré à partir de fichiers de contenu
en markdown avec l'outil [Pelican](https://getpelican.org/). Le serveur de
production s'occupe de toujours être synchronisé avec la dernière version du
contenu de repository et regénère les pages régulièrement après des
modifications.

Pour publier du contenu sur le site on peut donc simplement modifier les
fichiers markdown et *pusher* les changements sur la branche *prod* du
repository.

### Serveur d'API

Pour plus de souplesse et d'accessibilité, ceci n'est pas la manière
privilégiée pour publier du contenu (par exemple un compte-rendu ou une annonce
d'événement). Lorsqu'un utilisateur autorisé du forum (faisant partie du groupe
*rédacteur*) poste un message, discourse effectue une requête `POST` sur le
serveur d'API avec comme payload du json décrivant la nature de la publication
(voir la [documentation des webhook discourse](???)). À la réception du cette
requête, le serveur d'API vérifie que le post correspond à un certain format
(contient le tag "compte-rendu" ou "evenement") et publie le contenu du message
sur le site. Ainsi on peut voir sur le site les messages "officiels" et
"importants" du forum, présentés en lecture seule dans une forme plus
accessible.

## Installation / Développement

Le projet se découpe donc en 2 parties écrites en python3. Dépendances du générateur du site:

- Pelican

Dépendances du serveur d'API:

- Flask
- Requests
- PyYaml
