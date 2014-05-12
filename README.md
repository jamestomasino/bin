## bin scripts intended for ~/bin

### Dependencies ###

`safe-reattach-to-user-namespace` requires `attach-to-user-namespace`

    $ brew install attach-to-user-namespace
    
`weather` requires `jq` - [jq](http://stedolan.github.io/jq/)

### Install ###

From cloned git repo folder:

    ln -s `pwd` ~/bin
