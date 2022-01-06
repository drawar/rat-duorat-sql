{
    logdir: "logdir/bert_run",
    model_config: "configs/spider/nl2code-bert.jsonnet",
    model_config_args: {
        data_path: 'third_party/spider/',
        bs: 2,
        num_batch_accumulated: 12,
        bert_version: "bert-large-uncased-whole-word-masking",
        summarize_header: "avg",
        use_column_type: false,
        max_steps: 81000,
        num_layers: 8,
        lr: 7.44e-4,
        bert_lr: 1e-5,
        att: 1,
        end_lr: 0,
        sc_link: true,
        cv_link: true,
        use_align_mat: true,
        use_align_loss: true,
        bert_token_type: true,
        decoder_hidden_size: 512,
        end_with_from: true, # equivalent to "SWGOIF" if true
        clause_order: null, # strings like "SWGOIF", it will be prioriotized over end_with_from
    },

    eval_name: "run_%s_%d" % [self.eval_use_heuristic, self.eval_beam_size],
    eval_output: "logdir/bert_run/ie_dirs",
    eval_beam_size: 1,
    eval_use_heuristic: true,
    eval_steps: [ 10000 * x for x in std.range(4, 8)],
    eval_section: "val",
}
