#!/usr/bin/env python3
"""Regression tests for the permanent Human Route runtime boundary (#101)."""

from __future__ import annotations

import unittest

import human_route_runtime as human_route
import render_site


class HumanRouteRuntimeTests(unittest.TestCase):
    def test_interaction_contract_is_standalone_not_text_patch(self) -> None:
        self.assertIn("function ensureStatus(section)", human_route.MAP_SCRIPT)
        self.assertIn("正在加载局部地图…", human_route.MAP_SCRIPT)
        self.assertIn("地图中心已更新。", human_route.MAP_SCRIPT)
        self.assertIn("可以重试", human_route.MAP_SCRIPT)
        self.assertIn("prefers-reduced-motion", human_route.MAP_SCRIPT)
        self.assertNotIn("_replace_once", human_route.MAP_SCRIPT)

    def test_runtime_contract_replaces_legacy_map_script(self) -> None:
        original_script = render_site.MAP_SCRIPT
        original_style = render_site.STYLE
        try:
            human_route.install_runtime_contract(render_site)
            self.assertEqual(render_site.MAP_SCRIPT, human_route.MAP_SCRIPT)
            self.assertIn(human_route.INTERACTION_STYLE, render_site.STYLE)
        finally:
            render_site.MAP_SCRIPT = original_script
            render_site.STYLE = original_style

    def test_human_type_labels_hide_raw_core_enums(self) -> None:
        cases = (
            ({"type": "system"}, "系统"),
            ({"type": "concept"}, "概念"),
            ({"type": "artifact"}, "制品"),
            ({"type": "agent"}, "主体 / 组织"),
        )
        for record, expected in cases:
            with self.subTest(record=record):
                self.assertEqual(human_route.human_object_type_label(record), expected)

    def test_semantic_view_label_takes_precedence(self) -> None:
        record = {"type": "system", "kind": "platform_service"}
        label = human_route.human_object_type_label(record, lambda _: "implementation")
        self.assertEqual(label, "实现")


if __name__ == "__main__":
    unittest.main()
