<AUTOMATION>
<p>

## [![Awesome](https://awesome.re/badge.svg)](https://github.com/RandyMcMillan/randymcmillan/blob/master/sources/awesome.html) [![legit](https://github.com/RandyMcMillan/legit/actions/workflows/automate.yml/badge.svg)](https://github.com/RandyMcMillan/legit/actions/workflows/automate.yml) [![statoshi.host](https://github.com/bitcoincore-dev/statoshi.host/actions/workflows/statoshi.host.yml/badge.svg)](https://github.com/bitcoincore-dev/statoshi.host/actions/workflows/statoshi.host.yml)

<CENTER></CENTER>

</p>
</AUTOMATION>

<details>
<summary>legit - git commit custom hash</summary>

```shell
git clone https://github.com/RandyMcMillan/legit.git ~/legit
cd ~/legit && ./make-legit.sh
```
</p>
</details>


<details>
<summary>statoshi.host - dockerized bitcoin node statistics</summary>

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install docker docker-compose make
git clone https://github.com/bitcoincore-dev/statoshi.host.git ~/statoshi.host
cd ~/statoshi.host && make run
```
</p>
</details>



