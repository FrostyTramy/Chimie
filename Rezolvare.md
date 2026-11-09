# TEST — Dumitrașcu Tudor-Dominik, X-G (9.11.2026)

## 1. Care este efectul fenomenului de străpungere a diodei?

**Răspuns corect: b) creșterea bruscă a curentului invers prin diodă.**

La polarizare inversă, când tensiunea atinge valoarea de străpungere, curentul invers crește brusc, în timp ce tensiunea pe diodă rămâne aproape constantă. Pe acest efect funcționează dioda Zener.

- a) greșit — creșterea curentului direct apare la polarizare directă, nu prin străpungere.
- c) greșit — tensiunea pe diodă nu scade brusc, ci se menține aproape constantă ($U_Z$).

## 2. Valoarea minimă a rezistenței R

Date: $U = 18\ \text{V}$, $U_Z = 6\ \text{V}$, $I_{Z\max} = 30\ \text{mA}$.

Rezistența R este în serie cu dioda Zener, deci prin ea trece curentul $I = I_Z$. Tensiunea pe rezistență:

$$U_R = U - U_Z = 18 - 6 = 12\ \text{V}$$

Curentul nu trebuie să depășească $I_{Z\max}$:

$$I = \frac{U - U_Z}{R} \le I_{Z\max} \;\Rightarrow\; R \ge \frac{U - U_Z}{I_{Z\max}}$$

$$R_{\min} = \frac{12\ \text{V}}{30\ \text{mA}} = \frac{12}{0{,}03}\ \Omega = 400\ \Omega$$

**Răspuns: $R_{\min} = 400\ \Omega$.**
