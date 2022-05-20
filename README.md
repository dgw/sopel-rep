# sopel-rep
Lets users "luv" and "h8" other users on IRC. Functional clone of a mIRC script
someone used in a channel I was in. (Never saw their code, not that I'd want to
do a *port* of anything written for mIRC...)

## Dependencies
Sopel version 7.1 or higher

## Usage
### Commands
* `.luv nick`: Adds +1 to the user's reputation score
* `.h8 nick`: Adds -1 to the user's reputation score

### Actions
* `/me <3 nick`: Adds +1 to the user's reputation score
* `/me </3 nick`: Adds -1 to the user's reputation score

### Inline karma
* `nick++` anywhere in a message adds +1 to the user's reputation score
* `nick--` anywhere in a message adds -1 to the user's reputation score
