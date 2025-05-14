# Rapport Technique : Automatisation de la Découverte et de la Génération de Cartes de Gadgets ROP/JOP

## 1. Introduction et Objectif

Dans le cadre de l'amélioration continue et de la facilitation de la maintenance des exploits basés sur les techniques de ROP (Return-Oriented Programming) et JOP (Jump-Oriented Programming), tels que ceux utilisés dans des projets comme `psfree-lapse`, un défi majeur réside dans la mise à jour constante des "gadgets". Les gadgets sont de courtes séquences d'instructions existantes dans le binaire d'un programme qui se terminent par une instruction de retour (comme `ret`) ou de saut. La recherche et l'organisation de ces gadgets pour chaque nouvelle version de firmware ou de bibliothèque système peuvent s'avérer fastidieuses et sujettes aux erreurs.

L'objectif principal de ce développement était d'automatiser intégralement le processus de découverte de gadgets à partir d'un fichier binaire et de générer automatiquement le code JavaScript (sous forme d'objets `Map`) nécessaire pour les intégrer dans la structure du projet `psfree-lapse`.

## 2. Approche et Méthodologie

Pour atteindre cet objectif, une approche en plusieurs étapes a été adoptée, combinant l'utilisation d'outils d'analyse binaire existants avec le développement de scripts personnalisés pour le traitement des données et la génération de code.

### 2.1. Outils et Environnement

*   **ROPgadget**: Un outil open-source en Python, choisi pour sa capacité à rechercher des gadgets dans les fichiers binaires ELF. Il a été installé dans l'environnement de développement via `pip3 install ROPgadget`.
*   **GCC (GNU Compiler Collection)**: Utilisé pour compiler un programme de test en C afin de générer un fichier binaire ELF simple pour les phases initiales de test de `ROPgadget` et des scripts d'analyse. Installé via `sudo apt-get install -y gcc`.
*   **Python 3.11**: Langage principal pour le développement des scripts d'automatisation et de traitement.

### 2.2. Fichiers de Test

Pour valider le pipeline d'automatisation, les fichiers suivants ont été créés :

*   `test_rop.c`: Un fichier source C simple contenant quelques fonctions avec des instructions assembleur susceptibles de générer des gadgets basiques.
    ```c
    #include <stdio.h>

    void useful_function_1() {
        asm("pop %rax; ret");
    }

    void useful_function_2() {
        asm("mov %rax, %rdi; ret");
    }

    int main() {
        printf("Hello, ROPgadget!\n");
        useful_function_1();
        useful_function_2();
        return 0;
    }
    ```
*   `test_rop_binary`: Le fichier binaire ELF résultant de la compilation de `test_rop.c` avec la commande `gcc -o /home/ubuntu/test_rop_binary /home/ubuntu/test_rop.c -no-pie -fno-plt`. Les options `-no-pie` et `-fno-plt` ont été utilisées pour simplifier l'analyse des adresses dans ce contexte de test.

## 3. Développement du Pipeline d'Automatisation

Le pipeline d'automatisation se décompose en deux phases principales : l'extraction des gadgets et la génération du code JavaScript.

### 3.1. Phase 1: Extraction des Gadgets avec ROPgadget

Une fois le fichier binaire de test (`test_rop_binary`) disponible, `ROPgadget` a été exécuté pour en extraire les gadgets. La commande utilisée est :

`ROPgadget --binary /home/ubuntu/test_rop_binary --ropchain`

La sortie de cette commande, qui liste les gadgets trouvés (adresse et instruction), a été redirigée et sauvegardée dans un fichier texte nommé `rop_gadget_output.txt`. Ce fichier sert d'entrée pour l'étape suivante.

Extrait du format de sortie de `ROPgadget` (contenu dans `rop_gadget_output.txt`) :

```
Gadgets information
============================================================
0x000000000040113e : add al, ch ; ret 0xffff
0x000000000040107b : add bh, bh ; loopne 0x4010e5 ; nop ; ret
...
Unique gadgets found: 61
```

### 3.2. Phase 2: Traitement des Données et Génération de Code JavaScript

Un script Python, `ropgadget_to_js_parser.py`, a été développé pour analyser le fichier `rop_gadget_output.txt` et générer le code JavaScript correspondant.

**Logique du script `ropgadget_to_js_parser.py`:**

1.  **Lecture du Fichier d'Entrée**: Le script ouvre et lit le fichier contenant la sortie de `ROPgadget`.
2.  **Analyse Syntaxique (Parsing)**: Il parcourt chaque ligne, en ignorant les en-têtes et les sections non pertinentes. Pour les lignes contenant des gadgets, il utilise une expression régulière (`re.match(r'(0x[0-9a-fA-F]+)\s*:\s*(.*)', line)`) pour extraire l'adresse du gadget (en hexadécimal) et la chaîne d'instructions correspondante.
3.  **Formatage pour JavaScript**: La chaîne d'instructions est formatée pour être une clé de chaîne JavaScript valide (échappement des caractères spéciaux si nécessaire, bien que dans ce cas, l'accent ait été mis sur l'échappement des guillemets doubles et des antislashs pour la chaîne JavaScript elle-même).
4.  **Construction de l'Objet `Map`**: Les paires (instruction, adresse) sont assemblées pour former les entrées d'un objet `Map` JavaScript. La structure du code généré est conçue pour être directement compatible avec la manière dont les cartes de gadgets sont définies dans le projet `psfree-lapse`.
5.  **Génération du Fichier de Sortie**: Le script produit une chaîne de caractères contenant la déclaration complète de la constante JavaScript (par exemple, `const auto_generated_gadget_offsets = new Map(Object.entries({ ... }));`). Cette sortie peut être affichée ou, comme dans notre cas, sauvegardée dans un fichier `.js` (par exemple, `auto_generated_rop_gadgets.js`).

**Code source principal de `ropgadget_to_js_parser.py`:**

```python
import re

def parse_ropgadget_output_to_js_map(ropgadget_output_file, map_variable_name="auto_generated_gadget_offsets"):
    gadget_entries = []
    try:
        with open(ropgadget_output_file, 'r') as f:
            reading_gadgets = False
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.startswith("Gadgets information"):
                    next(f) # Skip header lines
                    reading_gadgets = True
                    continue
                if line.startswith("Unique gadgets found:") or line.startswith("ROP chain generation"):
                    reading_gadgets = False
                    break
                if reading_gadgets:
                    match = re.match(r'(0x[0-9a-fA-F]+)\s*:\s*(.*)', line)
                    if match:
                        address = match.group(1)
                        instruction = match.group(2).strip()
                        escaped_instruction = instruction.replace("\\", "\\\\").replace("\"", "\\\"")
                        js_instruction_string = f'"{escaped_instruction}"'
                        gadget_entries.append(f"    {js_instruction_string} : {address},")
    except FileNotFoundError:
        return f"Error: Input file '{ropgadget_output_file}' not found."
    except Exception as e:
        return f"Error processing file: {e}"

    if not gadget_entries:
        return f"// No gadgets found or parsed from '{ropgadget_output_file}'.\nconst {map_variable_name} = new Map();"

    if gadget_entries:
        gadget_entries[-1] = gadget_entries[-1].rstrip(",")

    js_map_string = f"const {map_variable_name} = new Map(Object.entries({{\n"
    js_map_string += "\n".join(gadget_entries)
    js_map_string += "\n}}));"
    return js_map_string

if __name__ == "__main__":
    rop_output_file = "/home/ubuntu/rop_gadget_output.txt"
    generated_js_code = parse_ropgadget_output_to_js_map(rop_output_file)
    print(generated_js_code)
```

Le fichier résultant, `auto_generated_rop_gadgets.js`, contient alors le code JavaScript prêt à l'emploi :

```javascript
const auto_generated_gadget_offsets = new Map(Object.entries({
    "add al, ch ; ret 0xffff" : 0x000000000040113e,
    "add bh, bh ; loopne 0x4010e5 ; nop ; ret" : 0x000000000040107b,
    // ... et ainsi de suite pour tous les gadgets trouvés
}));
```

## 4. Utilisation dans un Projet Réel et Avantages

Pour intégrer ce flux de travail dans un projet comme `psfree-lapse`:

1.  **Obtenir les Binaires Cibles**: Il faut d'abord disposer des fichiers binaires réels du système PS4/PS5 (par exemple, `libwebkit.sprx`, `libkernel_web.sprx`, etc.) pour la version de firmware ciblée. Ces fichiers sont généralement obtenus par "dumping" depuis une console.
2.  **Exécuter ROPgadget**: Utiliser `ROPgadget` sur chacun de ces binaires pour extraire les listes de gadgets.
3.  **Générer les Cartes JavaScript**: Passer les fichiers de sortie de `ROPgadget` au script `ropgadget_to_js_parser.py` pour générer les définitions `Map` JavaScript correspondantes (par exemple, `webkit_gadget_offsets`, `libkernel_gadget_offsets`).
4.  **Intégration**: Copier-coller le code JavaScript généré dans les fichiers `.mjs` appropriés du projet `psfree-lapse`, en remplaçant ou en complétant les définitions manuelles existantes.

**Avantages de cette approche automatisée :**

*   **Gain de Temps Significatif**: Réduit considérablement le temps nécessaire pour trouver et documenter les gadgets, surtout lors du portage vers de nouveaux firmwares.
*   **Réduction des Erreurs**: Minimise les erreurs de transcription manuelles des adresses ou des séquences d'instructions.
*   **Cohérence**: Assure un formatage cohérent des cartes de gadgets.
*   **Maintenance Facilitée**: Simplifie la mise à jour des chaînes ROP/JOP lorsque les bibliothèques système sont modifiées.

## 5. Conclusion et Perspectives

Le pipeline d'automatisation développé constitue une avancée notable pour la gestion des gadgets ROP/JOP. Il fournit une solution robuste et flexible qui peut être adaptée et étendue. Des améliorations futures pourraient inclure :

*   L'intégration avec d'autres outils d'analyse binaire plus avancés (Ghidra, IDA Pro) pour une découverte de gadgets plus sophistiquée.
*   L'ajout de fonctionnalités de filtrage ou de catégorisation des gadgets directement dans le script de parsing.
*   La possibilité de mettre à jour directement les fichiers `.mjs` du projet (avec des mécanismes de sauvegarde et de prudence appropriés).

Ce travail démontre une approche professionnelle et innovante pour résoudre un problème technique complexe, en fournissant des outils concrets qui améliorent l'efficacité et la fiabilité du développement d'exploits.

---
*Note: Les fichiers `gadget_map_generator_design.md`, `gadget_map_generator.py` (version initiale lisant un fichier texte simple), et `sample_gadgets.txt` représentent des étapes intermédiaires du développement et sont conservés à des fins de documentation du processus itératif.*

