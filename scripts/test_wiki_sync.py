"""Tests for wiki_sync.py that need no network and no pandoc."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wiki_sync  # noqa: E402


class TitleToPath(unittest.TestCase):
    def test_subpage_becomes_directory(self):
        p = wiki_sync.title_to_path("Company Brain/Approvals")
        self.assertEqual(p.relative_to(wiki_sync.MIRROR_DIR).as_posix(), "Company Brain/Approvals.wiki")

    def test_windows_unsafe_characters_are_escaped(self):
        p = wiki_sync.title_to_path("Outreach: how to describe us?")
        self.assertEqual(p.name, "Outreach%3A how to describe us%3F.wiki")


class PlanPublish(unittest.TestCase):
    def entry(self, text="new"):
        return [{"title": "T", "source": "docs/t.md", "text": text}]

    def test_missing_page_is_created(self):
        self.assertEqual(wiki_sync.plan_publish(self.entry(), {"T": {}}, "Bot@sync")[0][2], "create")

    def test_identical_page_is_left_alone(self):
        cur = {"T": {"text": "new\n", "user": "Someone"}}
        self.assertEqual(wiki_sync.plan_publish(self.entry(), cur, "Bot@sync")[0][2], "same")

    def test_page_last_edited_by_the_bot_is_updated(self):
        cur = {"T": {"text": "old", "user": "Bot"}}
        self.assertEqual(wiki_sync.plan_publish(self.entry(), cur, "Bot@sync")[0][2], "update")

    def test_page_last_edited_by_a_person_is_refused(self):
        cur = {"T": {"text": "old", "user": "Chris"}}
        self.assertEqual(wiki_sync.plan_publish(self.entry(), cur, "Bot@sync")[0][2], "refuse")

    def test_without_a_bot_name_any_change_is_refused(self):
        cur = {"T": {"text": "old", "user": "Bot"}}
        self.assertEqual(wiki_sync.plan_publish(self.entry(), cur, "")[0][2], "refuse")


if __name__ == "__main__":
    unittest.main()
