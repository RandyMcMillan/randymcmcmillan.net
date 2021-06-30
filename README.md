[🐝](https://keyserver.ubuntu.com/pks/lookup?search=randy.lee.mcmillan%40gmail.com&fingerprint=on&op=vindex) [Twitter](https://twitter.com/RandyMcMillan) [Keybase](https://randymcmillan.keybase.pub) [Clubhouse](https://clubhouse.com/@randymcmillan)
----

## [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) AWESOME GITOPS
<AUTOMATION>
<p>
### AUTOMATION
 [![automate](https://github.com/RandyMcMillan/randymcmillan/actions/workflows/automate.yml/badge.svg)](https://github.com/RandyMcMillan/randymcmillan/actions/workflows/automate.yml) [![global-statoshi-host](https://github.com/RandyMcMillan/randymcmillan/actions/workflows/statoshi.host.yml/badge.svg)](https://github.com/RandyMcMillan/randymcmillan/actions/workflows/statoshi.host.yml) [![global-stats-bitcoincore-dev](https://github.com/RandyMcMillan/randymcmillan/actions/workflows/stats.bitcoincore.dev.yml/badge.svg)](https://github.com/RandyMcMillan/randymcmillan/actions/workflows/stats.bitcoincore.dev.yml)
</p>
</AUTOMATION>


<details>
<summary>COMMANDS</summary>

```shell
TOKEN=$(~/GH_TOKEN); export TOKEN && curl -I https://api.github.com -u $(GIT_USER):$TOKEN
```
</p>
</details>



<details>
<summary>👀</summary>
<p>

```shell
seq 0 947 | (while read -r n; do bitcoin-cli gettxout \
54e48e5f5c656b26c3bca14a8c95aa583d07ebe84dde3b7dd4a78f4e4186e713 $n \
| jq -r '.scriptPubKey.asm' | awk '{ print $2 $3 $4 }'; done) | \
tr -d '\n' | cut -c 17-368600 | xxd -r -p > bitcoin.pdf
```

</p>
</details>