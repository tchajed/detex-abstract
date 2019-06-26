# detex abstract

Turns a LaTeX abstract into a Markdown abstract.

For example, `detex-abstract.py --sys 'Argosy' abstr.tex` turns this:

```tex
% Reasoning about storage systems is challenging because these systems make
% persistence guarantees even if the system crashes at any point. To achieve these
% crash-safety guarantees, storage systems include recovery procedures to restore
% the system to a consistent state after a crash. Moreover, large-scale systems
% are structured as a stack of layers and can require recovery at multiple layers
% of abstraction.
%
% Formal verification can ensure that
% crash-safety guarantees hold regardless of when the system crashes. To make
% verification tractable, large-scale systems should be verified in a modular
% fashion, layer-by-layer in the software stack. Layered recovery makes modularity
% challenging because the system can crash in the middle of a high-level recovery
% procedure and must start over with the low-level recovery procedure.
Storage systems make persistence guarantees even if the system crashes at any
time, which they achieve using recovery procedures that run after a crash.
We present \sys, a framework for machine-checked proofs of storage systems that
supports layered recovery implementations with modular proofs.
Reasoning about layered recovery procedures is especially challenging
because the system can crash in the middle of a more abstract layer's recovery
procedure and must start over with the lowest-level recovery procedure.
%\sys introduces a
%notion of recovery refinement as the basis for crash safety theorems. To
%construct a recovery refinement, the developer implements a high-level storage
%API (e.g., transactional writes to disk) using a lower-level API (e.g., reads
%and writes of disk blocks) and supplies a recovery procedure to give client
%programs atomic crash behavior. Recovery refinement includes a set of proof
%obligations about the correctness of the implementation. \sys in exchange
%provides a proof that composes implementations, recovery procedures (recovering
%from the bottom layer up), and these proofs obligations to prove the end-to-end
%system correct.
%

This paper introduces \emph{recovery refinement}, a set of conditions that ensure
proper implementation of an interface with a recovery procedure. \sys includes a proof that recovery refinements compose, using Kleene algebra for
concise definitions and metatheory.
We implemented Crash
Hoare Logic, the program logic used by FSCQ~\cite{chen:fscq}, to prove recovery refinement, and
demonstrated the whole system by verifying an example of layered recovery featuring a write-ahead log
running on top of a disk replication system. The metatheory of the framework,
the soundness of the program logic, and these examples are all verified in the
Coq proof assistant.
```

into this:

```md
Storage systems make persistence guarantees even if the system crashes
at any time, which they achieve using recovery procedures that run after
a crash.  We present Argosy, a framework for machine-checked proofs of
storage systems that supports layered recovery implementations with
modular proofs.  Reasoning about layered recovery procedures is
especially challenging because the system can crash in the middle of a
more abstract layer's recovery procedure and must start over with the
lowest-level recovery procedure.

This paper introduces recovery refinement, a set of conditions that
ensure proper implementation of an interface with a recovery procedure.
Argosy includes a proof that recovery refinements compose, using Kleene
algebra for concise definitions and metatheory.  We implemented Crash
Hoare Logic, the program logic used by FSCQ, to prove recovery
refinement, and demonstrated the whole system by verifying an example of
layered recovery featuring a write-ahead log running on top of a disk
replication system. The metatheory of the framework, the soundness of
the program logic, and these examples are all verified in the Coq proof
assistant.
```
