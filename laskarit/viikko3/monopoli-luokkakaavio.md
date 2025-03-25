```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Aloitusruutu --> Ruutu
    Vankila --> Ruutu
    Sattuma_ja_yhteismaa --> Ruutu
    Asemat_ja_laitokset --> Ruutu
    Normaali_katu --> Ruutu
    Normaali_katu -- "1" Nimi
    Normaali_katu -- "0..4" Talo
    Normaali_katu -- "0..1" Hotelli
    Normaali_katu -- "0..1" Pelaaja
    Ruutu "40" -- Toiminto
    Sattuma_ja_yhteismaa -- Kortti
    Kortti "1" -- "1" Toiminto
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelaaja "2..8" -- Raha

```
