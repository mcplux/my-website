from wagtail import blocks


class SocialLinkBlock(blocks.StructBlock):
    name = blocks.CharBlock(help_text="Social name (e.g. GitHub)")
    icon = blocks.CharBlock(
        help_text="Lucide icon name (e.g. github, linkedin, twitter)"
    )
    url = blocks.URLBlock()

    class Meta:
        icon = "link"
        label = "Social Link"
