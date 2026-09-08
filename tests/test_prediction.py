import pytest

from src import predict


def test_load_artifacts_raises_clear_error_when_missing(monkeypatch, tmp_path):
    monkeypatch.setattr(predict.config, "MODELS_DIR", tmp_path)
    with pytest.raises(predict.ArtifactsNotFoundError):
        predict.load_artifacts()
