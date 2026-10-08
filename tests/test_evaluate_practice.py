"""Kiểm tra lệnh chấm chạy TrackEval trong tiến trình có alias NumPy."""

from evaluate_practice import run_trackeval


def test_run_trackeval_patches_numpy_in_child(tmp_path):
    script = tmp_path / "scripts" / "run_mot_challenge.py"
    script.parent.mkdir()
    script.write_text(
        "import numpy as np\n"
        "assert np.float is float and np.int is int\n"
    )
    run_trackeval(tmp_path, "test", "MOT17", "train")
