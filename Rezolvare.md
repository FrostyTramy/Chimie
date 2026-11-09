# TEST — Dumitrașcu Tudor-Dominik, X-G (9.11.2026)

## 1. Care este efectul fenomenului de străpungere a diodei?

**Răspuns corect: b) creșterea bruscă a curentului invers prin diodă.**

La polarizare inversă, când tensiunea atinge valoarea de străpungere, curentul invers crește brusc, în timp ce tensiunea pe diodă rămâne aproape constantă. Pe acest efect funcționează dioda Zener.

## 2. Valoarea minimă a rezistenței R

Date: $U = 18\ \text{V}$, $U_Z = 6\ \text{V}$, $I_{Z\max} = 30\ \text{mA}$.

$$U_R = U - U_Z = 12\ \text{V}, \qquad I = \frac{U-U_Z}{R} \le I_{Z\max} \Rightarrow R \ge \frac{12\ \text{V}}{30\ \text{mA}} = 400\ \Omega$$

**Răspuns: $R_{\min} = 400\ \Omega$.**

## 7. Frecvență mare înseamnă:

**Răspuns corect: b) perioada mică a semnalului.**

Frecvența și perioada sunt invers proporționale: $f = \dfrac{1}{T}$. Cu cât $T$ este mai mic, cu atât $f$ este mai mare.

## 8. Dioda de comutație schimbă starea de conducție cu starea de blocare:

**Răspuns corect: a) foarte repede.**

Dioda de comutație este construită pentru timpi de comutare foarte mici (nanosecunde), de aceea se folosește în circuite de frecvență mare și în circuite digitale.

## 9. Caracteristica statică de funcționare a diodei, cu toate mărimile care intervin

Caracteristica statică $I = f(U)$ este curba curentului prin diodă în funcție de tensiunea aplicată.

```
                     I (mA)
                       |                  /
                       |                 /   zona de conducție
                       |                /    (polarizare directă)
                       |               /
                       |              /
                       |            _/
                       |         __/
  U_BR  ---------------+--------'----------------------  U (V)
   |  zona de          |       U_γ
   |  străpungere      |
   |                   |   curent invers I_R (µA, foarte mic)
   v                  -I_R
(−I, µA)
```

Mărimile care intervin:

- **$U$** – tensiunea aplicată pe diodă (axa orizontală); $U>0$ polarizare directă, $U<0$ polarizare inversă.
- **$I$** – curentul prin diodă (axa verticală); $I>0$ curent direct, $I<0$ curent invers.
- **$U_\gamma$** – tensiunea de prag (de deschidere): ≈ 0,6–0,7 V la siliciu, ≈ 0,2–0,3 V la germaniu. Peste ea curentul direct crește rapid.
- **$I_F$** – curentul direct, mare (mA–A), în zona de conducție.
- **$I_R$ (sau $I_0$)** – curentul invers (de saturație), foarte mic (µA–nA), aproape constant la polarizare inversă.
- **$U_{BR}$** – tensiunea de străpungere; la $|U|\ge U_{BR}$ curentul invers crește brusc.

Ecuația dioadei ideale: $I = I_0\left(e^{U/(nU_T)} - 1\right)$, cu $U_T \approx 26\ \text{mV}$ la 300 K.

**Zone de funcționare:** (1) polarizare directă — conducție pentru $U>U_\gamma$; (2) polarizare inversă — blocare, curent $I_R$ neglijabil; (3) străpungere — creștere bruscă a curentului invers la $U_{BR}$.
