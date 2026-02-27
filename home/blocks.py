from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class AboutBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(form_classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()
    quote = blocks.BlockQuoteBlock()


class SocialLinkBlock(blocks.StructBlock):
    name = blocks.CharBlock(help_text="Social name (e.g. GitHub)")
    icon = blocks.CharBlock(
        help_text="Lucide icon name (e.g. github, linkedin, twitter)"
    )
    url = blocks.URLBlock()

    class Meta:
        icon = "link"
        label = "Social Link"
