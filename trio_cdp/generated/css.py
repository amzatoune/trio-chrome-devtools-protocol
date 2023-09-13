# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.css
from cdp.css import (
    CSSComputedStyleProperty,
    CSSContainerQuery,
    CSSKeyframeRule,
    CSSKeyframesRule,
    CSSLayer,
    CSSLayerData,
    CSSMedia,
    CSSPositionFallbackRule,
    CSSProperty,
    CSSRule,
    CSSScope,
    CSSStyle,
    CSSStyleSheetHeader,
    CSSSupports,
    CSSTryRule,
    FontFace,
    FontVariationAxis,
    FontsUpdated,
    InheritedPseudoElementMatches,
    InheritedStyleEntry,
    MediaQuery,
    MediaQueryExpression,
    MediaQueryResultChanged,
    PlatformFontUsage,
    PseudoElementMatches,
    RuleMatch,
    RuleUsage,
    SelectorList,
    ShorthandEntry,
    SourceRange,
    StyleDeclarationEdit,
    StyleSheetAdded,
    StyleSheetChanged,
    StyleSheetId,
    StyleSheetOrigin,
    StyleSheetRemoved,
    Value
)


async def add_rule(
        style_sheet_id: StyleSheetId,
        rule_text: str,
        location: SourceRange
    ) -> CSSRule:
    '''
    Inserts a new rule with the given ``ruleText`` in a stylesheet with given ``styleSheetId``, at the
    position specified by ``location``.

    :param style_sheet_id: The css style sheet identifier where a new rule should be inserted.
    :param rule_text: The text of a new rule.
    :param location: Text position of a new rule in the target style sheet.
    :returns: The newly created rule.
    '''
    session = get_session_context('css.add_rule')
    return await session.execute(cdp.css.add_rule(style_sheet_id, rule_text, location))


async def collect_class_names(
        style_sheet_id: StyleSheetId
    ) -> typing.List[str]:
    '''
    Returns all class names from specified stylesheet.

    :param style_sheet_id:
    :returns: Class name list.
    '''
    session = get_session_context('css.collect_class_names')
    return await session.execute(cdp.css.collect_class_names(style_sheet_id))


async def create_style_sheet(
        frame_id: cdp.page.FrameId
    ) -> StyleSheetId:
    '''
    Creates a new special "via-inspector" stylesheet in the frame with given ``frameId``.

    :param frame_id: Identifier of the frame where "via-inspector" stylesheet should be created.
    :returns: Identifier of the created "via-inspector" stylesheet.
    '''
    session = get_session_context('css.create_style_sheet')
    return await session.execute(cdp.css.create_style_sheet(frame_id))


async def disable() -> None:
    '''
    Disables the CSS agent for the given page.
    '''
    session = get_session_context('css.disable')
    return await session.execute(cdp.css.disable())


async def enable() -> None:
    '''
    Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been
    enabled until the result of this command is received.
    '''
    session = get_session_context('css.enable')
    return await session.execute(cdp.css.enable())


async def force_pseudo_state(
        node_id: cdp.dom.NodeId,
        forced_pseudo_classes: typing.List[str]
    ) -> None:
    '''
    Ensures that the given node will have specified pseudo-classes whenever its style is computed by
    the browser.

    :param node_id: The element id for which to force the pseudo state.
    :param forced_pseudo_classes: Element pseudo classes to force when computing the element's style.
    '''
    session = get_session_context('css.force_pseudo_state')
    return await session.execute(cdp.css.force_pseudo_state(node_id, forced_pseudo_classes))


async def get_background_colors(
        node_id: cdp.dom.NodeId
    ) -> typing.Tuple[typing.Optional[typing.List[str]], typing.Optional[str], typing.Optional[str]]:
    '''
    :param node_id: Id of the node to get background colors for.
    :returns: A tuple with the following items:

        0. **backgroundColors** - *(Optional)* The range of background colors behind this element, if it contains any visible text. If no visible text is present, this will be undefined. In the case of a flat background color, this will consist of simply that color. In the case of a gradient, this will consist of each of the color stops. For anything more complicated, this will be an empty array. Images will be ignored (as if the image had failed to load).
        1. **computedFontSize** - *(Optional)* The computed font size for this node, as a CSS computed value string (e.g. '12px').
        2. **computedFontWeight** - *(Optional)* The computed font weight for this node, as a CSS computed value string (e.g. 'normal' or '100').
    '''
    session = get_session_context('css.get_background_colors')
    return await session.execute(cdp.css.get_background_colors(node_id))


async def get_computed_style_for_node(
        node_id: cdp.dom.NodeId
    ) -> typing.List[CSSComputedStyleProperty]:
    '''
    Returns the computed style for a DOM node identified by ``nodeId``.

    :param node_id:
    :returns: Computed style for the specified DOM node.
    '''
    session = get_session_context('css.get_computed_style_for_node')
    return await session.execute(cdp.css.get_computed_style_for_node(node_id))


async def get_inline_styles_for_node(
        node_id: cdp.dom.NodeId
    ) -> typing.Tuple[typing.Optional[CSSStyle], typing.Optional[CSSStyle]]:
    '''
    Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM
    attributes) for a DOM node identified by ``nodeId``.

    :param node_id:
    :returns: A tuple with the following items:

        0. **inlineStyle** - *(Optional)* Inline style for the specified DOM node.
        1. **attributesStyle** - *(Optional)* Attribute-defined element style (e.g. resulting from "width=20 height=100%").
    '''
    session = get_session_context('css.get_inline_styles_for_node')
    return await session.execute(cdp.css.get_inline_styles_for_node(node_id))


async def get_layers_for_node(
        node_id: cdp.dom.NodeId
    ) -> CSSLayerData:
    '''
    Returns all layers parsed by the rendering engine for the tree scope of a node.
    Given a DOM element identified by nodeId, getLayersForNode returns the root
    layer for the nearest ancestor document or shadow root. The layer root contains
    the full layer tree for the tree scope and their ordering.

    **EXPERIMENTAL**

    :param node_id:
    :returns: 
    '''
    session = get_session_context('css.get_layers_for_node')
    return await session.execute(cdp.css.get_layers_for_node(node_id))


async def get_matched_styles_for_node(
        node_id: cdp.dom.NodeId
    ) -> typing.Tuple[typing.Optional[CSSStyle], typing.Optional[CSSStyle], typing.Optional[typing.List[RuleMatch]], typing.Optional[typing.List[PseudoElementMatches]], typing.Optional[typing.List[InheritedStyleEntry]], typing.Optional[typing.List[InheritedPseudoElementMatches]], typing.Optional[typing.List[CSSKeyframesRule]], typing.Optional[typing.List[CSSPositionFallbackRule]], typing.Optional[cdp.dom.NodeId]]:
    '''
    Returns requested styles for a DOM node identified by ``nodeId``.

    :param node_id:
    :returns: A tuple with the following items:

        0. **inlineStyle** - *(Optional)* Inline style for the specified DOM node.
        1. **attributesStyle** - *(Optional)* Attribute-defined element style (e.g. resulting from "width=20 height=100%").
        2. **matchedCSSRules** - *(Optional)* CSS rules matching this node, from all applicable stylesheets.
        3. **pseudoElements** - *(Optional)* Pseudo style matches for this node.
        4. **inherited** - *(Optional)* A chain of inherited styles (from the immediate node parent up to the DOM tree root).
        5. **inheritedPseudoElements** - *(Optional)* A chain of inherited pseudo element styles (from the immediate node parent up to the DOM tree root).
        6. **cssKeyframesRules** - *(Optional)* A list of CSS keyframed animations matching this node.
        7. **cssPositionFallbackRules** - *(Optional)* A list of CSS position fallbacks matching this node.
        8. **parentLayoutNodeId** - *(Optional)* Id of the first parent element that does not have display: contents.
    '''
    session = get_session_context('css.get_matched_styles_for_node')
    return await session.execute(cdp.css.get_matched_styles_for_node(node_id))


async def get_media_queries() -> typing.List[CSSMedia]:
    '''
    Returns all media queries parsed by the rendering engine.

    :returns: 
    '''
    session = get_session_context('css.get_media_queries')
    return await session.execute(cdp.css.get_media_queries())


async def get_platform_fonts_for_node(
        node_id: cdp.dom.NodeId
    ) -> typing.List[PlatformFontUsage]:
    '''
    Requests information about platform fonts which we used to render child TextNodes in the given
    node.

    :param node_id:
    :returns: Usage statistics for every employed platform font.
    '''
    session = get_session_context('css.get_platform_fonts_for_node')
    return await session.execute(cdp.css.get_platform_fonts_for_node(node_id))


async def get_style_sheet_text(
        style_sheet_id: StyleSheetId
    ) -> str:
    '''
    Returns the current textual content for a stylesheet.

    :param style_sheet_id:
    :returns: The stylesheet text.
    '''
    session = get_session_context('css.get_style_sheet_text')
    return await session.execute(cdp.css.get_style_sheet_text(style_sheet_id))


async def set_container_query_text(
        style_sheet_id: StyleSheetId,
        range_: SourceRange,
        text: str
    ) -> CSSContainerQuery:
    '''
    Modifies the expression of a container query.

    **EXPERIMENTAL**

    :param style_sheet_id:
    :param range_:
    :param text:
    :returns: The resulting CSS container query rule after modification.
    '''
    session = get_session_context('css.set_container_query_text')
    return await session.execute(cdp.css.set_container_query_text(style_sheet_id, range_, text))


async def set_effective_property_value_for_node(
        node_id: cdp.dom.NodeId,
        property_name: str,
        value: str
    ) -> None:
    '''
    Find a rule with the given active property for the given node and set the new value for this
    property

    :param node_id: The element id for which to set property.
    :param property_name:
    :param value:
    '''
    session = get_session_context('css.set_effective_property_value_for_node')
    return await session.execute(cdp.css.set_effective_property_value_for_node(node_id, property_name, value))


async def set_keyframe_key(
        style_sheet_id: StyleSheetId,
        range_: SourceRange,
        key_text: str
    ) -> Value:
    '''
    Modifies the keyframe rule key text.

    :param style_sheet_id:
    :param range_:
    :param key_text:
    :returns: The resulting key text after modification.
    '''
    session = get_session_context('css.set_keyframe_key')
    return await session.execute(cdp.css.set_keyframe_key(style_sheet_id, range_, key_text))


async def set_local_fonts_enabled(
        enabled: bool
    ) -> None:
    '''
    Enables/disables rendering of local CSS fonts (enabled by default).

    **EXPERIMENTAL**

    :param enabled: Whether rendering of local fonts is enabled.
    '''
    session = get_session_context('css.set_local_fonts_enabled')
    return await session.execute(cdp.css.set_local_fonts_enabled(enabled))


async def set_media_text(
        style_sheet_id: StyleSheetId,
        range_: SourceRange,
        text: str
    ) -> CSSMedia:
    '''
    Modifies the rule selector.

    :param style_sheet_id:
    :param range_:
    :param text:
    :returns: The resulting CSS media rule after modification.
    '''
    session = get_session_context('css.set_media_text')
    return await session.execute(cdp.css.set_media_text(style_sheet_id, range_, text))


async def set_rule_selector(
        style_sheet_id: StyleSheetId,
        range_: SourceRange,
        selector: str
    ) -> SelectorList:
    '''
    Modifies the rule selector.

    :param style_sheet_id:
    :param range_:
    :param selector:
    :returns: The resulting selector list after modification.
    '''
    session = get_session_context('css.set_rule_selector')
    return await session.execute(cdp.css.set_rule_selector(style_sheet_id, range_, selector))


async def set_scope_text(
        style_sheet_id: StyleSheetId,
        range_: SourceRange,
        text: str
    ) -> CSSScope:
    '''
    Modifies the expression of a scope at-rule.

    **EXPERIMENTAL**

    :param style_sheet_id:
    :param range_:
    :param text:
    :returns: The resulting CSS Scope rule after modification.
    '''
    session = get_session_context('css.set_scope_text')
    return await session.execute(cdp.css.set_scope_text(style_sheet_id, range_, text))


async def set_style_sheet_text(
        style_sheet_id: StyleSheetId,
        text: str
    ) -> typing.Optional[str]:
    '''
    Sets the new stylesheet text.

    :param style_sheet_id:
    :param text:
    :returns: *(Optional)* URL of source map associated with script (if any).
    '''
    session = get_session_context('css.set_style_sheet_text')
    return await session.execute(cdp.css.set_style_sheet_text(style_sheet_id, text))


async def set_style_texts(
        edits: typing.List[StyleDeclarationEdit]
    ) -> typing.List[CSSStyle]:
    '''
    Applies specified style edits one after another in the given order.

    :param edits:
    :returns: The resulting styles after modification.
    '''
    session = get_session_context('css.set_style_texts')
    return await session.execute(cdp.css.set_style_texts(edits))


async def set_supports_text(
        style_sheet_id: StyleSheetId,
        range_: SourceRange,
        text: str
    ) -> CSSSupports:
    '''
    Modifies the expression of a supports at-rule.

    **EXPERIMENTAL**

    :param style_sheet_id:
    :param range_:
    :param text:
    :returns: The resulting CSS Supports rule after modification.
    '''
    session = get_session_context('css.set_supports_text')
    return await session.execute(cdp.css.set_supports_text(style_sheet_id, range_, text))


async def start_rule_usage_tracking() -> None:
    '''
    Enables the selector recording.
    '''
    session = get_session_context('css.start_rule_usage_tracking')
    return await session.execute(cdp.css.start_rule_usage_tracking())


async def stop_rule_usage_tracking() -> typing.List[RuleUsage]:
    '''
    Stop tracking rule usage and return the list of rules that were used since last call to
    ``takeCoverageDelta`` (or since start of coverage instrumentation).

    :returns: 
    '''
    session = get_session_context('css.stop_rule_usage_tracking')
    return await session.execute(cdp.css.stop_rule_usage_tracking())


async def take_computed_style_updates() -> typing.List[cdp.dom.NodeId]:
    '''
    Polls the next batch of computed style updates.

    **EXPERIMENTAL**

    :returns: The list of node Ids that have their tracked computed styles updated.
    '''
    session = get_session_context('css.take_computed_style_updates')
    return await session.execute(cdp.css.take_computed_style_updates())


async def take_coverage_delta() -> typing.Tuple[typing.List[RuleUsage], float]:
    '''
    Obtain list of rules that became used since last call to this method (or since start of coverage
    instrumentation).

    :returns: A tuple with the following items:

        0. **coverage** - 
        1. **timestamp** - Monotonically increasing time, in seconds.
    '''
    session = get_session_context('css.take_coverage_delta')
    return await session.execute(cdp.css.take_coverage_delta())


async def track_computed_style_updates(
        properties_to_track: typing.List[CSSComputedStyleProperty]
    ) -> None:
    '''
    Starts tracking the given computed styles for updates. The specified array of properties
    replaces the one previously specified. Pass empty array to disable tracking.
    Use takeComputedStyleUpdates to retrieve the list of nodes that had properties modified.
    The changes to computed style properties are only tracked for nodes pushed to the front-end
    by the DOM agent. If no changes to the tracked properties occur after the node has been pushed
    to the front-end, no updates will be issued for the node.

    **EXPERIMENTAL**

    :param properties_to_track:
    '''
    session = get_session_context('css.track_computed_style_updates')
    return await session.execute(cdp.css.track_computed_style_updates(properties_to_track))