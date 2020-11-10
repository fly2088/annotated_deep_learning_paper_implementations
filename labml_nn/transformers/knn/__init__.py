"""
# $k$NN-LM

This is an implementation of the paper
 [Generalization through Memorization: Nearest Neighbor Language Models](https://arxiv.org/abs/1911.00172).
It uses k-nearest neighbors to  improve perplexity of autoregressive transformer models.

An autoregressive language model estimates $p(w_t, \color{yellowgreen}{c_t})$,
 where $w_t$ is the token at step $t$
 and $c_t$ is the context, $\color{yellowgreen}{c_t} = (w_1, w_2, ..., w_{t-1})$.

This paper, improves  $p(w_t, c_t)$ using a k-nearest neighbor search
 on key-value pairs $\big(f(c_i), w_i\big)$, with search key $f(\color{yellowgreen}{c_t})$.
 Here $f(\color{yellowgreen}{c_t})$ is an embedding of the context $c_t$.
 The paper (and this implementation) uses the *input* to the feed-forward layer of the
 final layer of the transformer as $f(\color{yellowgreen}{c_t})$.

So to run $k$NN-LM we need to:

* [Train a transformer model](train_model.html)
* [Build an index](build_index.html) of $\big(f(c_i), w_i\big)$
* [Evaluate kNN-ML](eval_knn.html) using $k$NN seach on $\big(f(c_i), w_i\big)$
with  $f(c_t)$

This experiment uses a small dataset so that we can run this without using up a few hundred giga-bytes
of disk space for the index.

The official implementation of $k$NN-LM can be found [here](https://github.com/urvashik/knnlm).
"""